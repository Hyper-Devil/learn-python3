import re
import requests
import baiduaip
import time
# from bs4 import BeautifulSoup
# import lxml
# import html

start = time.time()
temp_ocr = baiduaip.get_text_from_image()
question = temp_ocr[0]
ans1 = temp_ocr[1]
ans2 = temp_ocr[2]
ans3 = temp_ocr[3]
# ans = []
# ans.append(ans1)
# ans.append(ans2)
# ans.append(ans3)

print(question)

url = "http://www.paopaoche.net/sj/120914.html"
res = requests.get(url)
ret = res.content.decode('gbk')
# body = html.unescape(res).replace("<br/>", "\n")
print(ret)


# with open('data.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
# print(c)

# result = re.match(r'\u98df\u53d1\u9b3c\u7684\u59d0\u59d0\u662f\u8c01', c)
# if result:
#     print(result.group())
# else:
#     print('No match!')

# print(c.find('\u98df\u53d1\u9b3c\u7684\u59d0\u59d0\u662f\u8c01'))

# for line in lines:
#     # if line.find('\u98df\u53d1\u9b3c\u7684\u59d0\u59d0\u662f\u8c01'):
#     if line.find('食发鬼的姐姐是谁?'):
#         print(line)
#         break
    
end = time.time()
print('程序用时：'+str(end-start)+'秒')
