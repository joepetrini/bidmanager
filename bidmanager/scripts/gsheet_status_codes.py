import sys, re
import gspread
from bs4 import BeautifulSoup
import urllib2
from datetime import datetime

#print sys.argv[1]
if len(sys.argv) == 1:
    print "Must include password"
    sys.exit()

gc = gspread.login('joepetrini@gmail.com',sys.argv[1])
sh = gc.open_by_url('https://docs.google.com/spreadsheet/ccc?key=0AgUErk7rE6TLdFNaV1ZObUVsV2NESkx6OVd3bXlxcHc#gid=0')
worksheet = sh.get_worksheet(0)
cell = worksheet.find("Url")
urls = worksheet.col_values(cell.col)
statuscol = worksheet.find("HttpStatusCode").col
print "statuscol row %s col %s" % (worksheet.find("HttpStatusCode").row, worksheet.find("HttpStatusCode").col)



for i in range(226,len(urls)):
    try:
        print "checking %s - %s" % (i, urls[i])
        resp = urllib2.urlopen(urls[i])
    except urllib2.URLError, e:
        worksheet.update_cell(i+1, statuscol, e.code)
        print e.code
    else:
        print "200"
        worksheet.update_cell(i+1, statuscol, "200")

        # Update titles
        """
        m = re.search('http://([^/]+)', urls[i])
        resp = urllib2.urlopen(m.group(0))
        html = resp.read()
        m = re.search('<title>([^<]+)</title>', html, re.IGNORECASE)
        try:
            print m.group(1)        
            worksheet.update_cell(i+1, 3, m.group(1))
        except:
            print "Couldn't Update Title"
        """

ws = sh.get_worksheet(1)
c = ws.find("LastUrlCheck")
ws.update_cell(c.row + 1, c.col, datetime.now().date().isoformat())
