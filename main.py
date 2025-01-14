# 导入必要的库和模块
import os  # 提供与操作系统交互的功能，如文件路径操作
import threading  # 允许程序并发运行多个线程，用于同时启动服务器和webview窗口
import time  # 提供时间处理函数，如休眠
import argparse  # 解析命令行参数

import uvicorn  # 用于运行FastAPI应用的ASGI服务器实现
import webview  # 创建原生桌面GUI窗口，用于显示HTML页面
from loguru import logger  # 强大的日志记录库，提供简洁的日志输出

from app import app  # 导入FastAPI应用实例


class WebSocketServer:
    def __init__(self, **kwargs):
        """
        初始化WebSocketServer类的实例。

        参数:
            kwargs (dict): 包含配置项的字典，支持以下键值：
                - host (str): 服务器监听地址，默认为 '0.0.0.0'
                - port (int): 服务器监听端口，默认为 8000
                - index_path (str): 网页入口文件路径，默认为 "templates/index.html"
        """
        self.host = kwargs.get('host', '0.0.0.0')  # 设置服务器监听地址
        self.port = kwargs.get('port', 8000)  # 设置服务器监听端口
        self.index_path = kwargs.get('index_path', os.path.join("templates", "index.html"))  # 设置网页入口文件路径
        self.app = app  # 绑定FastAPI应用实例

    def start_webview(self):
        """
        启动webview窗口，加载指定的HTML文件。
        """
        webview.create_window('Web Socket Example', str(self.index_path), width=1000, height=800, resizable=True)
        # 创建一个名为'Web Socket Example'的窗口，加载index_path指定的HTML文件，
        # 设置窗口宽度为1000px，高度为800px，并允许调整大小
        webview.start(self.start_server, gui='cef')  # 启动webview事件循环，保持窗口打开，并在启动时调用start_server方法

    def start_server(self):
        """
        启动FastAPI服务器。
        """
        uvicorn.run(self.app, host=self.host, port=self.port)
        # 使用uvicorn运行绑定的FastAPI应用实例，
        # 监听指定的host和port


if __name__ == "__main__":
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='启动WebSocket服务器和Webview窗口')
    parser.add_argument('--server', action='store_true', help='仅启动服务器')
    parser.add_argument('--host', default='0.0.0.0', help='服务器监听地址')
    parser.add_argument('--port', type=int, default=8000, help='服务器监听端口')
    parser.add_argument('--index-path', default=os.path.join("templates", "index.html"), help='网页入口文件路径')

    # 解析命令行参数
    args = parser.parse_args()

    # 检查 index 文件是否存在
    if not os.path.exists(args.index_path):
        logger.error(f"文件 {args.index_path} 不存在，无法启动服务器。")
    else:
        logger.info(
            f"服务器已启动，地址为 http://localhost:{args.port} 和 ws://localhost:{args.port}/ws")

        # 实例化WebSocketServer类
        server = WebSocketServer(host=args.host, port=args.port, index_path=args.index_path)

        if args.server:
            # 仅启动服务器
            server.start_server()
        else:
            # 启动webview窗口
            server.start_webview()
