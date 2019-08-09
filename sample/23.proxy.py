from urllib import request

# ret = request.urlopen('http://httpbin.org/ip')
# print(ret.read().decode('utf-8'))
# *read返回的是bytes需要decode

handler = request.ProxyHandler({'http':'116.62.198.43:8080'})
opener = request.build_opener(handler)
res = request.Request('http://httpbin.org/ip')
ret = opener.open(res)
print(ret.read().decode('utf-8')) 
