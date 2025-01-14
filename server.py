import os
from loguru import logger
from main import WebSocketServer




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
        # server.start_server_and_web()  # 如果需要同时启动服务器和webview，请取消此行注释
        server.start_server()  # 仅启动服务器