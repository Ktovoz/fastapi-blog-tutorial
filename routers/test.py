from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates('templates')


@router.get("/")
async def get():
    return templates.TemplateResponse("index.html", {"request": {}})


@router.get("/test")
async def test():
    print("test")  # 在控制台中打印 "test"
    return "test"  # 返回 "test" 作为响应


@router.get("/info")
async def info(request: Request):
    custom_param = "这是一个自定义参数"
    number_param = 42
    list_param = ["item1", "item2", "item3"]
    dict_param = {"key1": "value1", "key2": "value2"}
    static_file_url = request.url_for('static', path='style.css')  # 假设你有一个 style.css 文件在 static 目录下
    return templates.TemplateResponse("info.html", {
        "request": request,
        "custom_param": custom_param,
        "number_param": number_param,
        "list_param": list_param,
        "dict_param": dict_param,
        "static_file_url": static_file_url
    })
