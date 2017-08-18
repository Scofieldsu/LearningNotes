## 安装rancher

- 创建 docker-compose.yml 文件：

``` python
version: '2'
services:
  rancher:
    image: rancher/server:stable
    restart: unless-stopped
    ports:
      - "8080:8080"
      - "9345:9345"
    environment:
      TZ: 'Asia/Shanghai'
    command: "--db-host 192.168.1.84 --db-port 3306 --db-user rancher --db-pass rancher123 --db-name rancher "
```
- 其中数据库相关信息根据自己所创建的填写。

- 运行： docker-compose up -d

## 关于rancher

- Rancher是一个开放源码的软件平台，可以让组织在生产中运行和管理Docker和Kubernetes。使用Rancher，组织不再需要使用不同的开源技术从头开始构建容器服务平台。Rancher提供管理生产中的容器所需的整个软件堆栈。

- [更多关于rancher](http://rancher.com/)
