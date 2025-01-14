import datetime
import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from loguru import logger

router = APIRouter()

command_handlers = {}


def register_command(command):
    def decorator(func):
        logger.debug(f"正在注册命令 '{command}'，处理函数为 '{func.__name__}'")
        command_handlers[command] = func
        # 修改这里，只记录函数名而不是函数对象
        logger.info(
            f"当前注册的命令处理器: {', '.join(f'{cmd}: {handler.__name__}' for cmd, handler in command_handlers.items())}")
        return func

    return decorator


@register_command('echo')
async def echo_handler(message, websocket):
    logger.debug(f"echo_handler 被调用，消息为: {message}")
    try:
        await websocket.send_text(f"回显: {message}")
    except Exception as e:
        logger.error(f"echo_handler 中发生错误: {e}")


@register_command('custom')
async def custom_handler(message, websocket):
    logger.debug(f"custom_handler 被调用，消息为: {message}")
    try:
        await websocket.send_text(f"自定义回显: {message}")
    except Exception as e:
        logger.error(f"custom_handler 中发生错误: {e}")


@register_command('time')
async def time_handler(message, websocket):
    logger.debug(f"time_handler 被调用，消息为: {message}")
    try:
        now = datetime.datetime.now().isoformat()
        await websocket.send_text(f"服务器时间是 {now}")
    except Exception as e:
        logger.error(f"time_handler 中发生错误: {e}")


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.info("正在处理连接")
    try:
        while True:
            data = await websocket.receive_text()
            # 假设消息是以JSON格式发送的
            request = json.loads(data)
            command = request.get('command')
            data = request.get('data', '')
            if command not in command_handlers:
                logger.warning(f"非法命令: {command}")
                await websocket.send_text("非法命令")
                continue
            logger.debug(f"解析命令: {command}, 数据: {data}")

            if command in command_handlers:
                logger.debug(f"找到命令 '{command}'，调用处理函数 '{command_handlers[command].__name__}'")
                await command_handlers[command](data, websocket)
            else:
                logger.warning(f"未知命令: {command}")
                await websocket.send_text(f"未知命令: {command}")
    except json.JSONDecodeError:
        logger.error(f"无法解码JSON消息: {data}")
        await websocket.send_text("无效的JSON格式")
    except WebSocketDisconnect:
        logger.info("客户端已断开连接")
    except Exception as e:
        logger.error(f"处理消息时发生错误: {data}, 错误: {e}")
