import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from TT2.items import Tt2Item
import time
import datetime 

class TT2Spider(CrawlSpider):
    name = 'jornada'
    item_count = 0
    dateToday = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")
    allowed_domain = ['https://www.jornada.com.mx/ultimas']
    #Aquí será el inicio del Scrapeo
    start_urls = ['https://www.jornada.com.mx/ultimas']

    rules = {
    	  # Será la xpath para poder acceder a cada noticia
          Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="col-sm-12"]/h1/a | //div[@class="ljn-principal-rel-item"]/a | //div[@class="col-7 col-md-12"]/h2/a | //div[@class="col-7 col-sm-6 col-md-6 col-lg-9"]/h2/a')),
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
        month = monthNameToMonthNumber(mylist[3])
        day = mylist[2]
        year = mylist[4]
        date = (str(day) + '/' + str(month) + '/' + str(year))
        return date


    def lstToStr(self, lst):
        return " ".join(str(x) for x in lst)

    def parse_item(self, response):

        news = response.xpath('normalize-space(//div[@id="content_nitf"])').extract()
        news = self.lstToStr(news)
        dat = response.xpath('normalize-space(//*[@id="portal-Columns"]/div/div/article/div/div[1]/div/span[1]/span[2])').extract()
        dat = self.lstToStr(dat)
        dat = self.dateNews(dat)

        if news and (len(news.split()) > 180):
            mi_item = Tt2Item()

            mi_item['url'] = response.url
            mi_item['titulo'] = response.xpath('//div[@class="col-sm-12"]/h1/text()').extract()
            mi_item['autor'] = response.xpath('normalize-space(//span[@itemprop="name"]/text())').extract()
            mi_item['fecha'] = response.xpath('//div[@class="fechap"]/text()').extract()
            mi_item['noticia'] = news 
            self.item_count += 1
            if self.item_count > 10:
                raise CloseSpider('item_exceeded')
            yield mi_item