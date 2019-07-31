import re
import requests
import html
import time


# *思路：结构-大块-小块
def crawl_joke_list():
    url = "http://www.qiushibaike.com/text/page/"
    res = requests.get(url)
    # *获取每个段子div的正则↓
    pattern = re.compile(
        "<div class=\"article block untagged mb15.*?<div class=\"content\">\n<span>.*?</span>",
        re.S)
    # *<span>前需要\n
    # TODO把 <br/> 替换成\n，原因未知↓
    body = html.unescape(res.text).replace("<br/>", "\n")
    m = pattern.findall(body)
    # *抽取用户名的正则↓
    user_pattern = re.compile(
        "<div class=\"author clearfix\">.*?<h2>(.*?)</h2>", re.S)
    # *抽取段子的正则↓
    content_pattern = re.compile("<span>(.*?)</span>", re.S)
    for joke in m:
        user = user_pattern.findall(joke)
        output = []
        if len(user) > 0:
            output.append(user[0].replace("\n", ""))
            # *用replace去掉\n
        content = content_pattern.findall(joke)
        if len(content) > 0:
            output.append(content[0].replace("\n", ""))
        print("\t".join(output))
        # *join方法
    time.sleep(5)


if __name__ == '__main__':
    crawl_joke_list()
    # *目的是import时不执行
