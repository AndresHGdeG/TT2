import scrapy

class Tt2Item(scrapy.Item):
	
	url = scrapy.Field()
	titulo = scrapy.Field()
	autor = scrapy.Field()
	fecha = scrapy.Field()
	descripcion = scrapy.Field()
	noticia = scrapy.Field()
	pass