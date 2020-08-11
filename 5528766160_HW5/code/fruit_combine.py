# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         fruit_combine
# Description:  Use (Commodity_Name, City, Date) as a key and 
#               go through each data and combine them if they have the same key and replace price with mean price
# 將重複的資料合併讓（商品,城市,日期) 唯一，將價錢取最低價格到最高價格的平均
# Author:       Kuan-Hui Lin
# Date:         2020/5/12
# -------------------------------------------------------------------------------

from collections import defaultdict
import pandas as pd
# from create_datelist import create_date
# import numpy as np
# import time

# trans %m/%d/%Y to %Y-%m-%d for being the arguments in create_date()
# def transdate(date):
#     timeArray = time.strptime(date, "%m/%d/%Y")
#     newdate = time.strftime("%Y-%m-%d", timeArray)
#     return newdate

def combine_fruit(fruit_df,path):
    sort_fruit_df = fruit_df.sort_values(by="Date", ascending=True, na_position='last')

    # find start date and end date on whole dataframe 
    # start_end_date = list()
    # top = np.array(sort_fruit_df['Date'].head(1)).tolist()
    # end = np.array(sort_fruit_df['Date'].tail(1)).tolist()
    # start_end_date.append(transdate(str(top[0])))
    # start_end_date.append(transdate(str(end[0])))
    # datelist = create_date(start_end_date[0],start_end_date[1])   # create the date list from start date to end date

    dic = defaultdict(list)
    for i in range(len(sort_fruit_df)):
        # Use frist three columns to be the tuple key, and append the price if key is the same
        # {(Orange,Boston,01/02/2019):[23,34,45,34,44,55,88]} 
        if i == 0:
            key = (sort_fruit_df["Commodity_Name"][i],sort_fruit_df["City"][i],sort_fruit_df["Date"][i])
            dic[key].append(sort_fruit_df["Low_Price"][i])
            dic[key].append(sort_fruit_df["High_Price"][i])

        key_new = (sort_fruit_df["Commodity_Name"][i],sort_fruit_df["City"][i],sort_fruit_df["Date"][i])
        if key == key_new:
            dic[key].append(sort_fruit_df["Low_Price"][i])
            dic[key].append(sort_fruit_df["High_Price"][i])
        else:
            dic[key_new].append(sort_fruit_df["Low_Price"][i])
            dic[key_new].append(sort_fruit_df["High_Price"][i])
    # print(dic)

    new_dic = dict()
    for key,value in dic.items():
        # create a new dictionary with average price
        # like {(Orange,Boston,01/02/2019):33.5} 

        if len(value) == 0:
            print("There is no value in the dictionary.")
            break

        # if there is the only one value, it will add itself twice and average it also itself 
        mean = (max(value)+min(value))/2     #只有一個值也可以處理，自己加自己兩次，取平均還是自己
        new_dic[key] = mean
    # print(new_dic)

    # Trans {(Orange,Boston,01/02/2019):33.5} to the DataFrame 
    fruit_unique_df = pd.DataFrame(list(new_dic), columns=['Commodity', 'City', 'Date']).assign(Mean_Price=new_dic.values()).sort_values(by='Date',ignore_index=True)
    fruit_unique_df.to_csv(path+'/'+'fruit_unique.csv', index=False)
    print(fruit_unique_df)
    return fruit_unique_df


