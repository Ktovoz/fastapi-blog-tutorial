import os
import threading
import time

import uvicorn
import webview
from loguru import logger

from app import app


class WebSocketServer:
    def __init__(self, **kwargs):
        self.host = kwargs.get('host', '0.0.0.0')
        self.port = kwargs.get('port', 8000)
        self.index_path = kwargs.get('index_path', os.path.join("templates", "index.html"))
        self.app = app

    def start_webview(self):
        webview.create_window('Web Socket Example', str(self.index_path), width=1000, height=800, resizable=True)
        webview.start()

    def start_server(self):
        uvicorn.run(self.app, host=self.host, port=self.port)

    def start_server_and_web(self):
        # 启动FastAPI服务器
        server_thread = threading.Thread(target=self.start_server)
        server_thread.daemon = True
        server_thread.start()
        time.sleep(1)
        # 启动webview窗口
        self.start_webview()


if __name__ == "__main__":
    # 配置参数
    config = {
        "host": "0.0.0.0",
        "port": 8000,
        "index_path": os.path.join("templates", "index.html")
    }

    # 检查 index 文件是否存在
    if not os.path.exists(config['index_path']):
        logger.error(f"文件 {config['index_path']} 不存在，无法启动服务器。")
    else:
        logger.info(
            f"服务器已启动，地址为 http://localhost:{config['port']} 和 ws://localhost:{config['port']}/ws")

        # 实例化WebSocketServer类
        server = WebSocketServer(**config)

        # 启动服务器和webview
        # server.start_server_and_web()
        server.start_server()
