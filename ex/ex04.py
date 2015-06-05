import urllib2
response = urllib2.urlopen('http://sports.sohu.com/20141202/n406567706.shtml')
html = response.read()
print html
