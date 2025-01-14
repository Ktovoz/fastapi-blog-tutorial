# 导入必要的模块
from importlib import import_module  # 动态导入模块
from pathlib import Path  # 操作文件路径
from pkgutil import iter_modules  # 遍历包中的模块

from fastapi import FastAPI, APIRouter  # 创建FastAPI应用和API路由
from fastapi.staticfiles import StaticFiles  # 提供静态文件服务
from loguru import logger  # 记录日志

# 创建FastAPI应用实例
app = FastAPI()

# 挂载静态文件目录，使得可以通过/static/访问静态资源
app.mount("/static", StaticFiles(directory="static"), name="static")

# 定义一个字典用于缓存已导入的模块，避免重复导入
_imported_modules = {}

def register_routers(package_name='routers'):
    """
    自动注册指定包下的所有API路由。

    参数:
        package_name (str): 包含API路由的包名，默认为'routers'
    """
    # 获取当前文件所在目录，并拼接上包名得到包的实际路径
    package_dir = Path(__file__).resolve().parent / package_name

    # 记录正在注册路由的日志信息
    logger.info(f"正在注册路由，包目录: {package_dir}")

    try:
        # 遍历包中的所有模块
        for (_, module_name, _) in iter_modules([str(package_dir)]):
            # 如果模块已经导入过，则直接使用缓存中的模块
            if module_name in _imported_modules:
                module = _imported_modules[module_name]
            else:
                # 否则动态导入模块并缓存
                module = import_module(f"{package_name}.{module_name}")
                _imported_modules[module_name] = module

            # 记录成功导入模块的日志信息
            logger.debug(f"导入模块: {module_name}")

            # 尝试从模块中获取名为'router'的对象
            router = getattr(module, 'router', None)

            # 如果获取到的对象是APIRouter实例，则将其注册到FastAPI应用中
            if isinstance(router, APIRouter):
                app.include_router(router)
                logger.debug(f"已注册路由: {module_name}")
            else:
                # 如果未找到有效的APIRouter实例，记录警告日志
                logger.warning(f"模块 {module_name} 没有找到有效的 APIRouter 实例")
    except Exception as e:
        # 如果发生任何异常，记录错误日志
        logger.error(f"注册路由时发生错误: {e}")

# 调用函数注册所有路由
register_routers()
