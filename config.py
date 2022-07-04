import os
from os import path

from pydantic import BaseSettings
from functools import lru_cache

from docs.description import DESCRIPTION, LICENSE_INFO, CONTACT


ROOT_PATH = os.getcwd()


class Settings(BaseSettings):
    DEV: bool = True  # 是否开发模式

    description: str = DESCRIPTION
    version: str = "v1"
    admin_email: str = "373704015@qq.com"
    items_per_user: int = 50
    license_info: dict = LICENSE_INFO
    contact: dict = CONTACT

    app_name: str = "CPS 自用FastApi脚手架"
    app_host: str = "127.0.0.1"  # 地址
    app_port: int = 4040  # 端口

    log_level: str = "debug"  # 日志等级
    log_engine: str = "loguru"  # 日志引擎

    # 常用功能开关
    enable_static: bool = True  # 开启静态服务
    enable_schedule: bool = False  # 是否开启定时任务
    enable_gzip: bool = False  # 是否开启gzip亚索
    enable_cors: bool = False  # 是否开启跨域
    enable_upload: bool = True  # 是否开启上传文件接口
    enable_swagger: bool = True  # 是否开启swagger

    # 常用目录配置
    path_log: str = path.join(ROOT_PATH, "logs")  # 日志目录
    path_static: str = path.join(ROOT_PATH, "static")
    path_upload: str = path.join(ROOT_PATH, "static", "upload")

    class Config:
        env_file = "config.ini"  # 读取失败


# settings = Settings()
# 缓存配置文件到cache，不用每次调用接口都读取文件io
@lru_cache
def get_settings():
    print("服务器初始化: ")
    return Settings()
