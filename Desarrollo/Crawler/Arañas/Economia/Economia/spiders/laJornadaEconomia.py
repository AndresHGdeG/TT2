import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from Economia.items import EconomiaItem
import time
import datetime 

class laJornadaDeportesSpider(CrawlSpider):
    name = 'laJornadaEconomia'
    item_count = 0
    dateToday = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")
    allowed_domain = ['https://www.jornada.com.mx/ultimas/economia/']

    start_urls = ['https://www.jornada.com.mx/ultimas/economia/']

    rules = {
		Rule(LinkExtractor(allow=(), restrict_xpaths=('//h1[@class="elecciones-titulo ljn-title-listado"]/a | //h2[@class="ljn-title-listado"]/a')),
                            callback= 'parse_item', follow= False)
    }
    
    def parse_item(self, response):
        mi_item = EconomiaItem()
        
        mi_item['url'] = response.url
        mi_item['seccion'] = response.xpath('//*[@id="2-n"]/a/text()').extract()
        mi_item['titulo'] = response.xpath('//div[@class="col-sm-12"]/h1/text()').extract()
        mi_item['autor'] = response.xpath('normalize-space(//span[@itemprop="name"]/text())').extract()
        mi_item['fecha'] = response.xpath('normalize-space(//*[@id="portal-Columns"]/div/div/article/div/div[1]/div/span[1]/span[2])').extract()
        mi_item['noticia'] = response.xpath('normalize-space(//div[@id="content_nitf"])').extract()
        self.item_count += 1
        if self.item_count >50:
            raise CloseSpider('item_exceeded')
        yield mi_item