s = 'abcde'
print(s.find('b'))
print(s.find('c'))
print(s.find('e'))
print(s.find('x'))
# *返回的是第一个匹配的子串的下标位置，如果没有找到，返回-1

s = 'aa12bb12cc'
print(s.split('12'))
# *返回分割后的列表

s = 'abc'
print(s.upper())
print(s.lower())

s = 'abcdefg'
print(s[2:5])
print(s[:5])
print(s[3:])
print(s[3:-1])
# *左闭右开 -1是g，不包括

s1 = 'wasd'
s2 = 'qwer'
print(s1 + s2)

s = 'axbxcxdxe'
print(s.replace('x', '#'))

s = ['a', 'b', 'c']
# 连接字符串中元素
s1 = ','.join(s)
s2 = '-'.join(s)
print(s)
print(s1)
print(s2)

s = 'abcdefg'
print(s[::-1])
# 反转
print(s[::2])
# 从第0个开始每两个取一个
print(s[1::3])
# 从第1个开始每三个取一个
