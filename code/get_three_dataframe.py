# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         get_three_dataframe
# Description:  
# Author:       Kuan-Hui Lin
# Date:         2020/4/27
# -------------------------------------------------------------------------------
# pip3 install fake_useragent

from __future__ import unicode_literals
from config import KIND_MAP_URL, LOCATIONS, LOCATIONS_MAP_KEYS
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from weather_place_data import get_weather_place_data
from fruit_combine import combine_fruit
from all_tables_combine import combine_all_tables
from graph import analyze_plotgraph
from fake_useragent import UserAgent
from write_csv import write_to_csv
from date_util import get_date_list
from directory import create_directory
import pandas as pd
import requests
import re
import os


# 抽取數據的正則表達式 (Regular expression for extracting data)
pat_row = re.compile(
     r'<tr class="ReportsTableCell2"><td><span>(\d+/\d+/\d+)</span></td><td><span>([\d.]+) - ([\d.]+)'
     r'</span></td><td><span>(.*?)</span></td><td><span>(.*?)</span></td><td><span>(.*?)</span></td><td>'
     r'<span>(.*?)</span></td><td>'
)
# 抽取頁數的正則表達式 (Regular expression for extracting the number of pages)
pat_page = re.compile(
    r'<font class="smaller">(<b>)?(\d+)([\s\S]+?)(</b>)?</font>'
)

# 獲取頁數 (get the number of pages)
def get_pages(html):
    objs = re.findall(pat_page, html)
    pages = len(objs)
    return int(pages)

# 獲取隨機請求頭 (get header)
def get_ua():
    """
    设置请求头
    :return:
    """
    location = os.getcwd() + '/fake_useragent.json'
    ua = UserAgent(path=location)  #verify_ssl=False
    return ua.random

# 獲取 html 代碼 (get html)
def get_html(url):
    headers = {
        'User-Agent': get_ua()
    }
    try:
        res = requests.get(url=url, headers=headers, timeout=60)
        if res.status_code == 200:
            html = res.text
            # with open('area.html', 'w') as ff:
            #     ff.write(html)
            return html
    except Exception as e:
        print('{}Request data failed'.format(url))
        print(e)
        return False


def generate_url(kind, date, location):
    """
    Build a request url
    :param kind: fruit tpye
    :param date: date 
    :param location: city 
    :return:
    """
    base_url = KIND_MAP_URL.get(kind)
    if base_url:
        base_url.format(location=location, date=date)
    else:
        return
    return base_url


def get_and_format_data(url, all_data, kind, location, everyday):
    """
    get every data (獲取每一條數據)
    :param url: requesting-complete url (請求的完整url)
    :param all_data: save all data (保存所有數據）
    :param kind: fruit type 
    :param location: city
    :param everyday: date
    :return:
    """
    html = str(get_html(url))
    pages = get_pages(html)
    if pages > 1:
        # 一般不會有超過一頁的情況，但避免發生，如果出現超過一頁的情況，記錄下來，再去單獨爬取 
        # (Generally, there will not be more than one page, but in order to avoid it, if there is more than one page, record it and go to crawl alone)
        print(url + 'has more than 1 page')

    for pat_obj in re.finditer(pat_row, html):
        # 正则獲取每一行數據 (get each row of data by using re group)
        data_row = [
            kind,
            location,
            everyday,
            pat_obj.group(2),
            pat_obj.group(3),
            pat_obj.group(5),
            pat_obj.group(7)
        ]
        all_data.append(data_row)
        print(kind, location, everyday, 'done!')


def main_task(filepath='./csv_files/fruit_price.csv'):
    """
    Start to get fruit data (開始獲取水果數據）
    :param filepath: Saved csv file name (保存的csv文件名稱）
    :return:
    """
    task_list = []
    # 線程池 (Thread Pool)
    executor = ThreadPoolExecutor(max_workers=60)
    date_list = get_date_list()
    all_data = []
    # 水果種類 (fruit type)
    for kind in KIND_MAP_URL:
        base_url = KIND_MAP_URL.get(kind)
        # 所有地区（loop for all locations）
        for location in LOCATIONS.get(kind):
            # each day on 01/02/2019-12/31/2019 (because the page on 01/01/2019 is broken)
            locAbr = LOCATIONS_MAP_KEYS.get(location)
            for everyday in date_list:
                # 日期中的/需要编码，直接替换，地區名稱如果含有空格需要轉為+ (The / in the date needs to be coded and directly replaced. If the area name contains spaces, it needs to be converted to +)
                url = base_url.format(date=everyday.replace('/', '%2F'), 
                                    location=location.replace(' ', '+'),
                                    locAbr=locAbr)
                # get_and_format_data(url, all_data, kind, location, everyday)
                print(kind, location, everyday)
                task_list.append(executor.submit(get_and_format_data, url, all_data, kind, location, everyday))
    # 等待所有線程跑完 (wait for all thread finish)
    wait(task_list, return_when=ALL_COMPLETED)
    print(len(all_data))
    write_to_csv(filepath, all_data)

if __name__ == '__main__':
    print(" ======= Get fruit and market price data ======== ")
    csvfolder = "./csv_files"
    create_directory(csvfolder)

    main_task('./csv_files/fruit_price.csv')
    fruit_csvdata = pd.read_csv('./csv_files/fruit_price.csv')
    fruit_price_df = pd.DataFrame(fruit_csvdata)

    print(" ======== Get place and weather data ========")
    place_df, weather_df= get_weather_place_data(csvfolder)
    print(" All grabing process are done! ")

    print(" ======== Preprocess fruit dataset ======= ")
    fruit_unique_df = combine_fruit(fruit_price_df,csvfolder)
    print(" Preprocess done! ")

    print(" ======== Combine tables ======= ")
    all_merge_df = combine_all_tables(fruit_unique_df, place_df, weather_df,csvfolder)
    print(" Get a database done! ")

    print(" ======== Start plot graph and Analyze ======= ")
    analyze_plotgraph(all_merge_df, weather_df)
    print(" All process are done! ")
