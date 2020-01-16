from bs4 import BeautifulSoup
import requests
URL = 'http://www.baidu.com/s?wd='
word = '御魂「魂」的两件套可能触发的效果是?'

HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
# url = 'http://www.paopaoche.net/sj/120926.html'

# res = requests.get(url, headers=HEADERS)
# soup = BeautifulSoup(res.content.decode('gbk'), 'lxml')
# span = soup.find_all('span', style = 'color: rgb(23, 54, 93);')[0]
# print(span)
# strong = span.find('strong')
# print(strong)
# ans = span.string
# print(ans)

res = requests.get(URL + str(word), headers=HEADERS)
print(res.text)
