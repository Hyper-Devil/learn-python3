with open(r'D:\learn-cpp\DataSet\red2\train.txt', 'r+') as f:
    # r+ 读写
    lines = f.readlines()
    for line in lines:
        f.writelines(str(line.strip()) + ' 1\n')