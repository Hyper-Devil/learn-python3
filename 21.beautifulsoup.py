import requests
import lxml
from bs4 import BeautifulSoup
import time
import re

url = "https://www.qiushibaike.com/text/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())
joke_list = soup.find_all(
    "div", class_=re.compile("article block untagged mb15 typs_hot.*?"))
    # *这里不用正则的话没法匹配，但是教程没有用
for author in joke_list:
    print(
        author.find("h2").string + "\n" +
        "".join(author.find("div", class_="content").stripped_strings))
        # *stripped_strings返回的是生成器
time.sleep(1)
'''
str = "-";
seq = ("a", "b", "c"); 
print str.join( seq );
>>a-b-c
'''
