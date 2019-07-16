a = 2
if a == 1:
    print('a == 1')
elif a == 2:
    print('a == 2')
elif a != 1 and a != 2:
    # elif a != 1:
    # 系统只执行第一个elif
    print('a != 1 or 2')

list_a = [1, 2, '3']
for i in list_a:
    # for后边也有冒号
    print(i)

for i in range(5, 8):
    # 还是左闭右开
    print(i)

b = 0
# 一定要给b赋值，否则会报错
while b != 5:
    print(b)
    b += 1

c = 1
while c <= 10:
    if c in range(2, 5):
        print("c∈[2, 5)")
        break
        # break会直接跳出并结束循环 所以不会输出2
    print(c)
    c += 1

c = 5
while c <= 10:
    if c in range(6, 9):
        print("c∈[6, 9)")
        continue
        # continue可以提前结束本轮循环，并直接开始下一轮循环。所以本段代码死循环
    print(c)
    c += 1
