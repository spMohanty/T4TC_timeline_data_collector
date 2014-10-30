import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import json

items = []

for pageNum in range(100):
	page = urllib2.urlopen('http://timeline.web.cern.ch/timelines/Building-the-LHC?page='+str(pageNum)).read()
	soup = BeautifulSoup(page)

	def innerHTML(element):
	    return element.decode_contents(formatter="html")
	count = 0
	for article in soup.findAll('article'):
		count += 1
		# print dir(article)
		d = {}
		d['headline'] = article.findChildren("h2")[0].findChildren("a")[0].decode_contents(formatter="html")
		d['icon'] = 'https://upload.wikimedia.org/wikipedia/commons/c/cc/Ambox_green_tick.png'
		d['description'] = innerHTML(article.findChildren("div", {"class":"field-item"})[0])
		d['date'] = article.findChildren("span")[0].text #Date

		date_object = datetime.strptime(article.findChildren("span")[0].text, '%d %B %Y')
		d['date'] = str(date_object.year)+","+str(date_object.month)+","+str(date_object.day)
		images=article.findChildren("img") #Image tag
		if len(images)>0:
			d['media'] = images[0]['src']
			d['icon'] = images[0]['src']
		items.append(d)
	if count == 0:
		break

print json.dumps(items)