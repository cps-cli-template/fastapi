from pydantic import BaseSettings
from functools import lru_cache
from os import path

description = """自用的脚手架，集成一些<b>常用</b>的功能：
<br> 1、离线的swagger和redoc
<br> 2、静态服务
<br> 3、文件上传、下载
<br> 4、JWT权鉴
<br> 5、定时任务
<br> 6、基本的业务功能约束
<br> 7、一键开启gzip
<br> 8、一键开启跨域
<br>
<br> PS: 自己用的爽才是最关键的，fastapi的类型提示让项目无论过了多久都能快速回忆迭代更新，
<br> 真的比很多老牌web框架要舒服，再集成上一些常用功能，爽~~~
"""
contact = {
    "name": "Capsion / CPS",
    "url": "http://www.capsion.top",
    "email": "373704015@qq.com",
}

license_info = {
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
}

ROOT_PATH = r""


class Settings(BaseSettings):
    DEV: bool = True  # 是否开发模式
    app_name: str = "CPS 自用FastApi脚手架"
    description: str = description
    version: str = "v1"
    admin_email: str = "373704015@qq.com"
    items_per_user: int = 50
    license_info: dict = license_info
    contact: dict = contact

    host: str = "127.0.0.1"  # 地址
    port: int = 4040  # 端口
    log_level: str = "debug"  # 日志等级
    log_engine: str = "loguru"  # 日志引擎

    # 常用功能开关
    static_enable: bool = True  # 开启静态服务
    schedule_enable: bool = False  # 是否开启定时任务
    gzip_enable: bool = False  # 是否开启gzip亚索
    cors_enable: bool = False  # 是否开启跨域
    upload_enable: bool = False  # 是否开启上传文件接口
    swagger_enable: bool = True  # 是否开启swagger

    log_dir: str = "logs"

    upload_path: str = (
        r"D:\CPS\MyProject\demo\cps-cli\cps-cli-template-fastapi\test\upload"
    )

    class Config:
        env_file = ".env"  # 读取失败


# settings = Settings()
# 缓存配置文件到cache，不用每次调用接口都读取文件io
@lru_cache
def get_settings():
    print("创建setting对象")
    return Settings()
