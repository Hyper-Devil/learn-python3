import requests

response = requests.get('http://www.httpbin.org/get')
print(response.url)
# 返回请求网站的 URL
print(response.status_code)
# 返回响应的状态码
print(response.encoding)
# 返回响应的编码方式
print(response.cookies)
# 返回响应的 Cookie 信息
print(response.headers)
# 返回响应头
print(response.content)
# 返回 bytes 类型的响应体
print(response.text)
print(response.content.decode('utf-8'))
# 返回 str 类型的响应体，相当于 response.content.decode('utf-8')
print(response.json())
# 返回 dict 类型的响应体，相当于 json.loads(response.text)
