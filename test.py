import re
import json
import datetime
import AirticketsCrawler

# 取得機票報價
AC = AirticketsCrawler.Quote('2018-04-07', '2018-04-14', 2, 1, 'tpe', 'kix', 'tak', 'tpe')
# 匯出JSON
AC.export('json_Airtickets/Airtickets_'+datetime.datetime.now().strftime('%Y%m%d')+'.json')

print(AC.data)



def hello(_value):
    """print word"""
    print("hello " + _value + "!")

hello("world")

print(2)

str_1 = '17:10TPE2 小時 55 分鐘直飛 21:05KIX 19:05TAK2 小時 40 分鐘直飛 20:45TPE'
str_2 = re.search(r"\d{2}:\d{2}", str_1).group().replace(',','')
print(str_2)


data = {}
data['a']=[]
data['a'].append({'a':'a'})

with open('test.txt', 'w') as f:
  json.dump(data, f, ensure_ascii=False)