import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from Economia.items import EconomiaItem
import time
import datetime 

class elEconomistaSpider(CrawlSpider):
    name = 'economiaElEconomista'
    item_count = 0
    dateToday = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")
    allowed_domain = ['https://www.eleconomista.com.mx/economia/']
    start_urls = ['https://www.eleconomista.com.mx/seccion/economia/']

    rules = {
		  Rule(LinkExtractor(allow=(), restrict_xpaths=('//center/a'))),
          Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="entry-data"]/h3/a')),
            callback= 'parse_item', follow= False)
    }

    def parse_item(self, response):
        mi_item = EconomiaItem()

        mi_item['url'] = response.url
        mi_item['titulo'] = response.xpath('//div[@class="title"]/h1/text()').extract()
        mi_item['autor'] = response.xpath('normalize-space(//div[@class="author-data"]/text())').extract()
        mi_item['fecha'] = response.xpath('//span[@class="article-date"]/time/text()').extract()
        mi_item['descripcion'] = response.xpath('//div[@class="title"]/h3/p').extract()
        mi_item['noticia'] = response.xpath('//div[@class="entry-body"]/p').extract()
        self.item_count += 1
        if self.item_count >300:
            raise CloseSpider('item_exceeded')
        yield mi_item