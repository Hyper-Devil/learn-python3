import sys


def test():
    args = sys.argv
    # *sys模块有一个argv变量，用list存储了命令行的所有参数。
    # *argv至少有一个元素，因为第一个参数永远是该.py文件的名称。
    if len(args) == 1:
        print('hello world!')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('two many arguments!')


if __name__ == '__main__':
    test()
# *当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# *而如果在导入该hello模块时，if判断将失败
# *因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
# *cmd运行python hello.py Michael获得的sys.argv就是['hello.py', 'Michael]，输出hello, Michael!。
# *直接运行则输出hello world！
