import smtplib
import datetime
import feedparser
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup
import time
import io
import random
import re
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

ticker = 'PIH'
print (ticker)
url = 'http://finance.yahoo.com/quote/' + str(ticker) + '?p=' + str(ticker)
stats_url = 'http://finance.yahoo.com/quote/' + str(ticker) + '/key-statistics?p=' + str(ticker)

def get_info(url, stats_url):
    
    binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/firefox.exe')
    #browser = webdriver.Firefox(firefox_binary=binary)
    browser = webdriver.PhantomJS('C:/users/eric/desktop/edgar_alert/phantomjs-2.1.1-windows/bin/phantomjs.exe')

    #front page
    browser.get(url)
    #soup = BeautifulSoup(browser.page_source.encode("utf-8"), 'html.parser')
    parent_table = browser.find_element_by_id('quote-summary')
    right_table = parent_table.find_elements_by_tag_name('div')[1]. \
    find_element_by_tag_name('table').find_element_by_tag_name('tbody')
    market_cap = right_table.find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[1].text
    if market_cap[-1:] == 'M':
        market_cap = float(market_cap.split('M')[0])*1000000
    elif market_cap[-1:] == 'B':
        market_cap = float(market_cap.split('B')[0])*1000000000
    beta = right_table.find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[1].text
    PE_ratio = right_table.find_elements_by_tag_name('tr')[2].find_elements_by_tag_name('td')[1].text

    #stats page
    browser.get(stats_url)
    time.sleep(2)
    print (stats_url)
    #try:
    left_table = browser.find_element_by_xpath('//*[@id="main-0-Quote-Proxy"]/section/div[2]/section/div/section/div[2]/div[1]/div[1]/div/table/tbody/tr[3]/td[2]')
    print (left_table.text)
    

        #find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')

    #     EPS = left_table[2].find_elements_by_tag_name('td')[1].text
    #     Price_To_Sales = left_table[5].find_elements_by_tag_name('td')[1].text
    #     Price_To_Book = left_table[6].find_elements_by_tag_name('td')[1].text
    #     EV_To_Rev = left_table[7].find_elements_by_tag_name('td')[1].text
    #     EV_To_EBITDA = left_table[8].find_elements_by_tag_name('td')[1].text
    # except:
    #     print ('this url has an error: ', stats_url)
    #     browser.get_screenshot_as_file('screenshot-phantomjs.png')


get_info(url, stats_url)
get_info(url, stats_url)
get_info(url, stats_url)
get_info(url, stats_url)
get_info(url, stats_url)
get_info(url, stats_url)
