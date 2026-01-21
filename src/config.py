import os
from os import path

from pydantic import BaseSettings
from functools import lru_cache

import src.Types as T
from src.docs.description import DESCRIPTION, LICENSE_INFO, CONTACT
from src.utils.ip import get_inside_ip, get_computer_name

ROOT_PATH = os.getcwd()
STATIC_PATH = ""


class Settings(BaseSettings):
    DEV: bool = True  # 是否开发模式

    app_name: str = "CPS 自用FastApi脚手架"
    app_host: str = "0.0.0.0"  # 地址
    app_port: int = 4040  # 端口
    app_version: str = "v1"
    app_description: str = DESCRIPTION
    app_contact: dict = CONTACT
    app_license_info: dict = LICENSE_INFO
    app_inner_ip: str = get_inside_ip()
    app_computer_name: str = get_computer_name()

    # 预置中间件
    middleware_cors_enable: bool = False  # 跨域
    middleware_gzip_enable: bool = False  # gzip压缩（尽量使用nginx的）
    middleware_http_time_count_enable: bool = True  # 计算请求处理时间

    # 日志相关
    log_enable: bool = True
    log_level: str = "debug"  # 日志等级
    log_engine: str = "loguru"  # 日志引擎
    log_path: str = path.join(ROOT_PATH, "logs")  # 日志目录

    # 常用功能开关
    enable_schedule: bool = False  # 是否开启定时任务
    enable_gzip: bool = False  # 是否开启gzip亚索
    enable_cors: bool = False  # 是否开启跨域
    enable_upload: bool = True  # 是否开启上传文件接口

    # api 文档配置
    swagger_enable: bool = True
    swagger_route: str = "/docs"
    redoc_enable: bool = True
    redoc_route: str = "/redoc"

    # Redis 配置
    redis_enable: bool = False
    redis_options: T.RedisOptions = T.RedisOptions()

    # 静态目录配置
    static_enable: bool = True  # 开启静态服务
    static_path: str = path.join(ROOT_PATH, "static")
    static_route: str = "/static"

    # 上传配置
    upload_enable: bool = True
    upload_path: str = path.join(ROOT_PATH, "static", "upload")

    class Config:
        env_file: str = path.join(ROOT_PATH, "config.ini")  # 读取失败


# settings = Settings()
# 缓存配置文件到cache，不用每次调用接口都读取文件io
@lru_cache
def get_settings() -> Settings:
    print("服务器根目录: ", os.getcwd())
    return Settings()
