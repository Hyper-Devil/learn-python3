def print_hello():
    # 冒号结尾
    print('hello')


print_hello()


def print_str(s):
    print(s)
    return s * 2
    # return代表函数的返回值


print(print_str('fuck'))


def print_default(s='hello'):
    # print(s)
    # 如果不注释掉这一行，就会输出两个hello
    return s
    # 如果注释掉这一行，就会输出none


print(print_default())
print(print_default('default'))


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
print(power(5, 1))


def calc(*numbers):
    # 在前面加个*变成可变参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))
print(calc(1, 2, 3))
nums = [1, 2, 3, 4]
print(calc(*nums))
# *nums表示把nums这个list的所有元素作为可变参数传进去


def print_two(a, b):
    print(a, b)
    # return a, b


print_two(a='a', b='b')
print_two(b='b', a='a')
# 定义的函数中有print  此时不需要了


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
