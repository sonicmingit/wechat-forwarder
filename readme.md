# 🚀 企业微信消息转发服务

> 📢 **轻松解决企业微信白名单IP限制问题，让动态IP主机也能自由调用企业微信API。**

---

## 💡 痛点问题

企业微信的API调用通常都要求调用方服务器IP加入到企业微信的白名单中。
但实际工作中可能面临以下问题：

- 开发人员IP地址不固定，无法加入白名单。
- 临时调试和测试不便，需要频繁变更白名单。
- 缺乏一个稳定的固定IP作为调用企业微信API的中转服务器。

本项目旨在解决这些痛点，通过部署在固定IP服务器的中转服务实现消息透明转发。

---

## 🛠️ 功能说明

✅ **请求透明转发**

- 完全透传请求的URL路径、请求头、参数及请求体。
- 真实返回企业微信API的响应。

✅ **日志记录**

- 完整记录请求和响应信息，方便排查问题。

✅ **部署便捷**

- 使用Docker部署，极大简化运维和部署过程。

---

## 📦 部署说明

### 1️⃣ 克隆项目

```bash
git clone <本项目地址>
```

### 2️⃣ 文件结构

```
wechat-forwarder/
├── app.py
├── requirements.txt
└── Dockerfile
```

### 3️⃣ 构建Docker镜像

```bash
docker build -t wechat-forwarder .
```

### 4️⃣ 启动Docker容器

```bash
docker run -d -p 5000:5000 --restart=always --name wechat-forwarder wechat-forwarder
```

🎉 至此服务已部署完成，监听端口为`5000`。

---

## 🔍 使用说明

直接将企业微信API的调用路径前缀更换为你服务器的固定IP即可：

例如原本调用：
```
https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN
```

更改为：
```
http://你的固定服务器IP:5000/cgi-bin/message/send?access_token=ACCESS_TOKEN
```

### 📌 示例调用

```bash
curl -X POST 'http://你的固定服务器IP:5000/cgi-bin/message/send?access_token=你的ACCESS_TOKEN' \
-H 'Content-Type: application/json' \
-d '{
     "touser" : "@all",
     "msgtype" : "text",
     "agentid" : 你的应用AgentId,
     "text" : {
         "content" : "测试消息转发"
     },
     "safe":0
}'
```

---

## 📚 常见问题QA

**Q1：请求返回`Not Found`怎么办？**

A：表示访问了错误的路径或根路径未设置，确保调用企业微信API的具体路径，而非根路径。

**Q2：如何查看日志排查问题？**

A：通过以下命令实时查看容器日志：
```bash
docker logs -f wechat-forwarder
```

**Q3：服务转发超时如何解决？**

A：确认固定IP服务器与企业微信API网络连通性，检查是否有防火墙或安全策略阻止请求。

**Q4：服务是否可以处理高并发请求？**

A：当前服务简单设计，适用于日常开发和小规模使用。如需高并发支持，建议加入负载均衡或扩展服务能力。

---

## 📝 更新和维护

欢迎提交Issues或PR，持续优化本项目。

---

📌 **感谢您的使用，欢迎Star支持！✨**
