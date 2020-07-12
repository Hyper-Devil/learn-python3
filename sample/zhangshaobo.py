import numpy as np
import pandas as pd
import time
import random


def read():
    #1.打开CSV文件
    fileNameStr = 'C:/Users/WHD/Desktop/BeijingPM20100101_20151231.csv'
    df = pd.read_csv(fileNameStr,
                     encoding='utf-8',
                     usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    #说明我只用前几列；节省内存 A-J

    # print(df.head())
    # print("================================")
    # print(df.describe())
    # print("================================")
    # print(df.info())
    # print("================================")

    #2.查看是否有缺失值
    # print(df.isnull().sum().sort_values(ascending=False))
    # print("================================")
    #df.drop(["DEWP","HUMI","PRES","TEMP","cbwd","Iws","precipitation","Iprec"],axis=1,inplace=True)
    #print("*********************************")
    #print(df["DEWP"])

    #3.去掉三列PM数据全部为空的行
    print(df.info())
    df.dropna(
        axis='index',
        how='all',
        subset=['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post'],
        inplace=True)

    print("**************************")

    print(df.info())
    df.to_csv("bj.csv")  #打印数据处理后的文件

    #4.计算平均值
    start = time.time()
    df['sum'] = df[[
        'PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post'
    ]].sum(axis=1)
    #df['PM_Taiyuanjie']+df['PM_US Post']+df['PM_Xiaoheyan']
    df['count'] = df[[
        'PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post'
    ]].count(axis=1)
    df['ave'] = round(df['sum'] / df['count'], 2)

    end = time.time()  #啥意思
    print(end - start)  #啥意思

    #5.输出到文件
    df.to_csv("PM_BeiJing02.csv")
    print("****** done ******")

    #6.按照年做汇总，查看年的平均值
    print(df.groupby("year","mouth").mean())

    #以上都对，现在想要做7

    #7，按年分组，计算月均值变化


if __name__ == "__main__":
    read()
