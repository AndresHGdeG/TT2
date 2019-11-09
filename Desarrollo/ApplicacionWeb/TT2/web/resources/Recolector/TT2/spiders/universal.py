import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from TT2.items import Tt2Item
import time
import datetime 

class TT2Spider(CrawlSpider):
    name = 'universal'
    item_count = 0
    dateToday = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")
    allowed_domain = ['https://www.eluniversal.com.mx/']
    #Aquí será el inicio del Scrapeo
    start_urls = ['https://www.eluniversal.com.mx/']

    rules = {
    	  # Será la xpath para poder acceder a cada noticia
          Rule(LinkExtractor(allow=(), restrict_xpaths=('//h1[@class="field-content"]/a | //div[@class="field-content"]/div/div/div/h4/a | //div[@class="views-field views-field-title"]/h3/a | //h2[@class="field-content"]/a | //div[@class="view-content"]/div/div/h2')),
            callback= 'parse_item', follow= False)
    }

#-----------------------------------Funciones()---------------------------------------
    def lstToStr(self, lst):
        return " ".join(str(x) for x in lst)

    def parse_item(self, response):

        news = response.xpath('normalize-space(//div[@class="field field-name-body field-type-text-with-summary field-label-hidden"])').getall()
        news = self.lstToStr(news)
        news = news.replace(u'\xa0', u' ')

        if news and (len(news.split()) > 180):
            mi_item = Tt2Item()

            mi_item['url'] = response.url
            mi_item['titulo'] = response.xpath('//div[@class="pane-content"]/h1/text()').extract()
            mi_item['autor'] = response.xpath('//div[@class="field-item even"]/text()').extract()
            mi_item['fecha'] = response.xpath('//div[@class="fechap"]/text()').extract()
            mi_item['descripcion'] = response.xpath('normalize-space(//div[@class="field field-name-field-resumen field-type-text-long field-label-hidden"]/text())').extract()
            mi_item['noticia'] = news 
            self.item_count += 1
            if self.item_count > 30:
                raise CloseSpider('item_exceeded')
            yield mi_item
