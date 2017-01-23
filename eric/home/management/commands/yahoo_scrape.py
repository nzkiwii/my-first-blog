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
from bs4 import BeautifulSoup
import time
import io
from tqdm import tqdm
import random
import re
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        all_companies = Company.objects.all()
        all_tickers = []

        for company in all_companies:
            all_tickers.append(company.ticker)

        for ticker in tqdm(all_tickers):
            url = 'http://finance.yahoo.com/quote/' + str(ticker) + '?p=' + str(ticker)
            stats_url = 'http://finance.yahoo.com/quote/' + str(ticker) + '/key-statistics?p=' + str(ticker)
            profile_url = 'http://finance.yahoo.com/quote/' + str(ticker) + '/profile?p=' + str(ticker)

            def get_info(url, stats_url, profile_url, ticker):
                try:
                    browser = webdriver.PhantomJS('C:/users/eric/desktop/edgar_alert/phantomjs-2.1.1-windows/bin/phantomjs.exe')

                    #front page
                    browser.get(url)
                    time.sleep(2)
                    parent_table = browser.find_element_by_id('quote-summary')
                    right_table = parent_table.find_elements_by_tag_name('div')[1]. \
                    find_element_by_tag_name('table').find_element_by_tag_name('tbody')
                    market_cap = right_table.find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[1].text
                    if market_cap[-1:] == 'M':
                        market_cap = float(market_cap.split('M')[0])*1000000
                    elif market_cap[-1:] == 'B':
                        market_cap = float(market_cap.split('B')[0])*1000000000
                    beta = right_table.find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text
                    EPS = right_table.find_elements_by_tag_name('tr')[3].find_elements_by_tag_name('td')[1].text

                    #stats page
                    browser.get(stats_url)
                    time.sleep(2)
                    PE_ratio = browser.find_element_by_xpath('//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/section/div[2]/div[1]/div[1]/div/table/tbody/tr[3]/td[2]').text
                    Price_To_Sales = browser.find_element_by_xpath('//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/section/div[2]/div[1]/div[1]/div/table/tbody/tr[6]/td[2]').text
                    Price_To_Book = browser.find_element_by_xpath('//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/section/div[2]/div[1]/div[1]/div/table/tbody/tr[7]/td[2]').text
                    EV_To_Rev = browser.find_element_by_xpath('//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/section/div[2]/div[1]/div[1]/div/table/tbody/tr[8]/td[2]').text
                    EV_To_EBITDA = browser.find_element_by_xpath('//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/section/div[2]/div[1]/div[1]/div/table/tbody/tr[9]/td[2]').text
                    def na_to_none(metric):
                        if metric == 'N/A':
                            metric = None
                        return metric
                    market_cap = na_to_none(market_cap)
                    beta = na_to_none(beta)
                    EPS = na_to_none(EPS)
                    PE_ratio = na_to_none(PE_ratio)
                    Price_To_Sales = na_to_none(Price_To_Sales)
                    Price_To_Book = na_to_none(Price_To_Book)
                    EV_To_Rev = na_to_none(EV_To_Rev)
                    EV_To_EBITDA = na_to_none(EV_To_EBITDA)

                    #profile_page
                    browser.get(profile_url)
                    time.sleep(2)
                    sector = browser.find_element_by_xpath('//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/div[1]/div/div/p[2]/strong[1]').text
                    industry = browser.find_element_by_xpath('//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/div[1]/div/div/p[2]/strong[2]').text
                    employee_count = browser.find_element_by_xpath('//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/div[1]/div/div/p[2]/strong[3]/span').text
                    employee_count = employee_count.replace(',', '')

                    company = Company.objects.get(ticker=str(ticker))
                    company.market_cap = market_cap
                    company.beta = beta
                    company.PE_ratio = PE_ratio
                    company.EPS = EPS
                    company.Price_To_Sales = Price_To_Sales
                    company.Price_To_Book = Price_To_Book
                    company.EV_To_Rev = EV_To_Rev
                    company.EV_To_EBITDA = EV_To_EBITDA
                    company.sector = sector
                    company.industry = industry
                    company.employee_count = employee_count
                    company.save()
                    browser.close()

                except Exception as e:
                    browser.get_screenshot_as_file('phantomjs-errors/%s.png' % ticker)
                    browser.close()


            get_info(url, stats_url, profile_url, ticker)
