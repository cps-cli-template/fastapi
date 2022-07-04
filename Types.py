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

sys.path.append('..')
from os import path

from pydantic import BaseModel


class Res(BaseModel):
    success: bool = True
    msg: str = "请求成功"
    res: Any


class Err(Res):
    success: bool = False
    msg: str = "请求失败"
