# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         multi_linear_reg
# Description:  multiple linear regression
# Author:       Kuan-Hui Lin
# Date:         2020/5/12
# -------------------------------------------------------------------------------
# one-hot encoding: let location more meaningful 使 地區 編碼更有意義
#因為類別沒有順序之分，所以不可以轉換成有大小差別的數值，而要轉換成虛擬變數（Dummy variable），轉換的方法就叫做 one-hot encoding（獨熱編碼）。
import statsmodels.api as sm
import pickle 
import pandas as pd

def multi_linerreg(path, _df):

    cleanup_nums = {"Commodity":{"STRAWBERRIES": 1, "BLUEBERRIES": 2,'LIMES':3,'GUAVA':4,'ORANGES':5}}

    df_dum = pd.get_dummies(_df['City'])
    df2 = _df.join(df_dum)
    df2_final = df2.iloc[:,2:]        # df2_final not include original city and date
    df2_final.replace(cleanup_nums, inplace=True)
    y = df2_final['Mean_Price']
    X = df2_final[['AvgTemp', 'Commodity','ATLANTA','BALTIMORE','BOSTON','CHICAGO','DETROIT','LOS ANGELES','MIAMI','NEW YORK','PHILADELPHIA']]
    X_expan = sm.add_constant(X)      #increase dimension (i.e. add constant 1 in first column) y=kx+b
    regmodel = sm.OLS(y, X_expan)     #OLS : ordinary least square model
    results = regmodel.fit() 
    print(results.summary())
    results.save(path + '/' + "results.pickle")
    