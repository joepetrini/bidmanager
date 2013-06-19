from backend.crawler import Crawler

c = Crawler(county="essex", url="http://glenridgenj.org/rfp.htm")

bids = c.soup.find_all('a')
for bid in bids:
	url = bid['href']
	if url.split('.')[-1] in c.doctypes:
		title = bid.text
		c.AddItem(title=title, url=url)
