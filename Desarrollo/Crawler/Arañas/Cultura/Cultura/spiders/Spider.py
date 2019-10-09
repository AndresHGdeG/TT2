import scrapy 
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from Cultura.items import CulturaItem
from scrapy.exceptions import CloseSpider
import datetime 

class spidr(CrawlSpider):
	name="ElEconomista"
	allow_domain=['www.eleconomista.com.mx']
	start_urls=['https://www.eleconomista.com.mx/tags/cultura/']
	dateToday = datetime.datetime.now().strftime("%d-%m-%y-%H:%M")
	nameCSV=name+'_'+dateToday+'.csv'
	noticia_contador=0
	num_noticias=10


	rules=(
		Rule(LinkExtractor(allow=(r'arteseideas')),callback='parse_item',follow=True),
		)


	def parse_item(self,response):
		self.logger.info("-------------Entre al link: %s----------",response.url)


		contenido=response.xpath('//div[@class="entry-body"]/p/text()|//div[@class="entry-body"]/h2/text()')[2].get()

		if contenido:

			myItem=CulturaItem()

			myItem['url'] = response.url
			myItem['titulo']=response.xpath('//div[@class="title"]/h1/text()').get()
			myItem['noticia']=response.xpath('//div[@class="entry-body"]/p/text()|//div[@class="entry-body"]/h2/text()').getall()
			myItem['autor'] = response.xpath('normalize-space(//div[@class="author-data"]/text())').getall()
			myItem['fecha'] = response.xpath('//span[@class="article-date"]/time/text()').get()
			myItem['descripcion'] = response.xpath('//div[@class="title"]/h3/p').getall()
						
			self.noticia_contador+=1
			if self.noticia_contador>self.num_noticias:
				raise CloseSpider("no_proxies_after_reset")
			yield myItem



