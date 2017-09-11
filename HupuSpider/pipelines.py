# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
class HupuspiderPipeline(object):
	def __init__(self):
		self.file=codecs.open('hupu.json','w')
  
	def process_item(self, item, spider):
		line=json.dumps(dict(item))+'\n'
		self.file.write(line)	
		return item	