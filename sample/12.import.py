import os
import old.mymodel
# *需要__init__.py

# from old import mymodel
# print_hello()
# *不推荐

import sys
sys.path.append('./')
import test
# TODO 仍未解决的问题：如何加载任意目录下的模块
# *解决

path1 = os.path.abspath('.')
# 当前目录
print(path1)
path2 = os.path.abspath('../')
# 上级目录
print(path2)
path3 = os.path.abspath('/')
# 根目录
print(path3)
old.mymodel.print_hello()
test.print_hello2()
