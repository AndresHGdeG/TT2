import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from TT2.items import Tt2Item
from bs4 import BeautifulSoup
import time
import datetime 

class TT2Spider(CrawlSpider):
    name = 'sopitas'
    item_count = 0
    dateToday = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")
    allowed_domain = ['https://www.sopitas.com/']
    #Aquí será el inicio del Scrapeo
    start_urls = ['https://www.sopitas.com/']

    rules = {
    	  # Será la xpath para poder acceder a cada noticia
          Rule(LinkExtractor(allow=(), restrict_xpaths=('//h3[@class="post-title m-0"]/a')),
                            callback= 'parse_item', follow= False)
    }

#-----------------------------------Funciones()---------------------------------------
    def dateNews(self, dat):
        def monthNameToMonthNumber(string):
            m = {
                "ene": 1,
                "feb": 2,
                "mar": 3,
                "abr": 4,
                "may": 5,
                "jun": 6,
                "jul": 7,
                "ago": 8,
                "sep": 9,
                "oct": 10,
                "nov": 11,
                "dic": 12
            }
            s = string.strip()[:3].lower()
            try:
                out = m[s]
                return out
            except:
                raise ValueError("")

        mylist = dat.replace(' ', ',').split(',')
        month = monthNameToMonthNumber(mylist[0])
        day = mylist[1]
        year = mylist[3]
        date = (str(day) + '/' + str(month) + '/' + str(year))
        return date


    def lstToStr(self, lst):
        return " ".join(str(x) for x in lst)

    def parse_item(self, response):

        news = response.xpath('//div[@class="post-content"]/child::p').getall()
        news = self.lstToStr(news)
        news = BeautifulSoup(news, features="lxml")
        news = news.get_text()
        dat = response.xpath('string(//p[@class="m-0"]/time)').extract()
        dat = self.lstToStr(dat)
        dat = self.dateNews(dat)

        if news and (len(news.split()) > 180):
            mi_item = Tt2Item()

            mi_item['url'] = response.url
            mi_item['titulo'] = response.xpath('//figcaption/h1/text()').extract()
            mi_item['autor'] = response.xpath('string(//a[@rel="author"])').extract()
            mi_item['fecha'] = dat
            mi_item['noticia'] = news 
            self.item_count += 1
            if self.item_count > 5:
                raise CloseSpider('item_exceeded')
            yield mi_item