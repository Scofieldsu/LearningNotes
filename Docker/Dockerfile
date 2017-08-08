# 基础镜像
FROM pypy:2
# 作者
MAINTAINER Yu Yuan
# 升级apt-get update
RUN apt-get update && apt-get install -y --no-install-recommends \
		net-tools \
	&& rm -rf /var/lib/apt/lists/*
# 环境变量
ENV APP_ROOT /code
# 工作目录
WORKDIR ${APP_ROOT}
# 端口
EXPOSE 5050
# 复制文件
COPY . ${APP_ROOT}/
# 安装依赖
RUN pip install --no-cache-dir --trusted-host mirrors.aliyun.com -i http://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
# 运行命令
CMD ["gunicorn","-c","gun.conf", "run:app"]