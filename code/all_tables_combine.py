# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         combine all tables
# Description:  
# Author:       Kuan-Hui Lin
# Date:         2020/5/12
# -------------------------------------------------------------------------------

import pandas as pd

def combine_all_tables(fruit, place, weather,path):
    place['City'] = place['City'].str.upper()
    weather['City'] = weather['City'].str.upper()

    weather_fruit_merge_df = pd.merge(weather, fruit, on=['City', 'Date'])  # 因為天氣是 Date 唯一 (weather: date unique, city and date are both in left and right DataFrame)
    all_merge_df = pd.merge(weather_fruit_merge_df,place,left_on='City',right_on='City')   #因為 place，city 是唯一 (place: city unique)
    all_merge_df.to_csv(path + '/' + 'all_merge_result.csv', index=False)
    return all_merge_df


