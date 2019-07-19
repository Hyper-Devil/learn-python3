import os
# import sys
# sys.path.append('./old/')
# import fx
import test
# 同目录没问题

path1 = os.path.abspath('.')
# 当前目录
print(path1)
path2 = os.path.abspath('..')
# 上级目录
print(path2)
path3 = os.path.abspath('/')
# 根目录
print(path3)
# fx.print_hello()
test.print_hello()
