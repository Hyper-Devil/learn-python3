classmates = ['Michael', 'Bob', 'Tracy']
# list是一种有序的集合，可以随时添加和删除其中的元素。使用方括号[]
print(len(classmates))
print(classmates)
print(classmates[0])
print(classmates[1])
# 索引从0开始
print(classmates[-1])
# 倒数第一个元素
classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
# 插入‘Jack’到第二个位置
print(classmates)
classmates.pop()
# 删除末尾元素
print(classmates)
classmates.pop(1)
# 删除索引位置元素
print(classmates)
classmates[1] = 'Sarah'
# 通过直接赋值来替换索引位置元素
print(classmates)

classmates = ('Michael', 'Bob', 'Tracy')
# 元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改,使用圆括号()
print(classmates)
# 可以同名
t = (1,)
# 如果定义的tuple只有一个元素，需要加上逗号，与小括号区分开
print(t)
# 输出的时候也会显示逗号
