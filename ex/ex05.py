import urllib
import sys
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re
import time
from BeautifulSoup import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    url = 'http://sports.163.com/14/1005/21/A7QSQNIJ00052UUC.html#p=A7Q50OAL5GUM0005'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Referer': 'sports.163.com'}
    reqreq = urllib2.Request(url, '', headers)
    f = urllib2.urlopen(reqreq, timeout = 60)
    print f.read()
