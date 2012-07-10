import urllib
import urllib2

from bs4 import BeautifulSoup


url = "http://wikileaks.org/syria-files/releasedate/2012-07-09.html"
req = urllib2.Request(url)
response = urllib2.urlopen(req)
source = response.read()

soup = BeautifulSoup(source)
newsoup = soup.find("table","cable")

parsed = []

for link in newsoup.find_all('a'):
	n = link.get('href')
	parsed.append(n)

parsed = sorted(set(parsed))
for i in parsed:
	print i



