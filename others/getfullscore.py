#!/usr/bin/python
# coding=utf-8
#国科大院史知识竞赛满分程序
'''
powered by zhangbin
'''
import sys
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re
import time
from sendMail import *
from BeautifulSoup import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


hosturl = 'http://yszsjs2.cas.cn/answer.action'
posturl = hosturl
flag = 1



class ucas_freshmen(object):
    """class for retrieving the information of newest post """
    def __init__(self):
        self.txtZKZH = ''
        self.txtSFZH = ''

'''    def set_login_info(self, txtZKZH, txtSFZH):
        """ complete the base login information """
        self.txtZKZH = txtZKZH
        self.txtSFZH = txtSFZH
'''

    def login(self):
        ''' login ucas_freshmen '''

        """ set cookies """
        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                   'Referer': hosturl}

        # first HTTP request without form data
        try:
            reqreq = urllib2.Request(posturl, '', headers)
            f = urllib2.urlopen(reqreq, timeout = 60)
        except:
            raise MyException("There was an error." )
        soup = BeautifulSoup(f)
        # parse and retrieve two vital form values
        viewstate_arr =  soup.findAll('input',attrs = {"name" : "__VIEWSTATE", 'id': '__VIEWSTATE'})
        eventvalidation_arr = soup.findAll('input',attrs = {"name" : "__EVENTVALIDATION", 'id': '__EVENTVALIDATION'})
        viewstate = viewstate_arr[0].get('value')
        eventvalidation = eventvalidation_arr[0].get('value')


        postData = {    'txtSFZH' : self.txtSFZH,
                        'txtZKZH' : self.txtZKZH,
                        'OkButton' : '确定',
                        'ScriptManager1_HiddenField':'',
                        '__EVENTTARGET': '',
                        '__EVENTARGUMENT': '',
                        '__LASTFOCUS': '',
                        '__VIEWSTATE': viewstate,
                        '__EVENTVALIDATION': eventvalidation,
                        'rblType': '0'
        }
        postData = urllib.urlencode(postData)
        request = urllib2.Request(posturl, postData, headers)
        try:
            response = urllib2.urlopen(request, timeout = 60)
        except:
            raise MyException("There was an error.")
        text = response.read()
        #print text
        return text

def grep_info(text):
    global flag
    soup = BeautifulSoup(text)
    ret = ''

    grep_info = {'name': 'lblxm',
                 'stuID': 'lblxh',
                 'ID': 'LabZJHM',
                 'political affiliation': 'LabZZMM',
                 'birthday': 'LabBirthday',
                 'national': 'LabMZ',
                 'Corp.': 'lbldw',
                 'specialty': 'lblzy',
                 'campus': 'lblyq',
                 'buildingID': 'lbllh',
                 'roomNO.': 'lblfjh',
                 'telephone': 'lbldh',
                 'departments': 'lblyx',
                 'class': 'lblbj',
                 'headTeacher': 'lblbzr'}

    for key, value in grep_info.items():
        tmp = soup.find('span', attrs = {'id': value})
        if tmp.string:
            ret += '-' * 60 + '\n' + key + ': ' + tmp.string +'\n'

    ret += '-' * 60

    reArgu = r'roomNO|campus|class|headTeacher|buildingID|telephone'
    pattern = re.compile(reArgu)
    result = pattern.search(ret)

    print ret
    if result and flag <= 2:
        send_mail('827603830@qq.com', 'Hey, You can check ucas', (ret.decode('utf-8')).encode('gb2312'))
        flag += 1


def waiting(num):
    count = 0
    while count < num:
        count += 1
        print '.',
        time.sleep(1)
    print ''


def main():
    SFZH = ''
    ZKZH = ''
    user_login = ucas_freshmen()
    user_login.set_login_info(ZKZH, SFZH)
    count = 1
    while True:
        print 'start scrawling for the', count ,'\bth time.'
        count += 1
        try:
            info = user_login.login()
            grep_info(info)
        except :
            pass
        print '----------done and waiting for 60 seconds----------\n '
        waiting(60)


if __name__ == '__main__':
    main()
