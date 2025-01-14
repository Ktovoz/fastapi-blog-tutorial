# 导入必要的库和模块
import datetime
import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from loguru import logger

# 创建一个API路由实例，用于定义WebSocket端点
router = APIRouter()

# 定义一个字典来存储命令及其对应的处理函数
command_handlers = {}

def register_command(command):
    """
    注册命令处理器的装饰器函数。

    参数:
        command (str): 要注册的命令名称。

    返回:
        decorator (function): 实际的装饰器函数，用于包装命令处理函数。
    """
    def decorator(func):
        # 记录正在注册的命令及其处理函数名
        logger.debug(f"正在注册命令 '{command}'，处理函数为 '{func.__name__}'")
        command_handlers[command] = func

        # 记录当前所有已注册的命令处理器
        logger.info(
            f"当前注册的命令处理器: {', '.join(f'{cmd}: {handler.__name__}' for cmd, handler in command_handlers.items())}")

        return func  # 返回原始函数，不改变其行为

    return decorator


@register_command('echo')
async def echo_handler(message, websocket):
    """
    处理 'echo' 命令的异步函数。

    参数:
        message (str): 收到的消息内容。
        websocket (WebSocket): WebSocket连接对象。
    """
    logger.debug(f"echo_handler 被调用，消息为: {message}")
    try:
        # 向客户端发送回显消息
        await websocket.send_text(f"回显: {message}")
    except Exception as e:
        # 捕获并记录任何异常
        logger.error(f"echo_handler 中发生错误: {e}")


@register_command('custom')
async def custom_handler(message, websocket):
    """
    处理 'custom' 命令的异步函数。

    参数:
        message (str): 收到的消息内容。
        websocket (WebSocket): WebSocket连接对象。
    """
    logger.debug(f"custom_handler 被调用，消息为: {message}")
    try:
        # 向客户端发送自定义回显消息
        await websocket.send_text(f"自定义回显: {message}")
    except Exception as e:
        # 捕获并记录任何异常
        logger.error(f"custom_handler 中发生错误: {e}")


@register_command('time')
async def time_handler(message, websocket):
    """
    处理 'time' 命令的异步函数。

    参数:
        message (str): 收到的消息内容（本例中未使用）。
        websocket (WebSocket): WebSocket连接对象。
    """
    logger.debug(f"time_handler 被调用，消息为: {message}")
    try:
        # 获取当前时间并格式化为ISO8601字符串
        now = datetime.datetime.now().isoformat()
        # 向客户端发送服务器时间
        await websocket.send_text(f"服务器时间是 {now}")
    except Exception as e:
        # 捕获并记录任何异常
        logger.error(f"time_handler 中发生错误: {e}")


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket端点的主处理函数。

    参数:
        websocket (WebSocket): WebSocket连接对象。
    """
    await websocket.accept()  # 接受WebSocket连接
    logger.info("正在处理连接")

    try:
        while True:
            # 接收来自客户端的消息
            data = await websocket.receive_text()

            # 尝试将接收到的数据解析为JSON格式
            try:
                request = json.loads(data)
            except json.JSONDecodeError:
                logger.error(f"无法解码JSON消息: {data}")
                await websocket.send_text("无效的JSON格式")
                continue

            # 提取命令和数据
            command = request.get('command')
            data = request.get('data', '')

            # 检查命令是否合法
            if command not in command_handlers:
                logger.warning(f"非法命令: {command}")
                await websocket.send_text("非法命令")
                continue

            # 记录解析出的命令和数据
            logger.debug(f"解析命令: {command}, 数据: {data}")

            # 查找并调用相应的命令处理函数
            if command in command_handlers:
                logger.debug(f"找到命令 '{command}'，调用处理函数 '{command_handlers[command].__name__}'")
                await command_handlers[command](data, websocket)
            else:
                logger.warning(f"未知命令: {command}")
                await websocket.send_text(f"未知命令: {command}")

    except WebSocketDisconnect:
        # 处理客户端断开连接的情况
        logger.info("客户端已断开连接")
    except Exception as e:
        # 捕获并记录其他任何异常
        logger.error(f"处理消息时发生错误: {data}, 错误: {e}")
