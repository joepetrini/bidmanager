from backend.crawler import Crawler


c = Crawler(county="morris", url="http://www.chathamtownship.org/bid_list.html")

table = c.tree.xpath('//table[@width="98%"]')[0]
for tr in table.xpath('tr')[1:]:
	#date = get_date(tr)
	url = c.base_url +  tr.xpath('td')[2][0][0].get('href')
	title = tr.xpath('td')[0][0].text[:1000]
	c.AddItem(title=title, url=url)
