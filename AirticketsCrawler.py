""" Search for the airline ticket """
import re
import json
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup

class Skyscanner:
    """
    form Skyscanner
    """

    def __init__(self, startDate, endDate, adults, children, toGoDeparture, toGoDestination, returnDeparture, returnDestination):
        self.startDate = startDate
        self.endDate = endDate
        self.adults = str(adults)
        self.children = str(children)
        self.toGoDeparture = toGoDeparture
        self.toGoDestination = toGoDestination
        self.returnDeparture = returnDeparture
        self.returnDestination = returnDestination
        self.data = {}

        Skyscanner.search(self)

    def search(self):
        """
        Execute the search
        """

        options = webdriver.ChromeOptions()

        # set lang
        options.add_argument('lang=zh_TW.UTF-8')
        # set header
        #options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"')
        options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ASDAF-dsfsdfss-asdasd-ssalas"')

        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.skyscanner.com.tw/transport/d/'+self.toGoDeparture+'/'+self.startDate+'/'+self.toGoDestination+'/'+self.returnDeparture+'/'+self.endDate+'/'+self.returnDestination+'?adults='+self.adults+'&children='+self.children+'&adultsv2='+self.adults+'&childrenv2=5&infants=0&cabinclass=economy&ref=home#results')
        #driver.get('https://www.skyscanner.com.tw/transport/d/tpe/2018-04-07/kix/tak/2018-04-14/tpe?adults=2&children=1&adultsv2=2&childrenv2=5&infants=0&cabinclass=economy&ref=home#results')

        sleep(15)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        articles = soup.select('.day-list-item')

        date_now = datetime.datetime.now().strftime('%Y%m%d')
        data = {}
        data[date_now] = []

        i = 0
        for article in articles:
            if i < 3:
                # togo
                togo_airline = article.select('.AirlineLogo__big-logo-image-3V2-Z')[0]['alt']
                meta_togo = article.select('.leg-info')[0].getText()
                togo_stime = re.findall(r"\d{2}:\d{2}", meta_togo)[0]
                togo_etime = re.findall(r"\d{2}:\d{2}", meta_togo)[1]
                togo_departure = re.findall(r"[A-Z]{3}", meta_togo)[0]
                togo_destination = re.findall(r"[A-Z]{3}", meta_togo)[1]
                
                # return
                return_airline = article.select('.AirlineLogo__big-logo-image-3V2-Z')[1]['alt']
                meta_return = article.select('.leg-info')[1].getText()
                return_stime = re.findall(r"\d{2}:\d{2}", meta_return)[0]
                return_etime = re.findall(r"\d{2}:\d{2}", meta_return)[1]
                return_departure = re.findall(r"[A-Z]{3}", meta_return)[0]
                return_destination = re.findall(r"[A-Z]{3}", meta_return)[1]
                
                # fare
                ticket_fare = article.select('.price')[0].getText()
                ticket_fare = re.search(r"\d+,\d+", ticket_fare).group().replace(',','')
                
                data[date_now].append({
                    'outbound' : {
                        'airline' : togo_airline,
                        'depTime' : togo_stime,
                        'arrTime' : togo_etime,
                        'departure' : togo_departure,
                        'destination' : togo_destination
                    },
                    'inbound' : {
                        'airline' : return_airline,
                        'depTime' : return_stime,
                        'arrTime' : return_etime,
                        'departure' : return_departure,
                        'destination' : return_destination
                    },
                    'TicketFare' : ticket_fare
                })
                i += 1
            else:
                break
        
        driver.quit()
        self.data = data

    def export(self, path):
        """
        export json file to Hard Disk
        """

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False)
            self.path = path
