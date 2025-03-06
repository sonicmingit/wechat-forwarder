# -*- coding: utf-8 -*-
import logging
import requests
from flask import Flask, request, Response

app = Flask(__name__)

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])

# 企业微信API域名
WECHAT_API_BASE = "https://qyapi.weixin.qq.com"

@app.route('/<path:path>', methods=['POST', 'GET'])
def forward_request(path):
    """
    接收请求并转发到企业微信API
    """
    try:
        # 构建企业微信API完整的URL
        forward_url = f"{WECHAT_API_BASE}/{path}"

        # 获取请求方法、头部信息、查询参数和请求体
        method = request.method
        headers = {key: value for key, value in request.headers if key != 'Host'}
        params = request.args
        data = request.get_data()

        logging.info(f"接收到请求，路径: {path}，方法: {method}，参数: {params}，请求体长度: {len(data)}")

        # 转发请求
        response = requests.request(method=method,
                                    url=forward_url,
                                    headers=headers,
                                    params=params,
                                    data=data,
                                    timeout=10)

        logging.info(f"请求转发成功，企业微信返回状态码: {response.status_code}")

        # 返回企业微信响应内容
        return Response(response.content, status=response.status_code, headers=dict(response.headers))

    except requests.exceptions.RequestException as e:
        logging.error(f"请求转发失败: {str(e)}")
        return Response(f"请求转发失败: {str(e)}", status=500)

if __name__ == '__main__':
    logging.info("企业微信消息转发服务已启动，监听端口5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
