import urllib.request

res = urllib.request.urlopen('http://www.yuqiaochuang.com/')
ret = res.read().decode('utf-8')
print(ret)
