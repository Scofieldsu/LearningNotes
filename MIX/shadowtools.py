# coding=utf-8
## author:scofieldyu

import hashlib
import json
import subprocess


################### Tools function

## 服务动作
def service_action(action):
    subprocess.call("/etc/init.d/shadowsocks %s" %(action), shell=True)

## 删除配置中的端口
def remove_port(port,config):
    del config['port_password'][str(port)]
    write_file(config)
    print "删除端口成功..."

## 修改端口密码
def change_pwd(port,pwd,config):
    config['port_password'][str(port)] = str(pwd)
    write_file(config)
    print "密码修改成功..."

##  根据端口查询密码
def get_pwd_by_port(port,config):
    if str(port) in config['port_password'].keys():
        print config['port_password'][str(port)]
    else:
        print "端口不存在，查不到密码..."

## 查询端口是否存在于配置文件中
def find_port_config(port,config):
    print "检查端口是否已存在..."
    if str(port) in config['port_password'].keys():
        print str(port) + "端口已经存在于配置中..."
        return True
    else:
        print str(port) + "端口不在配置中..."
        return False


## 返回已在配置文件中的端口
def get_config_port_list(config):
    for x in config['port_password'].keys():
        print x


## 返回协议
def get_ss_method(config):
    print config['method']


## 获取配置文件的字典
def get_config():
    f = file(filename)
    config = json.load(f)
    return config

## 写入文件
def write_file(config):
    out = file(filename, 'w+')
    json.dump(config, out, indent=4)


#根据端口号计算密码,为16位md5的前6位
def get_md5_pwd(port):
    m2 = hashlib.md5()
    m2.update(str(port))
    print "【密码:】" + m2.hexdigest()[8:14]
    return m2.hexdigest()[8:14]

## 防火墙打开端口
def open_firewall_port(port):
    port_str = str(port)
    print "防火墙开启%s tcp端口..."%(port_str)
    subprocess.call("firewall-cmd --permanent --zone=public --add-port=%s/tcp" %(port_str), shell=True)
    print "防火墙开启%s udp端口..."%(port_str)
    subprocess.call("firewall-cmd --permanent --zone=public --add-port=%s/udp" %(port_str), shell=True)
    print "重载防火墙配置..."
    subprocess.call("firewall-cmd --reload", shell=True)

################################  Features  function

## 1. 新增端口账号

def add_port(port):
    port_str = str(port)
    exist_fg = find_port_config(port_str,config)
    if exist_fg:
        print "==========端口已存在!!!============"
    else:
        ## 防火墙新增端口
        open_firewall_port(port_str)

        ## 端口密码写入配置
        add_port_pure(port_str)
        print "写入配置成功..."

        ## 重启服务
        service_action('restart')



def add_port_pure(port_str):
    # (1) 获取密码
    pwd_str = get_md5_pwd(port_str)

    # (2) 写入配置
    config['port_password'][port_str] = pwd_str
    write_file(config)




##  提示语句
point_string = '''
1. 新增端口账号
2. 查询单个端口密码
3. 查询已存在所有端口
4. 查询协议
5. 重启服务
6. 检查某个端口是否已在配置中
7. 删除端口
8. 修改密码
9. 重新查看选项
10. 端口添加防火墙规则
'''
def  main():
    fg = True
    print point_string
    while fg:
        value = input("请选择对应序号操作，按0退出：")
        if value == 1:
            value_port = input("请输入端口：")
            add_port(value_port)
        elif value == 2:
            value_port = input("请输入端口：")
            get_pwd_by_port(value_port,config)
        elif value == 3:
            get_config_port_list(config)
        elif value == 4:
            get_ss_method(config)
        elif value == 5:
            service_action('restart')
        elif value == 6:
            value_port = input("请输入端口：")
            find_port_config(value_port,config)
        elif value == 7:
            value_port = input("请输入端口：")
            remove_port(value_port,config)
        elif value == 8:
            value_port = input("请输入端口：")
            value_pwd = raw_input("请输入新密码：")
            change_pwd(value_port,value_pwd,config)
        elif value == 0:
            fg = False
        elif value == 9:
            print point_string
        elif value == 10:
            value_port = input("请输入端口：")
            open_firewall_port(value_port)
        else:
            print "请重新选择正确的编号..."

if __name__ == '__main__':
    filename = '/etc/shadowsocks.json'
    config = get_config()
    main()
