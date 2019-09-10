# import re
import requests
import baiduaip
import time
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
URL = 'http://www.baidu.com/s?wd='


def ocr():
    ret = baiduaip.get_text_from_image()
    question = ret[0]
    if not question.endswith("?"):
        # ?出现报错'str' object has no attribute 'endsWith'
        # !endswith, w not W
        # question = ret[0]
        # else:
        question = ret[0] + ret[1]
    print('将查询问题：{}'.format(question))
    return question


def get_ppc_url(question, url):
    res = requests.get(url + str(question + '跑跑车'), headers=HEADERS)
    soup = BeautifulSoup(res.text, 'lxml')
    div_first_result = soup.find('div', class_='result c-container ', id='1')
    # ?出现报错result、find_all和find什么的
    # !是因为没有查到标签
    # !'result c-container ' followed a f**king space!
    a = div_first_result.find('a')
    href_url = a['href']
    return href_url


def prase_detail_page(url):
    print('正在分析网页：' + url)
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.content.decode('gbk'), 'lxml')
    # *ppc网站是gk2312编码，不能用text
    span_style1 = soup.find_all('span', style='color: rgb(23, 54, 93);')[0]
    strong_style1 = span_style1.find('strong')
    ans = str(strong_style1.string)
    if ans == "逢魔密信答案大全：":
        div_xq_main = soup.find('div', class_='xq-main')
        span_style2 = div_xq_main.find('span',
                                       style='color: rgb(95, 73, 122);')
        strong_style2 = span_style2.find('strong')
        ans = strong_style2.string
    # *直接取出strong标签中的值
    return ans


def main():
    start = time.time()
    ans = prase_detail_page(get_ppc_url(question=ocr(), url=URL))
    print('答案是：{}'.format(ans))
    end = time.time()
    print('程序用时：' + str(end - start) + '秒')


if __name__ == "__main__":
    main()
