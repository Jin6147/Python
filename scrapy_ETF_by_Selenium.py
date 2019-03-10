#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:38:14 2017

@author: JadeHo
"""
import os
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

group1=['0050','0051','0052','0053','0054','0055','0056','0057','0058','0059']
group2=['0061','006205','006206']
group3=['00635U','00642U']

def open_driver_to_get_html(url):
    #模擬打開Chrome來檢視原始碼
    driver = webdriver.Chrome()     
    driver.get(url)
    html = driver.page_source #get html
    driver.close()
    return html

def scrapy_all_etf(soup,group_id):
    #scrapy所有ETF資訊
    all_etf_list=[] 
    for id_ in group_id:
        etf_dict={} 
        etf_tr = soup.find(id=id_+'_tr')
        etf_dict['etf_name'] = etf_tr.find(id=id_+'_n').text #ETF代號/名稱
        etf_dict['etf_count'] = etf_tr.find(id=id_+'_c').text.replace(',','') #已發行受益權單位數
        etf_dict['etf_count2'] = etf_tr.find(id=id_+'_d').text #與前日已發行受益單位差異數
        etf_dict['etf_price'] = etf_tr.find(id=id_+'_e').text #成交價
        etf_dict['etf_env'] = etf_tr.find(id=id_+'_f').text #預估淨值
        etf_dict['etf_edp'] = etf_tr.find(id=id_+'_g').text #預估折溢價
        etf_dict['etf_pnv'] = etf_tr.find(id=id_+'_h').text #前一營業日淨值
        etf_dict['etf_link'] = etf_tr.find_all('a')[1].get('href') #投信網頁
        etf_dict['etf_time'] = etf_tr.find(id=id_+'_i').text #資料時間
        all_etf_list.append(etf_dict)
    
    return all_etf_list
        

'''
main
'''
url="http://mis.twse.com.tw/stock/etf_nav.jsp?ex=tse"

html_code = open_driver_to_get_html(url) #模擬打開Chrome來檢視原始碼
soup = BeautifulSoup(html_code, "lxml") 

group_id = group1+group1+group3  #整理欲爬的ETF群組
etf_list = scrapy_all_etf(soup=soup, group_id=group_id) #scrapy所有ETF資訊







