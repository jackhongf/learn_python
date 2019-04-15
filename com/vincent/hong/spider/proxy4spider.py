import urllib.request
import time
import random

errorCount =0
def surfInternet(url,proxyDict):
    url = str(url)
    proxyList = proxyDict.get('http')
   # html = ''
    try:
        ip = random.choice(proxyList)
        start = time.time()
        http_surpport = urllib.request.ProxyHandler({'http':ip})
        opener=urllib.request.build_opener(http_surpport)
        opener.addheaders=[('User-agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')]
        urllib.request.install_opener(opener)
        response = urllib.request.urlopen(url)
        html = response.read()
        # html=html.decode('gbk')
        #print('爬虫页面结果'%html)
    except Exception as excp:
        end = time.time()
        print('爬虫时间：%f'%(end-start))
        print('使用代理爬虫出现异常,更换ip继续访问',excp)
        print('当前IP：%s'%ip)
        global errorCount
        errorCount= errorCount+1
        if errorCount > len(proxyList):
            pass
            return
        print('异常次数：%d'%errorCount)
        surfInternet(url, proxyDict)
    else:
        end = time.time()
        print('爬虫完成时间：%f'%(end-start))
        print('使用代理爬虫成功')
        return html













