from importlib import import_module
from pathlib import Path
from pkgutil import iter_modules

from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from loguru import logger

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# 缓存已导入的模块
_imported_modules = {}

def register_routers(package_name='routers'):
    package_dir = Path(__file__).resolve().parent / package_name
    logger.info(f"正在注册路由，包目录: {package_dir}")

    try:
        for (_, module_name, _) in iter_modules([str(package_dir)]):
            if module_name in _imported_modules:
                module = _imported_modules[module_name]
            else:
                module = import_module(f"{package_name}.{module_name}")
                _imported_modules[module_name] = module

            logger.debug(f"导入模块: {module_name}")

            router = getattr(module, 'router', None)
            if isinstance(router, APIRouter):
                app.include_router(router)
                logger.debug(f"已注册路由: {module_name}")
            else:
                logger.warning(f"模块 {module_name} 没有找到有效的 APIRouter 实例")
    except Exception as e:
        logger.error(f"注册路由时发生错误: {e}")

# 注册所有路由
register_routers()
