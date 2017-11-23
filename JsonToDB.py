import json
from pprint import pprint

json_object = json.load(open('json_Airtickets/Airtickets_20171121.json', "r", encoding="utf-8"))

for day in json_object:
    print(day)
    for arr_ticket in json_object[day]:
        print(arr_ticket['TicketFare'])
        print(arr_ticket['outbound']['airline'])
        print(arr_ticket['outbound']['depTime'])
        print(arr_ticket['outbound']['arrTime'])
        print(arr_ticket['outbound']['departure'])
        print(arr_ticket['outbound']['destination'])
        print(arr_ticket['inbound']['airline'])
        print(arr_ticket['inbound']['depTime'])
        print(arr_ticket['inbound']['arrTime'])
        print(arr_ticket['inbound']['departure'])
        print(arr_ticket['inbound']['destination'])
