# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         graph_weather
# Description:  draw weather data on one graph
# Author:       Kuan-Hui Lin
# Date:         2020/5/12
# -------------------------------------------------------------------------------
# 純粹分析天氣

import matplotlib.pyplot as plt
from directory import create_directory
import pandas as pd

def plot_weather(path, bins, weather, month):
  
    weather['Date'] = pd.to_datetime(weather['Date'])
    bins['bins'] = pd.to_datetime(bins['bins'])
    weather['AvgTemp'] = weather['AvgTemp'].astype(float)
    city_grouped = weather.groupby(weather['City'])

    colours=['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
    plt.figure(figsize = (12,8))

    i=0
    for name,subgroup in city_grouped:
        weather_monthly_df = subgroup.groupby(pd.cut(subgroup['Date'], bins['bins'],labels=bins.iloc[:-1,0])).agg({'AvgTemp': 'mean'})
        meantemp = weather_monthly_df['AvgTemp'].tolist()
        
        # plot Line Graph
        plt.plot(month, meantemp, c=colours[i], label=name,  alpha=0.5, linewidth = 2.0, linestyle = '-', marker='v') 
        plt.legend() 
        # give text on each point
        # for a,b in zip(month,weather_monthly_df['AvgTemp']):
        #     plt.text(a, b, '%.2f' %b, ha='right', va= 'baseline',fontsize=10)
        i+=1

    plt.title("Weather")
    plt.xlabel("Month")   
    plt.ylabel("Mean Temperature")  
    create_directory(path)
    plt.savefig(path + '/' + 'weather.png')
    plt.close()
