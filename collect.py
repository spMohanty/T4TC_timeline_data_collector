import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen('http://timeline.web.cern.ch/timelines/Building-the-LHC').read()
soup = BeautifulSoup(page)

def innerHTML(element):
    return element.decode_contents(formatter="html")

for article in soup.findAll('article'):
	# print dir(article)
	print "="*10
	print article.findChildren("h2")[0].findChildren("a")[0].text #Heading
	print article.findChildren("span")[0].text #Date
	print article.findChildren("img") #Image tag
	print innerHTML(article.findChildren("div", {"class":"field-item"})[0])
