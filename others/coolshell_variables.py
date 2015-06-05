from urllib import urlopen

def crawlurl(url):
    f = urlopen(url)
    text = f.read()
    while(text.isdigit()):
        print text
        f = urlopen('http://fun.coolshell.cn/n/' + text)
        text = f.read()
    print text


if __name__ == '__main__':
    fun_url = 'http://fun.coolshell.cn/n/2014'
    crawlurl(fun_url)
