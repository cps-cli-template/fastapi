# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-07-04 16:30:54.828244
# @Last Modified by: CPS
# @Last Modified time: 2022-07-04 16:30:54.828244
# @file_path "W:\CPS\MyProject\demo\cps-cli\fastapi-template"
# @Filename "Types.py"
# @Description: 功能描述
#
import os, sys
from typing import Any

sys.path.append("..")
from os import path

from pydantic import BaseModel


class RedisOptions(BaseModel):
    url: str = "redis://127.0.0.1/0"
    host: str = "127.0.0.1"
    encoding: str = "utf-8"
    decode_responses: bool = True
    port: int = 6379
    db: int | str = 0
    max_connections: int = 100


class Res(BaseModel):
    success: bool = True
    msg: str = "请求成功"
    res: Any


class Err(Res):
    success: bool = False
    msg: str = "请求失败"


class Fileinfo(BaseModel):
    file_name: str
    file_path: str
    file_type: str
    size: str
    len: int
