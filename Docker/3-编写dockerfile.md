
---

# 编写Dockerfile

- 

``` javascript
RUN apt-get update && apt-get install -y \
    aufs-tools \
    automake \
    build-essential \
    curl \
    dpkg-sig \
    libcap-dev \
    libsqlite3-dev \
    mercurial \
    reprepro \
    ruby1.9.1 \
    ruby1.9.1-dev \
    s3cmd=1.1.* \
 && rm -rf /var/lib/apt/lists/*
```

- 构建缓存

    - 对于ADD和COPY指令，检查图像中文件的内容，并为每个文件计算校验和。在这些校验和中不考虑文件的最后修改和最后访问的时间。在缓存查找期间，将校验和与现有映像中的校验和进行比较。如果文件（如内容和元数据）中有任何变化，则缓存无效。

    - 除了ADD和COPY命令之外，缓存检查不会查看容器中的文件来确定缓存匹配。

- RUN 

    - RUN <command>（shell窗体，命令在shell中运行，默认情况下/bin/sh -c在Linux或cmd /S /CWindows上）

    - RUN ["executable", "param1", "param2"]（执行表单）

- COPY 

``` javascript
如果特定需要的文件更改，这将确保每个步骤的构建缓存仅被无效（强制该步骤重新运行）。

例如：

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

导致RUN步骤的缓存无效的数量减少，而不是放在 COPY . /tmp/前面。
```

- 

``` javascript
RUN mkdir -p /usr/src/things \
    && curl -SL http://example.com/big.tar.xz \
    | tar -xJC /usr/src/things \
    && make -C /usr/src/things all

```

- 
``` javascript
可以使用-f标记docker build来指向文件系统中的任何位置的Dockerfile。

$ docker build -f /path/to/a/Dockerfile .
```