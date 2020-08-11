# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         date_util
# Description:  
# Author:       Kuan-Hui Lin
# Date:         2020/4/27
# -------------------------------------------------------------------------------
from __future__ import unicode_literals
import datetime
from config import START_DATE, END_DATE


def get_date_list():
    """
    获取一段日期范围的列表
    :return:
    """
    date_list = []
    begin = datetime.date(*START_DATE)
    end = datetime.date(*END_DATE)
    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        str_day = day.strftime('%m/%d/%Y')
        date_list.append(str_day)
    return date_list


if __name__ == '__main__':
    list_d = get_date_list()
