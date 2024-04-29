# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2024-04-25 09:20:36.814376
# @Last Modified by: CPS
# @Last Modified time: 2024-04-25 09:20:36.814376
# @file_path "W:\CPS\MyProject\demo\cps-cli\template-fastapi\src\utils"
# @Filename "ip.py"
# @Description: 一些获取当前网络变量的函数
#


import os, sys
import socket


def get_inside_ip() -> str:
    """获取内网IP"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        return str(ip)

    except Exception as e:
        print("获取失败")
        s.close()
        return "127.0.0.1"


def get_computer_name() -> str:
    """获取计算机名称"""
    return socket.gethostname()
