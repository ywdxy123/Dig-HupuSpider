import scrapy 

from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request
from ..items import HupuspiderItem
from scrapy.contrib.loader import ItemLoader
from selenium import webdriver

import time
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options)

class HupuSpider(scrapy.Spider):
	name='spider'
	start_urls=['https://bbs.hupu.com/bxj']
	allowe_domains=['bbs.hupu.com']
	_x_query={
	'jointime':'//div[@class="personal_right"]/div/span[last()-1]/text()',
	'staytime':'//div[@class="personal_right"]/div/span[last()-2]/text()',
	}
	

	def __init__(self):
        # use any browser you wish
        # 
		

		self.browser = webdriver.Chrome() #使用前请安装对应的webdriver

	def parse(self,response):
		urls= response.xpath("//ul[@class='for-list']/li/div[2]/a/@href").extract()
		for url in urls:
			yield Request(url=url,callback=self.parse)
		
	 	
		self.browser.get(response.url)
		time.sleep(5)
		hupu_Loader=ItemLoader(item=HupuspiderItem(),response=response)
		hupu_Loader.add_xpath('jointime',self._x_query['jointime'])
		hupu_Loader.add_xpath('staytime',self._x_query['staytime'])
		yield hupu_Loader.load_item()
		


	def __del__(self):		 
		self.browser.close()

	


