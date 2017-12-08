import re
import json
import datetime
import twstock
"""
data = []


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

"""
stock = twstock.Stock('2890')
#stock = stock.fetch_from(2016, 1)
stock = stock.fetch(2015, 1)  # 獲取 2015 年 7 月之股票資料

data = []
for item in stock:
    print(item.date, item.close)

    data.append({
        'code' : '2890',
        'date' : item.date.strftime('%Y%m%d'),
        'price' : item.close
    })

with open('json_Airtickets/Stock_'+datetime.datetime.now().strftime('%Y%m%d')+'.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
