import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from TT2.items import Tt2Item
import time
import datetime 

class TT2Spider(CrawlSpider):
    name = 'aristegui'
    item_count = 0
    dateToday = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")
    allowed_domain = ['https://aristeguinoticias.com/']
    #Aquí será el inicio del Scrapeo
    start_urls = ['https://aristeguinoticias.com/']

    rules = {
          Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="class_notas_int"] | //div[@class="class_ultimas_noticias"]/div[@class="parrafo_noticias"] | //span[@class="col"]/ul/li | //div[@class="title_nota"]/a | //table[@class="economia"]/tbody/tr/td/a')),
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

        news = response.xpath('//div[@class="class_text"]/p/child::node()/text()|//div[@class="class_text"]/p/text()').getall()
        news = self.lstToStr(news)
        dat = response.xpath('//div[@class="share_publicado"]/text()').extract()
        dat = self.lstToStr(dat)
        dat = self.dateNews(dat)

        if news and (len(news.split()) > 180):
            mi_item = Tt2Item()

            mi_item['url'] = response.url
            mi_item['titulo'] = response.xpath('//div[@class="class_subtitular"]/h1/text() | //div[@class="class_subtitular"]/text()').extract()
            mi_item['autor'] = response.xpath('//div[@class="share_nom"]/text()').extract()
            mi_item['fecha'] = dat #response.xpath('//div[@class="share_publicado"]/text()').extract()
            mi_item['descripcion'] = response.xpath('//div[@class="class_text2"]/text()').extract()
            mi_item['noticia'] = news #response.xpath('//div[@class="class_text"]/p/child::node()/text()|//div[@class="class_text"]/p/text()').getall()
            self.item_count += 1
            if self.item_count > 30:
                raise CloseSpider('item_exceeded')
            yield mi_item
