import BeautifulSoup
import urllib
import sys

year = "2012"
month = 2
#missed part of 16
day = 17

urllist = open(sys.argv[1], 'a')

# optimized for speed...
# not legibility
while month <= 9:
    month = "0"+str(month)
    while day <= 31:
        if day < 10:
            day = "0"+str(day)
        else:
            day = str(day)
        url = "http://transcripts.cnn.com/TRANSCRIPTS/%s.%s.%s.html" % (year, month, day)
        print url
        page = urllib.urlopen(url)
        page = page.read()
        page = BeautifulSoup.BeautifulSoup(page)
        links = [div.findAll('a') for div in page.findAll("div", {"class": "cnnSectBulletItems"})]
        links = ["http://transcripts.cnn.com/%s" % item.get("href") for sublist in links for item in sublist]
        urllist.write("\n".join(links))
        urllist.write("\n")
    
        day = int(day)+1
    month = int(month)+1
    day = 1