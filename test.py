#encoding=utf-8

with open('testSet/data', 'rb') as f:
    for line in f.readlines():
        items = line.decode('utf-8').strip().split('\t')
        if items.__len__() < 2:
            continue
        print (items[1])