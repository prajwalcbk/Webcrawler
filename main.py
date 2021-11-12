from requests import *
from parsel import Selector
from urllib.parse import *
from bs4 import BeautifulSoup
import re
from threading import Thread

i=0
web_links=[]
lock=False
def Crawler(link):
	global web_links , lock
	try:
		if(link not in web_links):
			response=get(link)
			if(response.status_code!=200):
				return
			#print(response.content)
			print(link)
			web_links.append(link)
			#content=BeautifulSoup(response.text)
			select=Selector(response.text)
			links=select.xpath('//a/@href').getall()
			# 	print(content)
			links=list(set(links))
			#print(links)
			for web_pages in links:
				if(web_pages[0]=='#'):
					continue
				if 'javascript:' in web_pages or 'mailto' in web_pages:
		        		continue
				url_parse=urlparse(web_pages)
				#print(url_parse.netloc,end='')
				if(not url_parse.netloc):
					nextlink=urljoin(link,web_pages)
					Crawler(nextlink)
	except Exception as e:
		print(e)
#input_url=input()
Crawler('http://msrit.edu/department/cse.html')
