FROM swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/ubuntu:22.04
MAINTAINER author "dinglei@kernelsoft.com"
# 更换源操作,目前无其他合适的国内源,更换后会导致失败。
# COPY sources.list /etc/apt/
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /workdir

# 更新源
RUN	apt update
# 安装 python3
RUN	apt install python3 python3-pip -y
# 安装 akshare(数据来源)
RUN pip install akshare --upgrade
# 安装 pybroker(机器学习算法)
RUN pip install lib-pybroker
# 安装 backtrader(回测工具)
RUN pip install backtrader
RUN pip install matplotlib