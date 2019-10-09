import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from Economia.items import EconomiaItem
import time
import datetime 

class procesoSpider(CrawlSpider):
    name = 'economiaPrensa'
    item_count = 0
    dateToday = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")
    allowed_domain = ['https://www.la-prensa.com.mx/finanzas/']
    start_urls = ['https://www.la-prensa.com.mx/buscar/?q=finanzas']

    rules = {

          Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="tab-story"]/div[3]/ul/li[4]/span | //*[@id="tab-story"]/div[3]/ul/li[5]/span | //*[@id="tab-story"]/div[3]/ul/li[6]/span | //*[@id="tab-story"]/div[3]/ul/li[7]/span | //*[@id="tab-story"]/div[3]/ul/li[8]/span'))),
          Rule(LinkExtractor(allow=(), restrict_xpaths=('//h4/a')),
            callback= 'parse_item', follow= False)
    }

    def parse_item(self, response):
        mi_item = EconomiaItem()

        mi_item['url'] = response.url 
        mi_item['titulo'] = response.xpath('normalize-space(//section[@class="col-sm-8"]/h1/text() | //h1[@class="title"]/text())').extract()
        mi_item['autor'] = response.xpath('normalize-space(//div[@class="affix-start "]/p[@class="byline"]/text())').extract()
        mi_item['fecha'] = response.xpath('normalize-space(//p[@class="published-date"]/text())').extract()
        mi_item['descripcion'] = response.xpath('normalize-space(//h3[@class="subtitle"]/text())').extract()
        mi_item['noticia'] = response.xpath('//h3[@class="subtitle"]/text()//div[@class="content-body clearfix"]/div[@id="content-body-225-3940388"]/p/text() | //section[@class="content-continued-body clearfix"]/div[@id="content-body-226-3940388"]/p/text() | //section[@class=" col-sm-8"]/div/div/p/text() | //section[@class="content-continued-body clearfix"]/div/p/text()').extract()
        self.item_count += 1
        if self.item_count >50:
            raise CloseSpider('item_exceeded')
        yield mi_item