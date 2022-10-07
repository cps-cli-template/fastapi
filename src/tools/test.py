# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date:
# @Last Modified by: CPS
# @Last Modified time: 2022-05-28 17:34:32.614814
# @file_path "D:\CPS\MyProject\demo\cps-cli\cps-cli-template-fastapi\tools"
# @Filename "test.py"
# @Description: 测试用
#

from typing import *


import time


def delay(t: int = 1, msg="延时秒中"):
    for each in range(t):
        time.sleep(1)
        print(f"{msg}{('.' * ((each%3)+1))}")


if __name__ == "__main__":
    delay(5)
