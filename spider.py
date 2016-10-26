from urllib.request import urlopen
from domain import *
from data_finder import *

class Spider:

	base_url = ''
	domain_name = ''
	queue = set()
	crawled = set()
	
	def __init__(self, base_url, domain_name):
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue.add(Spider.base_url)
		self.crawl('First Spider', Spider.base_url)
		
	@staticmethod
	def crawl(thread_name, url):
		if url not in Spider.crawled:
			print(thread_name + ' now crawling ' + url)
			print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
			Spider.add_links_to_queue(Spider.get_links(url))
			Spider.queue.remove(url)
			Spider.crawled.add(url)
			
	@staticmethod	
	def add_links_to_queue(links):
		for url in links:
			if (url in Spider.queue) or (url in Spider.crawled):
				continue
			if Spider.domain_name != get_domain_url(url):
				continue
			Spider.queue.add(url)
	
	@staticmethod
	def get_links(url):
		html_string = ''
		try:
			response = urlopen(url)
			if 'text/html' in response.getheader('Content-Type'):
				html_bytes = response.read();
				html_string = html_bytes.decode("utf-8")
			link_finder = DataFinder(Spider.base_url, url)
			link_finder.feed(html_string)
		except Exception as e:
			print(str(e))
			return set()
		return link_finder.page_links()
