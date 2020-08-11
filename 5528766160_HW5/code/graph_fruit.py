# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         graph_fruit
# Description:  draw same fruit with different cities (Draw line graph of 10 cities on the same fruit picture)
# Author:       Kuan-Hui Lin
# Date:         2020/5/12
# -------------------------------------------------------------------------------

from collections import defaultdict
from directory import create_directory
import matplotlib.pyplot as plt

def plot_fixed_fruit(path, month, price):
    
    city = ['ATLANTA','BALTIMORE','BOSTON','CHICAGO','COLUMBIA',
            'DETROIT','LOS ANGELES','MIAMI','NEW YORK','PHILADELPHIA']

    colours=['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 
            'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

    create_directory(path)

    # fruit fix
    fruit_dic = defaultdict(list)
    for j in range(len(price)):
        if (j+1)%5 == 1:
            fruit_dic['BLUEBERRIES'].append(price[j])
        elif (j+1)%5 == 2:
            fruit_dic['GUAVA'].append(price[j])
        elif (j+1)%5 == 3:
            fruit_dic['LIMES'].append(price[j])
        elif (j+1)%5 == 4:
            fruit_dic['ORANGES'].append(price[j])
        elif (j+1)%5 == 0:
            fruit_dic['STRAWBERRIES'].append(price[j])

    # plot Line Graph
    leg_list = list()
    plt.figure(figsize = (11,10))
    for key in fruit_dic.keys():    #key is fruit name
        leg_list = list()
        for f in range(len(fruit_dic[key])):
            leg_list.append((str(key),city[f]))
            plt.plot(month, fruit_dic[key][f], c=colours[f%10], label='High',  alpha=0.5, linewidth = 2.0, linestyle = '-', marker='o')  
            if (f+1)%10 == 0:
                plt.legend(leg_list, loc='best')
                plt.title("Fruit Fixed and City Changed") 
                plt.xlabel("Month")   
                plt.ylabel("Mean Price for each type")  
                plt.savefig(path +'/'+ key +'.png')
                plt.close()
                plt.figure(figsize = (11,10))
