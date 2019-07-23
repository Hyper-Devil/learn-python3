with open('1.txt', 'r') as f:
    # *将vscode工作文件夹调整到sample文件夹  相对路径正常
    # print(f.read())
    c = f.read()
print(c)
# *文件关闭之后依然存在

with open('1.txt', 'r') as f:
    # *将vscode工作文件夹调整到sample文件夹  相对路径正常
    # print(f.read())
    c = f.readlines(10000)
    # *一次性读取整个文件；自动将文件内容分析成一个行的列表。10000字节打开限制
print(c)
# *文件关闭之后依然存在

with open(r'D:\learn-python3\sample\1.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line.strip())
        # *把末尾的'\n'删掉
        line = f.readline()

with open(r'D:\learn-python3\sample\1.txt', 'a') as f:
    # *参数a是在末尾追加  w覆写
    text = ['i love python\n', 'i hate python\n']
    f.writelines(text)
    # *writelines()中的参数只有一个。不同于write()，writelines()支持str同时也支持list写入
    # *如果使用list写入txt文件，可以写入多行；如果使用str写入txt文件，则只能写入一行。
    # *在list中的每个元素末尾必须加上’\n’的换行符，否则list中的各元素将写入一行之中
