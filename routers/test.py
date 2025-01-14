from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# 创建一个APIRouter实例，用于定义API的路由
router = APIRouter()

# 初始化Jinja2Templates实例，指定模板文件的目录
templates = Jinja2Templates(directory='templates')

# 定义根路径的GET请求处理函数
# 返回index.html模板，同时传入一个空的request对象
@router.get("/")
async def get():
    # 使用TemplateResponse方法渲染index.html模板，并传递一个空的request对象
    return templates.TemplateResponse("index.html", {"request": {}})

# 定义/test路径的GET请求处理函数
# 在控制台打印"test"，并返回"test"作为HTTP响应
@router.get("/test")
async def test():
    # 在控制台中打印 "test"
    print("test")
    # 返回 "test" 作为响应
    return "test"

# 定义/info路径的GET请求处理函数
# 接收Request对象作为参数，用于获取请求相关数据
@router.get("/info")
async def info(request: Request):
    # 下面是用于演示的变量，包含不同类型的参数
    custom_param = "这是一个自定义参数"  # 自定义字符串参数
    number_param = 42  # 整数参数
    list_param = ["item1", "item2", "item3"]  # 列表参数
    dict_param = {"key1": "value1", "key2": "value2"}  # 字典参数

    # 构造静态文件的URL，这里假设你有一个 style.css 文件在 static 目录下
    static_file_url = request.url_for('static', path='style.css')

    # 返回info.html模板，传入request对象和多个参数
    return templates.TemplateResponse("info.html", {
        "request": request,  # 传递request对象，用于模板渲染
        "custom_param": custom_param,  # 传递自定义字符串参数
        "number_param": number_param,  # 传递整数参数
        "list_param": list_param,  # 传递列表参数
        "dict_param": dict_param,  # 传递字典参数
        "static_file_url": static_file_url  # 传递静态文件的URL
    })
