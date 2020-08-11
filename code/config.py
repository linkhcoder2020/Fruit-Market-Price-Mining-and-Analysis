# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         config
# Description:  
# Author:       Kuan-Hui Lin
# Date:         2020/4/27
# -------------------------------------------------------------------------------
from __future__ import unicode_literals

# locAbr: location, repDate: date, startIndex: Page index (頁數索引), rowDisplayMax=Number of entries per page (每頁顯示條數)
orange_url = "https://www.marketnews.usda.gov/mnp/fv-report-top-filters?" \
             "type=termPrice&commAbr=ORG&locName={location}&commName=ORANGES&startIndex=1&" \
             "rowDisplayMax=100&portal=fvorganic%3D&navType=byComm&navClass=FRUITS&termNavClass=&" \
             "shipNavClass=&movNavClass=&stateID=&volume=&repType=termPriceDaily&locAbr={locAbr}&" \
             "environment=&varName=VALENCIA&organic=&repDate={date}&Go=Go"

limes_url = "https://www.marketnews.usda.gov/mnp/fv-report-top-filters?" \
            "type=termPrice&commAbr=LIM&locName={location}&commName=LIMES&startIndex=1&" \
            "rowDisplayMax=100&portal=fv&navType=byComm&navClass=FRUITS&termNavClass=&" \
            "shipNavClass=&movNavClass=&stateID=&volume=&repType=termPriceDaily&locAbr={locAbr}&" \
            "environment=&varName=SEEDLESS+TYPE&organic=&repDate={date}Go=Go"

guava_url = "https://www.marketnews.usda.gov/mnp/fv-report-top-filters?" \
            "type=termPrice&commAbr=GUAVA-V&locName={location}&commName=GUAVA&startIndex=1&" \
            "rowDisplayMax=100&portal=fv&navType=byComm&navClass=FRUITS&termNavClass=&shipNavClass=&" \
            "movNavClass=&stateID=&volume=&repType=termPriceDaily&locAbr={locAbr}&environment=&varName=" \
            "&organic=&repDate={date}&Go=Go"

strawberries_url = "https://www.marketnews.usda.gov/mnp/fv-report-top-filters?" \
                   "commAbr=STRBY&repDate={date}&varName=&locAbr={locAbr}&repType=termPriceDaily&" \
                   "termNavClass=&stateID=&navType=byComm&Go=Go&locName={location}&navClass=FRUITS&" \
                   "type=termPrice&shipNavClass=&volume=&startIndex=1&environment=&movNavClass=&" \
                   "commName=STRAWBERRIES&portal=fv&organic=&rowDisplayMax=100"

blueberries_url = "https://www.marketnews.usda.gov/mnp/fv-report-top-filters?" \
                  "commAbr=BLUBY&repDate={date}&locAbr={locAbr}&repType=termPriceDaily&" \
                  "termNavClass=&stateID=&navType=byComm&Go=Go&locName={location}&" \
                  "navClass=FRUITS&type=termPrice&shipNavClass=&volume=&" \
                  "startIndex=1&environment=&movNavClass=&commName=BLUEBERRIES&" \
                  "portal=fv&organic=&rowDisplayMax=100"

# 在拼接到 url 裡面需要把 LOS ANGELES 裡的空格變為 LOS+ANGELES,NEW YORK同樣 
# (In splicing into the url, you need to change the space in LOS ANGELES to LOS + ANGELES, the same as NEW YORK)
LOCATIONS = {
    'ORANGES': ['ATLANTA', 'BALTIMORE', 'BOSTON', 'CHICAGO', 'COLUMBIA', 'DETROIT',
                'LOS ANGELES', 'MIAMI', 'NEW YORK', 'PHILADELPHIA'],
    'LIMES': ['ATLANTA', 'BALTIMORE', 'BOSTON', 'CHICAGO', 'COLUMBIA', 'DETROIT',
              'LOS ANGELES', 'MIAMI', 'NEW YORK', 'PHILADELPHIA'],
    'GUAVA': ['ATLANTA', 'BALTIMORE', 'BOSTON', 'CHICAGO', 'COLUMBIA', 'DETROIT',
              'LOS ANGELES', 'MIAMI', 'NEW YORK', 'PHILADELPHIA'],
    'STRAWBERRIES': ['ATLANTA', 'BALTIMORE', 'BOSTON', 'CHICAGO', 'COLUMBIA', 'DETROIT',
                     'LOS ANGELES', 'MIAMI', 'NEW YORK', 'PHILADELPHIA'],
    'BLUEBERRIES': ['ATLANTA', 'BALTIMORE', 'BOSTON', 'CHICAGO', 'COLUMBIA', 'DETROIT',
                    'LOS ANGELES', 'MIAMI', 'NEW YORK', 'PHILADELPHIA'],
}
LOCATIONS_MAP_KEYS = {
    'ATLANTA': "AJ",
    'BALTIMORE': "BP",
    'BOSTON': "BH",
    'CHICAGO': "HX",
    'COLUMBIA': "CA",
    'DETROIT': "DU",
    'LOS ANGELES': "HC",
    'MIAMI': "MH",
    'NEW YORK': "NX",
    'PHILADELPHIA': "NA",
}
#水果名稱對應的 url (Url corresponding to fruit name)
KIND_MAP_URL = {
    "ORANGES": orange_url,
    "LIMES": limes_url,
    "GUAVA": guava_url,
    "STRAWBERRIES": strawberries_url,
    "BLUEBERRIES": blueberries_url,
}

# 開始日期(start date)，2019，1，1號會查找失败(2019, 1, 1 will fail)。 
START_DATE = (2019, 1, 2)
# 结束日期(end date) 2019，12，31
END_DATE = (2019, 12, 31)
# csv文件頭 (csv header)
HEADER = ["Commodity_Name", "City", "Date", "Low_Price", "High_Price", "Origin", 'Item_Size']
