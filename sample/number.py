a = 1
b = 1.0
c = 10000
# python3中长整数不用再加L

print('你好世界')
# pyhon3 print函数格式：print()
print('hello world!')
print(a)
print(b)
print(c)

str = 'hello world'
# 字符串

print('字符串')
print(str)
print(str[0])
# 切片 数字从0开始
print(str[2:5])
# 左闭右开
print(str[2:6])
# 此时末尾输出了一个空格
print(str[2:])
# 输出从第3个字符开始的字符串
print(str * 2)
# 输出字符串两次
print(str * 2)
print(str + 'TEST')
# 输出字符串连接字符串

list_a = ["str", 1, ["a", "b", "c"], 4]
'''
列表
一个有序可变集合的容器。不同的数据结构也可以放在同一个列表中，没有统一类型的限制。使用[]方括号
'''
list_b = ["hello"]
print('列表')
print(list_a[0])
print(list_a[1:3])
# 输出含第二个和第三个元素的列表
print(list_a[1:])
# 输出含从第二个开始的元素的列表
print(list_b * 2)
# 输出含两个list_b元素的列表
print(list_a + list_b)
# 输出含list_a和list_b的列表

tuple_a = ("str", 1, ["a", "b", "c"], 4)
# 元组 赋值后不可变的列表 使用()圆括号
tuple_b = ("hello", )
# 只有1个元素的tuple定义时必须加一个逗号,  来消除歧义
print('元组')
print(tuple_a[0])
print(tuple_a[1:3])
print(tuple_a[1:])
print(tuple_b * 2)
print(tuple_a + tuple_b)

dict_a = {"name": "Alan", "age": 24, 1: "level_1"}
print('字典')
print(dict_a["name"])
# 查找
print(dict_a["age"])
print(dict_a[1])
print("name" in dict_a)
# 判断key是否存在
print("xxx" in dict_a)
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())
dict_a[2] = 'level_2'
# 放入新数据，可覆盖
print(dict_a[2])
