# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         graph
# Description:  draw seperate graph (Avg price for specific fruit type/per month)
# Author:       Kuan-Hui Lin
# Date:         2020/5/12
# -------------------------------------------------------------------------------
# pip install matplotlib

from matplotlib.pyplot import plot, draw, show
from directory import create_directory
from graph_fruit import plot_fixed_fruit
from graph_weather import plot_weather
from linear_reg import linear_regression
from multi_linear_reg import multi_linerreg
import matplotlib.pyplot as plt
import pandas as pd

def analyze_plotgraph(database, weather_table):
    
    bins_df = pd.DataFrame({
                    'Month': ['1','2','3','4','5','6','7','8','9','10','11','12','13'],
                    'bins': ['12/31/2018','1/31/2019','2/28/2019','3/31/2019','4/30/2019','5/31/2019','6/30/2019',
                            '7/31/2019','8/31/2019','9/30/2019','10/31/2019','11/30/2019','12/31/2019'],
                    })

    # Create a new DataFrame(df) which includes some specific features to research 
    df = pd.DataFrame()
    df['City'] = database['City']
    df['Date'] = database['Date']
    df['AvgTemp'] = database['AvgTemp']
    df['Mean_Price'] = database['Mean_Price']
    df['Commodity'] = database['Commodity']

    # Change date type '01/02/2019' to '2019-01-02'
    df['Date'] = pd.to_datetime(df['Date'])
    bins_df['bins'] = pd.to_datetime(bins_df['bins'])
    df['Mean_Price'] = df['Mean_Price'].astype(float)

    # group City and Commodity 
    grouped_df = df.groupby(['City','Commodity'])

    # create a dictionary for storing graphs about price/per month
    path = "./avg_price_pic"
    create_directory(path)

    # plot the graph area
    whole_name = list()
    whole_avgprice = list()
    month_num = bins_df.iloc[:-1,0]

    # iterate each subgroup
    for name,subgroup in grouped_df:
        whole_name.append(name)
        # cut 'Date' by referring bins (Divide 'Date' heap by month)
        price_monthly_df = subgroup.groupby(pd.cut(subgroup['Date'], bins_df['bins'])).agg({'Mean_Price': "mean"})

        # if there is no price(NAN) in the month, use -1 to replace NAN for graphing 若沒有該月份的價錢資料，用-1代替
        price_monthly_df.fillna(-1,inplace=True)  

        avgprice_list = price_monthly_df['Mean_Price'].tolist()
        whole_avgprice.append(avgprice_list)

        # plot Line Graph
        plt.figure(figsize = (10,6))
        plt.plot(month_num, avgprice_list, c='blue', label='High',  alpha=0.5, linewidth = 2.0, linestyle = '-', marker='o') # 绘制最高气温的折线  
        title = "(" + str(name[0]) + " , " + str(name[1]) + ")"
        plt.title(title) 
        for a,b in zip(month_num,avgprice_list):
            plt.text(a, b, '%.2f' %b, ha='right', va= 'top',fontsize=11)
        plt.xlabel("Month")   
        plt.ylabel("Mean Price")  
        plt.savefig(path+'/'+title +'.png')
        plt.close()

    # plot_fixed_city("./fixed_city_pic", whole_name, month_num, whole_avgprice)
    plot_fixed_fruit("./fixed_fruit_pic", month_num, whole_avgprice)
    plot_weather("./weather_pic",bins_df, weather_table, month_num)
    linear_regression("./linear_reg_pic",df)
    multi_linerreg("./linear_reg_pic",df)
    print(" All process of drawing graph done! ")

