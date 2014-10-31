import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import json

timelines = ['Building-the-LHC', 'The-Large-Electron-Positron-Collider']
items = []



for timeline in timelines:
	for pageNum in range(100):
		page = urllib2.urlopen('http://timeline.web.cern.ch/timelines/'+timeline+'?page='+str(pageNum)).read()
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
			else:
				d['media'] = "https://c2.staticflickr.com/6/5087/5248565279_56c7a0d787_z.jpg"
			items.append(d)
		if count == 0:
			break

print json.dumps(items)