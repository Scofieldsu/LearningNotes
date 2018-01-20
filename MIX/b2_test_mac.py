# coding=utf-8

import csv

## 判断MAC地址第一个字节的次有效位是否为1,1为伪mac

## 首字节为2位16进制，16进制转换2进制可以单独给每一位转换后连接起来；则只需判断首字节第二位转换后的倒数第二位是否为1

## 对于1位16进制转换，可以先列出来有哪些字符转换后倒数第二位为1  【2, 3, 6, 7, A, B, E, F】

# 2   ==  0010

# 3   ==  0011
# 6   ==  0110
# A   ==  1010

# 7   ==  0111
# B   ==  1011
# E   ==  1110

# F   ==  1111

last_list = ['2', '3', '6', '7', 'A', 'B', 'E', 'F']
filename = 'D:/yu/mac_copy.csv'
# filename = 'D:/yu/test.csv'

with open(filename) as f:
    reader = csv.reader(f)
    result=list(reader)
    ## 统计为1的行数
    all_m = []
    m = 0
    print len(result)
    # for x in result:
    #     print x
    #     m+=1
    #     a = x[0].split(':')[0][1]
    #     if a in last_list:
    #         n+=1
    #         all_m.append(m)
    # print len(all_m)
    # print all_m
