import re
import json
import datetime
import AirticketsCrawler

# 取得機票報價
AC = AirticketsCrawler.Skyscanner('2018-04-07', '2018-04-14', 2, 1, 'tpe', 'kix', 'tak', 'tpe')
# 匯出JSON
AC.export('json_Airtickets/Airtickets_'+datetime.datetime.now().strftime('%Y%m%d')+'.json')
print('success, file path : ' + AC.path)