import threading
from queue import Queue
from spider import Spider
from domain import *

HOMEPAGE = 'http://viper-seo.com/'
DOMAIN_NAME = get_domain_url(HOMEPAGE)
queue = Queue()
NUMBER_OF_THREADS = 8
threads = set();
Spider(HOMEPAGE, DOMAIN_NAME, 'crawled.txt')

def create_workers():
	for i in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=run)
		t.daemon = True
		threads.add(t);
		t.start()
		
def run():
	while True:
		url = queue.get()
		Spider.crawl(threading.current_thread().name, url)
		queue.task_done()
	join_threads()
		
def give_spiders_jobs():
	for link in Spider.queue:
		queue.put(link)
	queue.join()
	crawl()
	
def crawl():
	queued_links = Spider.queue
	if len(queued_links) > 0:
		print(str(len(queued_links)) + ' links in the queue')
		give_spiders_jobs();

def join_threads():
	for t in threads:
		t.join()
		
create_workers()
crawl()
