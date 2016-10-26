from html.parser import HTMLParser
from urllib import parse
from domain import *

class DataFinder(HTMLParser):
	
	def __init__(self, base_url, page_url):
		super().__init__();
		self.base_url = base_url;
		self.page_url = page_url;
		self.crawled_links = set();
		
	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for (attribute, value) in attrs:
				if attribute == 'href':
					url = parse.urljoin(self.base_url, value)
					self.crawled_links.add(url);
					
	def page_links(self):
		return self.crawled_links;
		
	def error(self, message):
		pass
		