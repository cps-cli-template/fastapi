# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-10-06 15:45:45.529299
# @Last Modified by: CPS
# @Last Modified time: 2022-10-06 15:45:45.529299
# @file_path "D:\CPS\MyProject\Projects_Personal\cps-cli\template\fastapi\src\utils"
# @Filename "log.py"
# @Description: 功能描述
#
import os, sys

sys.path.append("..")

import loguru
from typing import Any


class Logger:
    def __init__(self):
        self.logger = loguru.logger
        self.catch = loguru.logger.catch

    def __msg(self, *msg: list[Any]) -> str:
        return "".join(map(str, msg))

    def info(self, *msg: list[Any]):
        self.logger.info(self.__msg(msg))

    def warning(self, *msg: list[Any]):
        self.logger.warning(self.__msg(msg))

    def error(self, *msg: list[Any]):
        self.logger.error(self.__msg(msg))

    def debug(self, *msg: list[Any]):
        self.logger.debug(self.__msg(msg))


logger = Logger()
