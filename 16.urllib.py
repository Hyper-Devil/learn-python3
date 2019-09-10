from urllib import request

# res = urllib.request.urlopen('http://www.yuqiaochuang.com/')
# ret = res.read().decode('utf-8')
# print(ret)

url = 'http://www.yuqiaochuang.com/'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

res = request.Request(url, headers=headers, method='POST')
ret = request.urlopen(res)
print(ret.read().decode('utf-8'))
