from backend.crawler import DocLinkCrawler


c = DocLinkCrawler(county="camden", url="http://haddonhts.com/request-for-proposalsqualificationsquotes/")
c.Crawl(c.soup.find("div", {"class": "entry-context"}))
