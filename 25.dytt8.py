from lxml import etree
import requests

BASE_DOMAIN = 'http://dytt8.net'
HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}


def get_detail_urls(url):
    res = requests.get(url, headers=HEADERS)
    ret = res.content.decode('gbk')
    html = etree.HTML(ret)
    detail_urls = html.xpath("//table[@class = 'tbspan']//a/@href")
    detail_urls = map(lambda url: BASE_DOMAIN + url, detail_urls)
    return detail_urls


def prase_detail_page(url):
    movie = {}
    res = requests.get(url, headers=HEADERS)
    ret = res.content.decode('gbk')
    html = etree.HTML(ret)
    title = html.xpath(
        "//div[@class = 'title_all']//font[@color = '#07519a']/text()")[0]
    # *结尾是/text()，小写xpath
    movie['title'] = title
    # *获取最上面的标题

    zoomE = html.xpath("//div[@id = 'Zoom']")[0]
    # *xpath返回的是列表
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    infos = zoomE.xpath(".//text()")
    for index, info in enumerate(infos):
        # *enumerate()同时列出数据和数据下标
        if info.startswith("◎年　　代"):
            info = info.replace("◎年　　代", "").strip()
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = info.replace("◎产　　地", "").strip()
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = info.replace("◎类　　别", "").strip()
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = info.replace("◎豆瓣评分", "").strip()
            movie['douban_rating'] = info
        elif info.startswith("◎IMDb评分"):
            info = info.replace("◎IMDb评分", "").strip()
            movie['IMDB_rating'] = info
        elif info.startswith("◎片　　长"):
            info = info.replace("◎片　　长", "").strip()
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = info.replace("◎导　　演", "").strip()
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = info.replace("◎主　　演", "").strip()
            # *到这里获取了第一行主演
            actors = [info]
            for x in range(index + 1, len(infos)):
                # *index+1表示主演的第二行
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    # *如果开头为◎，就break，就不会把这次的actor加入actors
                    break
                actors.append(actor)
            movie["actors"] = actors
        elif info.startswith("◎简　　介"):
            info = info.replace("◎简　　介", "").strip()
            for x in range(index + 1, len(infos)):
                profile = infos[x].strip()
                if profile.startswith("【下载地址】"):
                    break
            movie['profile'] = profile
    download_url = html.xpath("//td[@bgcolor = '#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    return movie


def spider():
    movies = []
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    for x in range(1, 2):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            movie = prase_detail_page(detail_url)
            movies.append(movie)
            print(movie)
    # print(movies)


if __name__ == "__main__":
    spider()
