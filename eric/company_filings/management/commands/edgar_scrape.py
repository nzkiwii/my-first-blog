from django.db import models
from django.core.management.base import BaseCommand, CommandError
from django.contrib import admin
from company_filings.models import CompanyFiling, SecurityAcquired
from home.models import Company
import smtplib
import datetime
import feedparser
import xml.etree.ElementTree as ET
import requests
import bs4
import time
import io
from tqdm import tqdm
import random


class Command(BaseCommand):

    def handle(self, *args, **options):

        #random header spoofing
        def LoadUserAgents(uafile):
            """
            uafile : string
                path to text file of user agents, one per line
            """
            uas = []
            with open(uafile, 'r') as uaf:
                for ua in uaf.readlines():
                    if ua:
                        uas.append(ua.strip()[1:-1-1])
            random.shuffle(uas)
            return uas

        uafile="headers.txt"
        all_headers = LoadUserAgents(uafile)
        header = random.choice(all_headers)
        headers = {
        "Connection" : "close",  # another way to cover tracks
        "User-Agent" : header}

        #all_tickers = Company.objects.all()
        all_tickers = ['NVDA', 'GOOG', 'GOOGL', 'APPL', 'TSLA']

        def process_tree(tree, ticker):
            def get_xml_metric(search):
                if search == None:
                    return None
                elif search.text == None:
                    return None
                else:
                    return search.text
            def get_filing_metric(search):
                if search == None:
                    return None
                else:
                    return search.text

            report_owner_name = get_xml_metric(tree.find('reportingOwner/reportingOwnerId/rptOwnerName'))
            ticker = get_xml_metric(tree.find('issuer/issuerTradingSymbol'))
            is_officer = get_xml_metric(tree.find('reportingOwner/reportingOwnerRelationship/isOfficer'))
            is_director = get_xml_metric(tree.find('reportingOwner/reportingOwnerRelationship/isDirector'))
            is_ten_percent_owner = get_xml_metric(tree.find('reportingOwner/reportingOwnerRelationship/isTenPercentOwner'))
            officer_title = get_xml_metric(tree.find('reportingOwner/reportingOwnerRelationship/officerTitle'))
            transaction_date = get_xml_metric(tree.find('periodOfReport'))
            filing_date = get_xml_metric(tree.find('ownerSignature/signatureDate'))
            #create company filing object
            filing = CompanyFiling.objects.update_or_create(company=Company.objects.get(ticker=ticker),
            report_owner_name=report_owner_name,
            ticker=ticker,
            is_officer=is_officer,
            is_director=is_director,
            is_ten_percent_owner=is_ten_percent_owner,
            officer_title=officer_title,
            transaction_date=transaction_date,
            filing_date=filing_date
            )
            filing
            for sec in tree.iter('nonDerivativeTransaction'):
                security_title = get_filing_metric(sec.find('securityTitle/value'))
                transaction_date = get_filing_metric(sec.find('transactionDate/value'))
                transaction_form_type = get_filing_metric(sec.find('transactionCoding/transactionFormType'))
                transaction_code = get_filing_metric(sec.find('transactionCoding/transactionCode'))
                transaction_shares = get_filing_metric(sec.find('transactionAmounts/transactionShares/value'))
                transaction_price_per_share = get_filing_metric(sec.find('transactionAmounts/transactionPricePerShare/value'))
                transaction_acquired_disposed_code = get_filing_metric(sec.find('transactionAquiredDisposedCode/value'))
                shares_owned_following_transaction = get_filing_metric(sec.find('postTransactionAmounts/sharesOwnedFollowingTransaction/value'))
                direct_or_indirect_ownership = get_filing_metric(sec.find('ownershipNature/directOrIndirectOwnershihp/value'))
                new_sec = SecurityAcquired.objects.update_or_create(filing=CompanyFiling.objects.get(id=filing[0].id),
                security_title=security_title,
                transaction_date=transaction_date,
                transaction_form_type=transaction_form_type,
                transaction_code=transaction_code,
                transaction_shares = transaction_shares,
                transaction_price_per_share=transaction_price_per_share,
                transaction_acquired_disposed_code = transaction_acquired_disposed_code,
                shares_owned_following_transaction = shares_owned_following_transaction,
                direct_or_indirect_ownership = direct_or_indirect_ownership)
                new_sec


        def edgar_scrape(ticker, headers):
            url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=' + str(ticker) + '&type=&dateb=&owner=only&count=100'
            #url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=' + str(ticker) + '&type=&dateb=&owner=only&count=100'
            res = requests.get(url, headers=headers)
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            for a in soup.find_all('a', href=True):
                if 'Documents' in a.text:
                    res = requests.get('https://www.sec.gov/' + str(a['href']), headers=headers)
                    soup = bs4.BeautifulSoup(res.text, 'html.parser')
                    for a in soup.find_all('a', href=True):
                         if a.getText()[-4:] == '.xml':
                            xml_url = 'https://www.sec.gov' + str(a['href'])
                            res = requests.get(xml_url, headers=headers)
                            time.sleep(1)
                            tree = ET.fromstring(res.content)
                            process_tree(tree, ticker)



        for ticker in tqdm(all_tickers):
            #try: edgar_scrape(ticker.ticke, headers)
            #except: pass
            edgar_scrape(ticker, headers)
