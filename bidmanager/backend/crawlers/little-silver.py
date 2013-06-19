from backend.crawler import Crawler

c = Crawler(county="monmouth", url="http://littlesilver.org/ls/Bid%20Notifications/")

bidlist = c.tree.xpath('//ul')[0]
for li in bidlist.xpath('li'):
	title = li.xpath('a/nobr')[0].text[:1000].replace('(pdf)','')
	url = li.xpath('a')[0].get('href')
	c.AddItem(title=title, url=url)
