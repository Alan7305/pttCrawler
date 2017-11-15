import re

"""test"""

def hello(_value):
    """print word"""
    print("hello " + _value + "!")

hello("world")

print(2)

str_1 = '17:10TPE2 小時 55 分鐘直飛 21:05KIX 19:05TAK2 小時 40 分鐘直飛 20:45TPE'
str_2 = re.search(r"\d{2}:\d{2}", str_1).group().replace(',','')
print(str_2)

data = []
data.append({'a':'a'})
print(data)