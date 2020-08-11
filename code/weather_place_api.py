# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         weather_place_api
# Description:  
# Author:       Kuan-Hui Lin
# Date:         2020/4/27
# -------------------------------------------------------------------------------
from collections import defaultdict
from create_datelist import create_date
import urllib.request, urllib.parse, urllib.error
import pandas as pd
import requests
import time
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def grab_data_from_place_api(cityname, api_key, folder):
    '''
    Document:
    因為找附近的要付費，所以就只專注在農夫市場 
    Because it costs money to find nearby ones, so I only focus on the specific farmers market
    Place API(Google Map): https://developers.google.com/places/web-service/search?hl=zh-tw#nearby-search-and-text-search-responses
    https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=market%20LosAngeles&inputtype=textquery&fields=formatted_address,name,geometry&key=AIzaSyDMi_xHrr4kvuqVkEPPVPJAyG5lM7cXmyQ

    '''
    urlapi = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"

    place_dict = defaultdict(list)
    for n in range(len(cityname)):

        #set url parameters
        parms = dict()
        parms['input'] = 'farmersmarket '+ cityname[n]
        parms['inputtype'] = 'textquery'
        parms['fields'] = 'formatted_address,name,geometry'
        parms['key'] = api_key
        url = urlapi + urllib.parse.urlencode(parms, quote_via=urllib.parse.quote)  #.quote: encode "market%20Atlanta" (space-->%20)

        # request url and decode url
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()

        #Get json and print json 
        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':   #判斷是否成功與否(Whether it is successful or not)
            print('==== Failure To Retrieve ====')
            print(data)
            continue

        # print(json.dumps(js, indent=4))      #pretty_json

        # Get latitude, longitude, location and marketname
        place_dict['City'].append(cityname[n])
        place_dict['Marketname'].append(js['candidates'][0]['name'])
        place_dict['Latitude'].append(js['candidates'][0]['geometry']['location']['lat'])
        place_dict['Longitude'].append(js['candidates'][0]['geometry']['location']['lng'])
        place_dict['Address'].append(js['candidates'][0]['formatted_address'])

    place_df = pd.DataFrame(place_dict)
    place_df.to_csv(folder+'/'+'place.csv', index=False)
    return place_df

def grab_data_from_weather_api(cityname, api_key, folder):
    #     https://weatherstack.com/
    #     https://api.weatherstack.com/historical
    #     ? access_key = YOUR_ACCESS_KEY
    #     & query = New York
    #     & historical_date_start = 2015-01-21
    #     & historical_date_end = 2015-01-25
    # https://api.weatherstack.com/historical?access_key=ceb5e81c09ea372fad329d7c6924f1b8&query=New%20York&historical_date_start=2019-01-01&historical_date_end=2019-12-31

    urlapi = "http://api.weatherstack.com/historical?"
    datelist_start =["2019-01-01","2019-03-01","2019-04-30","2019-06-29","2019-08-28","2019-10-27","2019-12-26"]
    datelist_end = ["2019-02-28","2019-04-29","2019-06-28","2019-08-27","2019-10-26","2019-12-25","2019-12-31"]

    if len(datelist_start) == len(datelist_end):
        date_length = len(datelist_end)
    else:
        print('ERROR!!!   The length of two date lists is different!')
    
    # print(datelist)
    weather_dict = defaultdict(list)
    for n in range(len(cityname)): 
        for d in range(date_length):
            print('City:',cityname[n],'Start Date:',datelist_start[d],'End Date:',datelist_end[d] )

            parms = dict()
            parms['access_key'] = api_key
            parms['query'] = cityname[n]
            parms['historical_date_start'] = datelist_start[d]
            parms['historical_date_end'] = datelist_end[d]
            url = urlapi + urllib.parse.urlencode(parms, quote_via=urllib.parse.quote)
            print(url)

            # request url and decode url
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            uh = urllib.request.urlopen(req, context=ctx)
            data = uh.read().decode()

            #Get json and print json 
            try:
                js = json.loads(data)
            except:
                js = None

            print(json.dumps(js, indent=4))      #pretty_json

            datelist = create_date(datelist_start[d],datelist_end[d]) 
            
            # each query result only show city name, latitude, longitude, weather code once
            city = js['location']['name']
            lat = js['location']['lat']
            lon = js['location']['lon']
            weather_code = js['current']['weather_code']

            # the remaining temperature data is based on the date range
            for a in range(len(datelist)):
                weather_dict['City'].append(city)
                weather_dict['Latitude'].append(lat)
                weather_dict['Longitude'].append(lon)
                weather_dict['WeatherCode'].append(weather_code)
                daytime = js['historical'][datelist[a]]['date']

                # try:
                #     daytime = js['historical'][datelist[a]]['date']
                # except:
                #     with open('miss_date.txt', 'a') as ff:
                #         ff.write(datelist[a])
                #     print('Get the date ',datelist[a],'failed.')

                timeArray = time.strptime(daytime, "%Y-%m-%d")
                newtime = time.strftime("%m/%d/%Y", timeArray)
                weather_dict['Date'].append(newtime)
                weather_dict['LowTemp'].append(js['historical'][datelist[a]]['mintemp'])
                weather_dict['HighTemp'].append(js['historical'][datelist[a]]['maxtemp'])
                weather_dict['AvgTemp'].append(js['historical'][datelist[a]]['avgtemp'])
            print('60 days done！')
            
            if datelist_end[d] == "2019-12-31":
                print('Finish in 365 days!!')
    
    weather_df = pd.DataFrame(weather_dict)
    weather_df.to_csv(folder+'/'+'weather.csv', index=False)
    return weather_df



