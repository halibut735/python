# coding=utf-8
import sys
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re
import time
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    href = 'http://www.gucas.ac.cn/site/157?c=103&pn='
    for i in range(1,35):
        tmp_href = href + str(i)
        f = urllib.urlopen(tmp_href)
        text = f.read()
        soup = BeautifulSoup(text)
        for item in soup.find_all('a', attrs = {'target': "_blank"}):
            print item

if __name__ == '__main__':
    main()
