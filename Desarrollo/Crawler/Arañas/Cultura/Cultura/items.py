# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CulturaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    seccion = scrapy.Field()
    titulo = scrapy.Field()
    autor = scrapy.Field()
    fecha = scrapy.Field()
    descripcion = scrapy.Field()
    noticia = scrapy.Field()
    pass
