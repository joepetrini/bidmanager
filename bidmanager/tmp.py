def crawlsite(tree):
    t = tree.xpath('//table[@width="98"]/tbody/tr')
    print t
    #t = tree.xpath("//table/tbody")
    for node in t:
        print node
    #print t[3]
    msg = "good"
    return ""
    #return {"bids": [{"a":"a"},{"b":"b"}],"msg":msg}