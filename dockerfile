# 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制代码到容器
COPY . /app

# 暴露端口
EXPOSE 5000

# 启动服务
CMD ["python", "app.py"]
