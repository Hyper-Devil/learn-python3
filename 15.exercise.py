# # ?计算0-100的和
# sum = 0
# for i in range(0, 101):
#     # *左闭右开
#     sum += i
# print('result is %d' % sum)

# # ?列举1-100质数
# # 质数：除了1和它本身以外不再有其他因数
# number = []

# def judge(i):
#     for m in range(2, i):
#         if i % m == 0:
#             break
#         elif (m < i - 1) and (i % m != 0):
#             continue
#         else:
#             number.append(int(i))

# for i in range(0, 101):
#     judge(i)
# print(number)
# *少了2

# *方法二
# def judge(i):
#     for m in range(2, i):
#         if i % m == 0:
#             return False
#     return True

# for i in range(2, 101):
#     if judge(i):
#         print(i)

# ?计算一篇文章中每个单词出现的次数
f = open('1.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()
# *按行读取成列表
count = {}
# *声明一个dict
for line in lines:
    tokens = line.strip().split(' ')
    # *split()分离成list[],strip()移除字符串头尾指定的字符
    # *也就是分离成单词组成的list
    for token in tokens:
        if token not in count:
            # *如果不在字典中，添加
            count[token] = 0
            # *默认出现次数0
        count[token] += 1

for word in count:
    print(word, count[word])
