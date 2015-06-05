import urllib
import os


pwd = '/Users/bingoboy/Downloads/'
files =  os.listdir(pwd)
for each in files:
    if '%' in each:
        decodeName = urllib.unquote(each)
        os.rename(pwd + each, pwd + decodeName)
