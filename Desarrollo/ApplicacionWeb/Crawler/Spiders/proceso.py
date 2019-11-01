import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from TT2.items import Tt2Item
import time
import datetime 

class TT2Spider(CrawlSpider):
    name = 'proceso'
    item_count = 0
    dateToday = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")
    allowed_domain = ['https://www.proceso.com.mx/']
    #Aquí será el inicio del Scrapeo
    start_urls = ['https://www.proceso.com.mx/']

    rules = {
    	  # Será la xpath para poder acceder a cada noticia
          Rule(LinkExtractor(allow=(), restrict_xpaths=('//h4/a')),
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
        month = monthNameToMonthNumber(mylist[1])
        day = mylist[0]
        year = mylist[3]
        date = (str(day) + '/' + str(month) + '/' + str(year))
        return date


    def lstToStr(self, lst):
        return " ".join(str(x) for x in lst)

    def parse_item(self, response):

        news = response.xpath('//div[@class="entry-content-inner padding-left"]/p/text()').extract()
        news = self.lstToStr(news)
        news = news.replace(u'\xa0', u' ')
        dat = response.xpath('normalize-space(//span[@class="posted-on"]/a/time/text())').extract()
        dat = self.lstToStr(dat)
        dat = self.dateNews(dat)

        if news and (len(news.split()) > 180):
            mi_item = Tt2Item()

            mi_item['url'] = response.url
            mi_item['titulo'] = response.xpath('normalize-space(//div[@class="postitle"]/h1/text())').extract()
            mi_item['autor'] = response.xpath('normalize-space(//span[@class="author-title"]/a/text())').extract()
            mi_item['fecha'] = dat
            mi_item['noticia'] = news 
            self.item_count += 1
            if self.item_count > 15:
                raise CloseSpider('item_exceeded')
            yield mi_item