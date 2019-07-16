StudentName_Number = {101: "alan", 102: "bob", 103: "lucy"}
# 字典，无序可更改
print(StudentName_Number[101])
# 变量名称区分大小写
StudentName_Number[102] = 'jack'
# 后面的值会把前面的值冲掉
print(105 in StudentName_Number)
# 判断key是否存在
print(StudentName_Number.get(105, 'not exist'))
# 是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
StudentName_Number.pop(102)
print(StudentName_Number)

s = set([1, 1, 2, 2, 3])
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
print(s)
s.add(4)
print(s)
s.remove(3)
# remove并不是pop   弹幕说与栈的概念有关
print(s)

s1 = set([1, 2, 3])
s2 = set([4, 2, 3])
# 注意是set([])
print(s1 & s2)
# 数学上的交集
print(s1 | s2)
# 数学上的并集
