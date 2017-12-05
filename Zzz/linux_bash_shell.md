## 1.系统信息

  - lsb_release -a  查看系统信息

## 2. 用户，组
  -  useradd xx  添加用户
  -  passwd  xx  设置密码
  -  su  切换至root用户
  -  su  xx 切换至某用户

## 3.firewall  防火墙相关
  -  systemctl start  firewalld # 启动
  -  systemctl status firewalld # 或者 firewall-cmd --state 查看状态
  -  systemctl disable firewalld # 停止
  -  systemctl stop firewalld  # 禁用
  -  firewall-cmd --reload # 更新防火墙规则

### 添加端口
  - firewall-cmd --zone=public --permanent --add-port=3690/tcp 

### 查看防火墙
  - firewall-cmd  --list-all 

## 4.文件和目录操作
  - ll  查看当前目录资源的读写权限

  - ls -lh 可将文件大小用k显示

  - rm -rf  xx目录    (慎用)

  - mv a  b  将a重命名为b


## 5.查看日志

  - less   xx.log

  - cat -n xx.log

  - tail -100 xx.log

## 6.chmod 修改文件权限

### 格式如下 : [ugoa...][[+-=][rwxX]...][,...]，
-  其中 u 表示该档案的拥有者，g 表示与该档案的拥有者属于同一个群体(group)者，o 表示其他以外的人，a 表示这三者皆是。 
-  + 表示增加权限、- 表示取消权限、= 表示唯一设定权限。 
-  r 表示可读取，w 表示可写入，x 表示可执行，X 表示只有当该档案是个子目录或者该档案已经被设定过为可执行。 

语法为：chmod abc file 
其中a,b,c各为一个数字，分别表示User、Group、及Other的权限。 
r=4，w=2，x=1 

-  -rw------- (600) -- 只有属主有读写权限。
-  -rw-r--r-- (644) -- 只有属主有读写权限；而属组用户和其他用户只有读权限。
-  -rwx------ (700) -- 只有属主有读、写、执行权限。
-  -rwxr-xr-x (755) -- 属主有读、写、执行权限；而属组用户和其他用户只有读、执行权限。
-  -rwx--x--x (711) -- 属主有读、写、执行权限；而属组用户和其他用户只有执行权限。
-  -rw-rw-rw- (666) -- 所有用户都有文件读、写权限。这种做法不可取。
-  -rwxrwxrwx (777) -- 所有用户都有读、写、执行权限。更不可取的做法。
 
例如： chmod  777   a.txt   表示所有用户可读写执行a

