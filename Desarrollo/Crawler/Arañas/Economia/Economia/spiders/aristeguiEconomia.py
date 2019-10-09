import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from Economia.items import EconomiaItem
import time
import datetime 

class DeportesSpider(CrawlSpider):
    name = 'economiaAristegui'
    item_count = 0
    dateToday = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")
    allowed_domain = ['https://aristeguinoticias.com/']

    start_urls = ['https://aristeguinoticias.com/tag/economia/']

    rules = {

		  Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="sub_notaprincipal"]/a | //div[@class="container_nota"]/a | //tr/td/a')),
            callback= 'parse_item', follow= False)
    }

    def parse_item(self, response):
        mi_item = EconomiaItem()

        mi_item['url'] = response.url 
        mi_item['titulo'] = response.xpath('//div[@class="class_subtitular"]/h1/text() | //div[@class="class_subtitular"]/text()').extract()
        mi_item['autor'] = response.xpath('//div[@class="share_nom"]/text()').extract()
        mi_item['fecha'] = response.xpath('//div[@class="share_publicado"]/text()').extract()
        mi_item['descripcion'] = response.xpath('//div[@class="class_text2"]/text()').extract()
        mi_item['noticia'] = response.xpath('normalize-space(//div[@class="class_text"])').extract()
        self.item_count += 1
        if self.item_count >100:
            raise CloseSpider('item_exceeded')
        yield mi_item