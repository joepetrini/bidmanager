from backend.crawler import DocLinkCrawler


c = DocLinkCrawler(county="monmouth", url="http://belmar.com/content.php?npid=69&npid1=239&pid=239&menu_id=20")
c.Crawl()
