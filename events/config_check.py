# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-08-24 09:47:53.357509
# @Last Modified by: CPS
# @Last Modified time: 2022-08-24 09:43:37.592153
# @file_path "W:\CPS\MyProject\demo\cps-cli\template-fastapi\events"
# @Filename "config_check.py"
# @Description: 功能描述
#
if __name__ == "__main__":
    import sys

    sys.path.append("..")
    sys.path.append("../../")

import os
from os import path

from loguru import logger
from config import Settings


def check_path_and_make(config: Settings):
    """
    检查所有config里面以_path结尾的目录，如果不存在则创建
    """
    config_dict = config.dict()
    config_keys = tuple(config_dict.keys())

    for key in config_keys:
        if key.endswith("_path"):
            target = config_dict[key]
            logger.debug(f"检查目录: {key} => {target}")

            # 检查目录
            if path.exists(target):
                continue

            # 递归创建目录创建目录
            os.makedirs(target)
            logger.info(f"创建不存在的目录: {target}")
