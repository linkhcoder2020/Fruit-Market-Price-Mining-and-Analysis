# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         linear_reg
# Description:  Linear Regression to analyze the relationship between price and temperature
# Author:       Kuan-Hui Lin
# Date:         2020/5/12
# -------------------------------------------------------------------------------
# pip3 install -U scikit-learn scipy matplotlib
# pip3 install seaborn

from directory import create_directory
from matplotlib import pyplot as plt
from scipy import stats
import seaborn as sns

def linear_regression(path,_df):

    create_directory(path)
    
    for fruit in _df['Commodity'].unique():
    
        fix_fruit_df = _df[_df['Commodity'] == fruit]
        slope, intercept, r_value, p_value, std_err = stats.linregress(fix_fruit_df['AvgTemp'],fix_fruit_df['Mean_Price'])
        
        sns.set(rc={'figure.figsize':(8, 7)})
        ax = sns.regplot(x="AvgTemp", y="Mean_Price", data=fix_fruit_df, color='b', 
                        line_kws={'color':'red','label':"y={0:.5f}x+{1:.5f}".format(slope,intercept)})
        # plot legend
        ax.legend()
        size_label = fruit
        plt.title("Commodity = {}".format(size_label))
        plt.savefig(path +'/'+'linear_reg_result_'+ fruit +'.png')
        plt.close()
    
