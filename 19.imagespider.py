import requests
import re


def crawl_image(image_url, image_local_path):
    r = requests.get('http:' + image_url, stream=True)
    # *二进制流
    with open(image_local_path, "wb") as f:
        f.write(r.content)


def crwal(page):
    url = "http://www.qiushibaike.com/imgrank/page/" + str(page)
    res = requests.get(url)
    content_list = re.findall("<div class=\"thumb\">(.*?)</div>",
                              res.content.decode("utf-8"), re.S)
    for content in content_list:
        image_list = re.findall("<img src=\"(.*?)\"", content)
        for image_url in image_list:
            crawl_image(image_url,
                        "./images/" + image_url.strip().split('/')[-1])
                        # *strip()移除首尾指定字符，split('/')分割取最后一元素


if __name__ == '__main__':
    crwal(1)
