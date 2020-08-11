# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         weather_place_data
# Description:  
# Author:       Kuan-Hui Lin
# Date:         2020/4/27
# -------------------------------------------------------------------------------

from create_datelist import create_date
from weather_place_api import grab_data_from_place_api,grab_data_from_weather_api

def get_weather_place_data():
    city = ["Atlanta","Baltimore","Boston","Chicago","Columbia","Detroit","Los Angeles","MiaMi","New York","Philadelphia"]
    place_key = "AIzaSyDMi_xHrr4kvuqVkEPPVPJAyG5lM7cXmyQ"
    weather_key = "ceb5e81c09ea372fad329d7c6924f1b8"

    print('Grab data from place API')
    place_df = grab_data_from_place_api(city,place_key)
    print('========= Place Grab End =========')
    print('Grab data from weather API')
    weather_df = grab_data_from_weather_api(city,weather_key)
    print('========= Weather Grab End =========')

    return place_df, weather_df