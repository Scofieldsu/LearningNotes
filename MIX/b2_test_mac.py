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


B1_LIST = ['2', '3', '6', '7', 'A', 'B', 'E', 'F']
AP_FILE = 'D:/yu/mac_copy.csv'
AP_FILE_TEST = 'D:/yu/test.csv'
OUI_FILE = 'D:/yu/oui.txt'
OUI_FILE_TEST = 'D:/yu/oui_test.txt'
OX_CHECK = '(hex)'


## ap文件的MAC地址去重
def remove_duplicates_mac(filename):
    with open(filename,"rb") as f:
        reader = csv.reader(f)
        result=list(reader)
    result_simple = []
    m = 0
    for x in xrange(len(result)):
        try:
            m+=1
            item = result[x][0]
            if item:
                if item not in result_simple:
                    result_simple.append(item)
        except Exception as e:
            print u"异常：AP.csv的"+str(m+1)+ u"行内容:" + str(result[x])
    print u"ap.csv中的MAC地址总记录条数：" + str(len(result))
    print u"ap.csv去重后的MAC总记录条数："+str(len(result_simple))
    return result_simple

## 根据b1位检测；根据前3字节是否已注册判断
def b1_check(result_simple,oui_prefix):
    # with open(filename,"rb") as f:
    #     reader = csv.reader(f)
    #     result=list(reader)
        ## 统计为1的行数
        all_m = []
        all_prefix = []
        unregist_mac = []
        m = 0
        for x in xrange(len(result_simple)):
            try:
                m+=1
                item = result_simple[x]
                # print item
                if item:
                    ## MAC 地址前8位即位前3字节   xx:xx:xx
                    prefix = item[0:8]
                    # print prefix
                    ## 判断是否在注册列表
                    if prefix not in oui_prefix:
                        all_prefix.append(m)
                        unregist_mac.append(item)
                    a = item.split(':')
                    b = a[0][1]

                    ##判断 B1位是否转换二进制后倒数第二位为1
                    if b in B1_LIST:
                        all_m.append(m)
            except Exception as e:
                pass
        print u"b1位检测的伪MAC地址条数："+ str(len(all_m))
        print u"伪MAC行数列表：" + str(all_m)
        print u"前3字节判断，没有注册的条数：" + str(len(all_prefix))
        print u"没有注册的MAC对应的行数列表：" + str(all_prefix)
        print u"没有注册的MAC为：" + str(unregist_mac)


## 把IEEE公开的oui文件转换为MAC地址前3字节的列表
def oui_check(filename):
    mac_prefix_list = []
    with open(filename,"rb") as file_oui:
        for line in file_oui:
            mac_prefix = trans_mac_from_line(line)
            if mac_prefix:
                mac_prefix_list.append(mac_prefix)
    print u"oui总记录条数：" + str(len(mac_prefix_list))
    return mac_prefix_list


## 根据oui文件每一行取出MAC前3字节
def trans_mac_from_line(line):
    x = ''
    if OX_CHECK in line:
        a = line.split(OX_CHECK)
        if len(a) > 0:
            x = a[0].strip().replace('-',':')
    return x


def main():
    oui_maclist = oui_check(OUI_FILE)
    result_simple = remove_duplicates_mac(AP_FILE)
    b1_check(result_simple,oui_maclist)


main()
