import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from Economia.items import EconomiaItem
import time
import datetime 

class aztecaDeportesSpider(CrawlSpider):
    name = 'economiaAzteca'
    item_count = 0
    dateToday = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")
    allowed_domain = ['https://www.tvazteca.com/aztecanoticias/finanzas/']
    start_urls = ['https://www.tvazteca.com/aztecanoticias/finanzas']

    rules = {
		  Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="Promo-title"]/a ')),
            callback= 'parse_item', follow= False)
    }

    def parse_item(self, response):
        mi_item = EconomiaItem()

        mi_item['url'] = response.url
        mi_item['seccion'] = response.xpath('//div[@class="az_layout whitebg"]/div[@class="az_layout-wrapper"]/h2/text() | //h2[@class="az_module-title"]/text()').extract()
        mi_item['titulo'] = response.xpath('normalize-space(//div[@class="az_module_note az_module_note-titlewrapper az_layut-col_full"]/h3/text() | //h1/text())').extract()
        mi_item['autor'] = response.xpath('//div[@class="CreativeWorkPage-authorName"]/text()').extract()
        mi_item['fecha'] = response.xpath('//div[@class="CreativeWorkPage-datePublished"]/text()').extract()
        mi_item['descripcion'] = response.xpath('//div[@class="CreativeWorkPage-subHeadline"]/text()').extract()
        mi_item['noticia'] = response.xpath('normalize-space(//div[@class="RichTextArticleBody-body"] | //div[@class="RichTextArticleBody-body"]/p/text())').extract()
        self.item_count += 1
        if self.item_count >35:
            raise CloseSpider('item_exceeded')
        yield mi_item