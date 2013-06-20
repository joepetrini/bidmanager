from backend.crawler import DocLinkCrawler

c = DocLinkCrawler(county="monmouth", url="http://littlesilver.org/ls/Bid%20Notifications/")
c.Crawl(c.soup.find('ul'))
