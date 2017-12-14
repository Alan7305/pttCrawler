import re
import json
import datetime
import twstock
from time import sleep

data = json.load(open('json_Airtickets/Stock_20171208.json', "r", encoding="utf-8"))


for item in data:
    #print(item['code'],item['date'],item['price'])

    print('INSERT INTO [dbo].[Stock_Data]'
           '([Code]'
           ',[Date]'
           ',[Price])'
     'VALUES'
           '(\''+item['code']+'\''
           ',\''+item['date']+'\''
           ',\''+str(item['price'])+'\')')

#stock = stock.fetch_from(2016, 1)

"""
data = []
for year in range(2015,2017):
    for month in range(1,13):
        print(year, month)

        stock = twstock.Stock('2890')
        stock = stock.fetch(year, month)  # 獲取 2015 年 7 月之股票資料

        sleep(10)

        for item in stock:
            print(item.date, item.close)

            data.append({
                'code' : '2890',
                'date' : item.date.strftime('%Y%m%d'),
                'price' : item.close
            })

with open('json_Airtickets/Stock_'+datetime.datetime.now().strftime('%Y%m%d')+'.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
"""
