from backend.crawler import Crawler

c = Crawler(county="camden",url="http://haddonhts.com/request-for-proposalsqualificationsquotes/")

links = c.soup.find("div", { "class" : "entry-content" }).find_all('a')

for a in links:
	title = a.text
	url = a['href']
	c.AddItem(title=title, url=url)