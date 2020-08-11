# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         create_datelist
# Description:  
# Author:       Kuan-Hui Lin
# Date:         2020/4/27
# -------------------------------------------------------------------------------

import datetime

def create_date(start_date = None,end_date = None):

    if start_date is None:
        start_date = '2020-01-01'
    if end_date is None:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d') #
        
    start_date=datetime.datetime.strptime(start_date,'%Y-%m-%d')
    end_date=datetime.datetime.strptime(end_date,'%Y-%m-%d')
    date = list()
    date.append(start_date.strftime('%Y-%m-%d'))
    while start_date < end_date:
        start_date += datetime.timedelta(days=+1)
        date.append(start_date.strftime('%Y-%m-%d'))
        
    return date