#!/usr/bin/python
import sys
import urllib
import urllib2
import cookielib
import string
import re
import time
import commands
import random
import struct

from BeautifulSoup import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


class loginChinaUnicom(object):

    def __init__(self):
        self.url = 'http://202.106.46.37/login.do?callback=jQuery171021991612273268402_1432177819223&username=***********&password=****&passwordType=6&wlanuserip=&userOpenAddress=sd&checkbox=0&basname=&setUserOnline=&sap=&macAddr=78%253A31%253Ac1%253Ac3%253A50%253Aa6&bandMacAuth=1&isMacAuth=1&basPushUrl=http%253A%252F%252F202.106.46.37%252F&passwordkey=&_=1432177852160'
        self.refUrl = 'http://202.106.46.37/index.do'


    def macGenerate(self):
        macBinList = []
        macHexList = []
        for i in range(1, 7):
            i = random.randint(0x00, 0xff)
            macBinList.append(i)
        Fake_HW = struct.pack('BBBBBB', macBinList[0], macBinList[1], macBinList[2], macBinList[3], macBinList[4], macBinList[5])
        for j in macBinList:
            macHexList.append(hex(j))
        hardware = ':'.join(macHexList).replace("0x", '')
        return hardware


    def pingChinaUnicom(self):
        response = commands.getstatusoutput('ping -c 1 -t 1 202.106.46.37')
        pattern = re.compile(r', (\d{1,3}\.\d)%')
        match = pattern.search(str(response))
        return match.group(1)


    def hasIP(self):
        response = commands.getstatusoutput('ifconfig en0')
        pattern = re.compile(r'(\d\d\d\.\d{1,3})\.\d{1,3}\.\d{1,3}')
        match = pattern.search(str(response))
        if match == None:
            return 3
        elif match.group(1) == '111.200':
            return 1
        elif match.group(1) == '169.254':
            return 0
        else :
            return 3


    def login(self):
        '''set cookies'''
        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                   'Referer': self.refUrl}

        '''
        get method for login~~~
        '''
        req = urllib2.Request(self.url, '', headers)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        pattern = re.compile(r'.*"message":"(.*?)",')
        match = pattern.match(res)
        outputStr = match.group(1)
        print match.group(1)


    def doIt(self):
        count = 1
        while True:
            count += 1
            statusOfIP = self.hasIP()
            if statusOfIP == 3:
                time.sleep(1)
                continue
            elif statusOfIP == 0 or count %5 == 0:
                commands.getstatusoutput('networksetup -setairportpower en0 Off')
                commands.getstatusoutput('networksetup -setairportpower en0 On')
                time.sleep(2)
                continue
            elif statusOfIP == 1:
                if self.pingChinaUnicom() == '0.0':
                    break
        self.login()


def main():
    a = loginChinaUnicom()
    a.doIt()

if __name__ == '__main__':
    main()
