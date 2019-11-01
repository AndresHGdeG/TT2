import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from TT2.items import Tt2Item
import time
import datetime 

class TT2Spider(CrawlSpider):
    name = 'economista'
    item_count = 0
    dateToday = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")
    allowed_domain = ['https://www.eleconomista.com.mx/']
    #Aquí será el inicio del Scrapeo
    start_urls = ['https://www.eleconomista.com.mx/']

    rules = {
    	  # Será la xpath para poder acceder a cada noticia
          Rule(LinkExtractor(allow=(), restrict_xpaths=('//h2[@itemprop="headline name"]/a | //article/a | //div[@class="entry-data"]/h3/a | //h2[@class="titulo"]/a')),
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
        month = monthNameToMonthNumber(mylist[2])
        day = mylist[0]
        year = mylist[4]
        date = (str(day) + '/' + str(month) + '/' + str(year))
        return date

    def lstToStr(self, lst):
        return " ".join(str(x) for x in lst)

    def parse_item(self, response):

        news = response.xpath('//div[@class="entry-body"]/p/text()').getall()
        news = self.lstToStr(news)
        dat = response.xpath('//span[@class="article-date"]/time/text()').extract()
        dat = self.lstToStr(dat)
        dat = self.dateNews(dat)

        if news and (len(news.split()) > 180):
            mi_item = Tt2Item()

            mi_item['url'] = response.url
            mi_item['titulo'] = response.xpath('//div[@class="title"]/h1/text()').extract()
            mi_item['autor'] = response.xpath('normalize-space(//div[@class="author-data"]/text())').extract()
            mi_item['fecha'] = dat 
            mi_item['descripcion'] = response.xpath('//div[@class="title"]/p/text()').extract()
            mi_item['noticia'] = news 
            self.item_count += 1
            if self.item_count > 10:
                raise CloseSpider('item_exceeded')
            yield mi_item