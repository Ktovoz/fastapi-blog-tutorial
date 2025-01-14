
# 📚 目录

- [🚀 FastAPI & PyWebview Blog Application](#fastapi--pywebview-blog-application)
  - [📖 简介](#简介)
  - [🎯 主要特性](#主要特性)
  - [🛠️ 技术栈](#技术栈)
  - [🚀 快速开始](#快速开始)
  - [📂 项目结构](#项目结构)
  - [🌐 WebSocket 集成](#websocket-集成)
  - [🎨 模板渲染](#模板渲染)
  - [❓ 常见问题](#常见问题)
  - [🤝 贡献指南](#贡献指南)
  - [📜 许可证](#许可证)
  - [📚 相关资源](#相关资源)
  - [🎉 感谢支持](#感谢支持)
  - [📬 联系我们](#联系我们)

---

# 🚀 FastAPI & PyWebview Blog Application

## 📖 简介

<div align="center">
  <h3>🌟 Star 本项目</h3>
  <p>如果你觉得这个项目对你有帮助，请给它一个 ⭐️ 支持！</p>
</div>

---

<div align="center">
  <h3>🚀 开始你的开发之旅</h3>
  <p>现在就克隆项目，开始你的开发之旅吧！</p>
  <pre><code>git clone https://github.com/Ktovoz/fastapi-blog-tutorial.git</code></pre>
</div>

---

<div align="center">
  <h3>📌 重要提示</h3>
  <p>本项目仍在积极开发中，可能会有重大更改。请定期查看更新。</p>
</div>

---

<div align="center">
  <h3>📊 项目状态</h3>
  <img src="https://img.shields.io/github/last-commit/Ktovoz/fastapi-blog-tutorial" alt="Last Commit">
  <img src="https://img.shields.io/github/issues/Ktovoz/fastapi-blog-tutorial" alt="Issues">
  <img src="https://img.shields.io/github/stars/Ktovoz/fastapi-blog-tutorial" alt="Stars">
  <img src="https://img.shields.io/github/forks/Ktovoz/fastapi-blog-tutorial" alt="Forks">
</div>

---

本项目是一个基于 **FastAPI** 和 **PyWebview** 的通讯系统，通过 **WebSocket** 实现实时通信，并使用 **Jinja2** 模板引擎生成动态页面。无论是对于想要学习 **FastAPI** 的新手，还是对于希望深入理解 **PyWebview** 和模板渲染的开发者，本项目都是一个不错的参考案例。

### 🌟 欢迎学习与使用

我们非常欢迎各位开发者学习本项目的代码结构和技术实现，同时也鼓励大家以本项目为基础，搭建自己的应用。如果你有任何问题或需要帮助，请随时联系我们的社区或提交 [Issue](https://github.com/Ktovoz/fastapi-blog-tutorial/issues)。

此外，你可以参考作者撰写的详细博客文章，了解更多的开发细节和技巧：
- [FastAPI & PyWebview 博客应用开发教程](https://blog.csdn.net/Ktovoz/article/details/14513850)

---

## 🎯 主要特性

- **基于 FastAPI 的 RESTful API 设计**
- **使用 WebSocket 实现实时通信**
- **通过 Jinja2 模板引擎渲染动态页面**
- **使用 PyWebview 创建桌面应用程序**
- **完善的错误处理和日志记录**
- **易于扩展和维护的项目结构**

---

## 🛠️ 技术栈

- **后端框架**：FastAPI
- **实时通信**：WebSocket
- **模板引擎**：Jinja2
- **桌面应用封装**：PyWebview
- **异步支持**：Asyncio

---

## 🚀 快速开始

### 1. 安装依赖

确保你已经安装了所有必要的依赖项，可以通过运行以下命令来完成：

```bash
pip install -r requirements.txt
```
### 2. 启动应用

#### 2.1 启动 FastAPI 服务器

在终端中运行以下命令来启动 **FastAPI** 服务器：

```bash
python app/main.py --server
```
#### 2.2 启动桌面应用

在终端中运行以下命令来启动 **PyWebview** 桌面应用：

```bash
python app/main.py
```
#### 2.3 参数说明

你可以通过以下参数来配置应用的启动行为：

- `--server`: 仅启动 FastAPI 服务器，不启动 PyWebview 桌面应用。
- `--host <地址>`: 指定 FastAPI 服务器监听的地址，默认为 `0.0.0.0`。
- `--port <端口>`: 指定 FastAPI 服务器监听的端口，默认为 `8000`。
- `--index-path <路径>`: 指定网页入口文件的路径，默认为 `templates/index.html`。

例如，如果你想启动服务器并指定监听地址和端口，可以运行：

```bash
python app/main.py --server --host 127.0.0.1 --port 8080
```
如果你想启动桌面应用并指定网页入口文件路径，可以运行：

```bash
python app/main.py --index-path templates/custom_index.html
```
### 3. 访问主页

打开浏览器，访问 [http://127.0.0.1:8000](http://127.0.0.1:8000)，你应该能够看到主页。

---

## 📂 项目结构

```
.
├── app/                 # 应用代码目录
│   ├── main.py          # 主入口文件
│   ├── routers/         # 路由定义
│   ├── templates/       # 模板文件
│   └── models/          # 数据模型（如果使用数据库）
├── tests/               # 测试代码目录
├── requirements.txt     # 项目依赖文件
└── README.md            # 项目介绍文件
```

---

## 🌐 WebSocket 集成

本项目通过 **WebSocket** 实现实时通信，例如实时更新博客文章的评论。WebSocket 的相关代码主要位于 [routers](./routers/) 目录下。

---

## 🎨 模板渲染

本项目使用 **Jinja2** 作为模板引擎，模板文件位于 [templates](./templates/) 目录下。通过 **FastAPI** 的 `HTMLResponse` 和模板引擎集成，可以轻松实现动态页面的渲染。

---

## ❓ 常见问题

### Q: 如何添加新的功能？

**A**: 可以在 [routers](app/routers/) 目录下添加新的路由和处理函数，同时在 [templates](./templates/) 目录下添加相应的模板文件。

---

## 🤝 贡献指南

欢迎任何对本项目感兴趣的开发者贡献代码或提出改进建议。请遵循以下步骤进行贡献：

1. **Fork 本项目**：点击 GitHub 页面右上角的 "Fork" 按钮，将项目复制到你的仓库。
2. **克隆仓库**：将 fork 后的仓库克隆到本地。
3. **创建分支**：为新功能或修复创建一个新的分支。
4. **提交更改**：在本地开发并测试后，提交更改。
5. **推送更改**：将更改推送到你的远程仓库。
6. **提交 Pull Request**：在 GitHub 上提交 Pull Request，描述你的更改内容。

---

## 📜 许可证

本项目采用 **MIT** 协议，详情请参考 [LICENSE](LICENSE) 文件。

---

<div align="center">
  <h3>📚 相关资源</h3>
  <ul>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI 官方文档</a></li>
    <li><a href="https://pywebview.flowrl.com/">PyWebview 官方文档</a></li>
    <li><a href="https://jinja.palletsprojects.com/">Jinja2 官方文档</a></li>
  </ul>
</div>

---

<div align="center">
  <h3>🎉 感谢支持</h3>
  <p>感谢所有贡献者和用户的支持！</p>
  <a href="https://github.com/Ktovoz/fastapi-blog-tutorial/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=Ktovoz/fastapi-blog-tutorial" />
  </a>
</div>

---

<div align="center">
  <h3>📌 标签</h3>
  <p>#FastAPI #PyWebview #WebSocket #Jinja2 #Python #DesktopApp</p>
</div>

---

<div align="center">
  <h3>📬 联系我们</h3>
  <p>有任何问题或建议？欢迎通过 <a href="https://github.com/Ktovoz/fastapi-blog-tutorial/issues">GitHub Issues</a> 联系我们。</p>
</div>
