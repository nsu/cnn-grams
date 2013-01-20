import BeautifulSoup
import sys
import urllib
import re
import string


urlFile = open(sys.argv[1])
for url in urlFile:
    url = url.strip()
    print url
    page = urllib.urlopen(url)
    
    
    page = page.read()
    soup = BeautifulSoup.BeautifulSoup(page)
    page = soup.findAll("p", {"class": "cnnBodyText"})
    
    if not page:
        continue
    
    date = page[0].text
    date = date.split(' ')[1:6]
    date = " ".join(date)
    
    page = page[2]
    
    
    for br in page.findAll("br"):
        br.extract()
    page = page.contents
    
    page = "\n".join([re.sub(r"(^[ \t]+[A-Z][A-Z]*.*\:)|[%s]" % string.punctuation, r'', line) for line in page if type(line) == BeautifulSoup.NavigableString])
    page = re.sub(r"( +)", " ", page)

    fileOut = open("/Users/alex/Code/transcripts/%s.txt" % date, 'w')
    fileOut.write(page)
    fileOut.close()