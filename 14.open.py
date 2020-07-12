with open("D:\\learn-python3\\sample\\yys_map.txt", "r", encoding='utf-8') as f:
    # *暂时使用绝对路径吧，相对路径老是不行，可能和vscode有关。解决
    # *打开中文txt把gbk编码转为utf-8
    f.readline()
    i = 1
    for line in f:
        print(line)
        print(i)   
        i += 1     
    # *调用readline()可以每次读取一行内容，返回的是一个字符串对象；调用readlines()一次读取所有内容并按行返回list
