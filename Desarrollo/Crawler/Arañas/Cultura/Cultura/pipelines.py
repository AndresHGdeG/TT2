# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter

class CulturaPipeline(object):
	@classmethod
	def __init__(self):
		self.file={}
		self.exporter={}

	def open_spider(self,spider):
		self.file=open(spider.nameCSV,'w+b')
		self.exporter=CsvItemExporter(self.file)
		self.exporter.fields_to_export = ['url', 'seccion','titulo', 'autor', 'fecha', 'descripcion', 'noticia']
		self.exporter.start_exporting()
	
	def close_spider(self, spider):
		self.exporter.finish_exporting()
		self.file.close() 
		
	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item

    