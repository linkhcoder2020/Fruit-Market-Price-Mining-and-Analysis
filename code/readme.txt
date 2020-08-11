The function are related weather data:
weather_place_data.py:
get_weather_place_data()
weather_place_api.py:
grab_data_from_weather_api()  : return weather DataFrame
create_date(): return a date list which includes every day within the specified range of dates.

-------------------------------------
The function are related place data:
weather_place_data.py:
get_weather_place_data() 
weather_place_api.py:
grab_data_from_place_api() : return place DataFrame

--------------------------------------
The function related fruit price data:
config.py :Crawl url, fruit type, date setting, csv column name and other setting 
data.csv  :Store crawl result
date_util.py :Create some of date
fake_useragent.json :fake header
get_three_dataframe.py: entry file 
write_csv.py : write the data in csv format
The rest are test related documents and are not important.

--------------------------------------
[fruit price data]
Website: https://www.freshfruitportal.com/usda-prices/
Get the following related information of five kinds of fruit:
Commodity:
1.	ORANGES (Variety: choose VALENCIA)
2.	LIMES (Variety: choose SEEDLESS TYPE)
3.	GUAVA (Variety default: all)
4.	STRAWBERRIES (Variety default: all)
5.	BLUEBERRIES (Variety default: all)

Parameters：
Report Type：TERMINAL MARKET
Date: 2019/01/01~2019/12/31 (can be changed if the date is not work in the website)
Location: 
1.	Atlanta
2.	Baltimore
3.	Boston
4.	Chicago
5.	Columbia
6.	Detroit
7.	Los Angeles
8.	Miami
9.	New York
10.	Philadelphia

Attributes：
1.	Commodity Name (web page: Commodity)
2.	City Name (web page: location )
3.	Date 
4.	Low Price
5.	High Price
6.	Origin
7.	Item Size

