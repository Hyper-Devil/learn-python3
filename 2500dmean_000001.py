import requests
import numpy as np
import matplotlib.pyplot as plt
import csv

# 设置图中中文字体
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
}

# code=0/1(沪/深)+6位代码
# 下载19991118至今的数据 5000天+

# Download_addres = 'http://quotes.money.163.com/service/chddata.html?code=0000001&start=19991118'
# f = requests.get(Download_addres, headers=HEADERS)
# with open("SH000001.csv", "wb") as code:
#     code.write(f.content)
# print("download done")

date = []
value = []
value_mean = []
with open('SH000001.csv', encoding='gbk') as f:
    f_csv = csv.reader(f)
    for i, row in enumerate(f_csv):
        if (i == 0):
            continue
        # print(row)
        date.append(row[0])
        value.append(float(row[3]))
        if (i >= 5000):  # 大于5000即取5000个
            break

assert len(date) == len(value)

date = date[::-1]
value = value[::-1]
# print(date)
# print(value)

for i in range(len(value)):
    if (i == 0):
        value_mean.append(value[0])
    elif (i > 0 and i < 2500):  # <5 前五个数
        value_mean.append(np.mean(value[0:i + 1]))
    else:  # 后
        value_mean.append(np.mean(value[i - 2500 + 1:i + 1]))  # -5 前五个数

# print(value_mean)
# print(len(value_mean))

value_mean_up = [x * 1.2 for x in value_mean]
value_mean_down = [x / 1.2 for x in value_mean]

plt.plot(date[-2500:], value[-2500:], c="royalblue", label="收盘价")
plt.plot(date[-2500:], value_mean[-2500:], c="cornflowerblue", label="2500天均线")
plt.plot(date[-2500:],
         value_mean_up[-2500:],
         c="lightsteelblue",
         label="2500天均线/1.2")
plt.plot(date[-2500:],
         value_mean_down[-2500:],
         c="lightsteelblue",
         label="2500天均线*1.2")
plt.xticks(date[-2500::50], rotation=90)
plt.legend(loc='best')
plt.xlabel('date', fontdict={'size': 16})
plt.ylabel('value', fontdict={'size': 16})
plt.title('2500天', fontdict={'size': 16})
plt.show()
