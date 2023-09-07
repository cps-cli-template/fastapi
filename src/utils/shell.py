# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2023-09-07 17:52:10.836203
# @Last Modified by: CPS
# @Last Modified time: 2023-09-07 17:52:10.836203
# @file_path "W:\CPS\MyProject\demo\cps-cli\template-fastapi\src\utils"
# @Filename "shell.py"
# @Description: 使用python调用其他二进制执行文件的工具类
#
import os, sys

sys.path.append("..")

from os import path
import subprocess
from subprocess import DEVNULL


def shell(commands: list[str]) -> bool:
    # 使用列表组合指令
    command_str = " ".join(commands)
    try:
        # res = subprocess.call(command_str)
        res = subprocess.call(command_str, stdout=DEVNULL)
        if res == 0:
            return True
        return False

    except Exception as err:
        print("err: ", err)
        return False


if __name__ == "__main__":
    from os import path

    scripts_dir = r"W:\CPS\MyProject\python-tools\gis-api\tools\arcpy_scripts"
    output_dir = r"W:/CPS/MyProject/python-tools/gis-api/static/upload/mikeio/res"

    py2_path = r"C:\Python27\ArcGIS10.2\python.exe"
    scripts = {
        "direction": "flow_direction.py",
        "speed": "flow_speed.py",
        "fishnet": "create_fishnet.py",
        "test": "test.py",
    }

    river_range = path.join(scripts_dir, "河道范围/河道范围.shp")
    point_range = path.join(output_dir, "50年一遇_fishnet.shp")

    res = shell(
        [
            py2_path,
            path.join(scripts_dir, scripts["test"]),
            "--output_shp",
            r"W:\CPS\MyProject\python-tools\gis-api\tools\arcpy_scripts\test.py",
        ]
    )
