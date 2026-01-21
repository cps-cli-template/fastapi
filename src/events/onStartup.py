# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-07-17 17:41:05.028133
# @Last Modified by: CPS
# @Last Modified time: 2022-07-17 17:41:05.028133
# @file_path "D:\CPS\MyProject\Projects_Personal\cps-cli\cps-cli-template-fastapi\events"
# @Filename "startup.py"
# @Description: 功能描述
#

from fastapi import __version__


from src.config import Settings
from src.events import config_check
from src.utils.helper import print_dict
from src.utils.log import logger


def print_info(config: Settings):
    logger.info(f"app fastAPI ver: {__version__}")

    logger.info(f"app 运行成功，访问限制为: {config.app_host}")
    logger.info(f"app 运行成功，内网访问地址1: http://{config.app_inner_ip}:{config.app_port}")
    logger.info(f"app 运行成功，内网访问地址2: http://{config.app_computer_name}:{config.app_port}")


def init(config: Settings):
    print("on_start_up: ")
    # 检查目录
    config_check.check_path_and_make(config)

    # 检查FastAPI版本
    print_info(config)
