# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-07-04 16:13:55.348149
# @Last Modified by: CPS
# @Last Modified time: 2022-07-04 16:13:55.348149
# @file_path "W:\CPS\MyProject\demo\cps-cli\fastapi-template\tools"
# @Filename "upload_small_file.py"
# @Description: 功能描述
#
import aiofiles
import hashlib
import os, time

from os import path
from fastapi import UploadFile
from loguru import logger


class Uploader:
    @staticmethod
    def upload_file_checker(upload_file: str) -> bool:
        name, ext = path.splitext(path.basename(upload_file))

        if os.path.exists(upload_file):
            # 判断是否存在md5文件
            md5_file_name = path.join(path.dirname(upload_file), f".{name}.md5")

    @staticmethod
    def get_file_md5_sync(file_name: str, read_size: int = 10 * 2**20) -> str:
        """
        获取文件的md5值

        - param file_name               :{str} {description}
        - param read_size=10*2**20 :{int} 每次写入文件的数据大小，第一个10表示: 10 MiB

        """

        md5_obj = hashlib.md5()

        with open(file_name, "rb") as file:
            finished = True
            while finished:
                data = file.read(read_size)
                md5_obj.update(data)

                if len(data) != read_size:
                    break

            return md5_obj.hexdigest()

    @staticmethod
    async def get_file_md5(file_name: str) -> str:
        # 每次写入文件的数据大小，第一个10表示: 10 MiB
        read_size = 10 * 2**20
        md5_obj = hashlib.md5()

        async with open(file_name, "rb") as file:
            # 从网络文件流分批读取数据到 b'',再写入文件
            finished = True
            while finished:
                data = await file.read(read_size)
                md5_obj.update(data)

                if len(data) != read_size:
                    break

            return md5_obj.hexdigest()

    @staticmethod
    async def small_file(data: bytes, output_path: str) -> bool:
        """
        小文件上传，文件首先保存到内存，然后再到本地
        """
        try:
            with open(output_path, "wb") as f:
                f.write(data)
                return True
        except:
            return False

    @staticmethod
    def stream_file(file, output_path: str, chunk_size: int = 10 * 2**20) -> bool:
        """
        大文件上传，以流的形式按量读取保存文件，默10m
        """
        try:
            with open(output_path, "wb") as f:  # 分批写入数据
                # 从网络文件流分批读取数据到 b'',再写入文件
                for i in iter(lambda: file.file.read(chunk_size), b""):
                    f.write(i)
                return True
        except:
            return False

    @staticmethod
    async def stream_file_async(
        file: UploadFile, output_path: str, chunk_size: int = 20 * 2**20
    ) -> bool:
        """
        @Description 【异步】大文件上传，以流的形式按量读取保存文件，默10m

        - param file                    :{param} {description}
        - param output_path             :{str}   {description}
        - param chunk_size=10*2**20 :{int}   每次写入文件的数据大小，这里代表20 MiB

        @returns `{ bool}` {description}

        """
        try:
            # 分批写入数据
            async with aiofiles.open(output_path, "wb") as f:

                # 从网络文件流分批读取数据到 b'',再写入文件
                finished = True
                while finished:
                    data = await file.read(chunk_size)
                    await f.write(data)

                    if len(data) != chunk_size:
                        finished = False
                        break

                return True

        except Exception as e:
            logger.debug(f"stream_file_async fail: {e}")
            return False

    @staticmethod
    def stream_file_md5(
        file: UploadFile, output_dir: str, batch_size: int = None
    ) -> str:
        """
        文件上传，以流的形式按量读取保存文件，默10m，且最终以md5命名该文件
        """

        # 检查文件是否存在
        md5_obj = hashlib.md5()
        output_path = path.join(output_dir, str(int(time.time())))
        name, ext = path.splitext(file.filename)
        try:
            if not batch_size:
                # 每次写入文件的数据大小，这里代表10 MiB
                batch_size = 10 * 2**20

            with open(output_path, "wb") as f:  # 分批写入数据
                # 从网络文件流分批读取数据到 b'',再写入文件
                for i in iter(lambda: file.file.read(batch_size), b""):
                    f.write(i)
                    md5_obj.update(i)

            output_path_md5 = path.join(output_dir, f"{md5_obj.hexdigest()}{ext}")
            os.rename(output_path, output_path_md5)
            return output_path_md5

        except Exception as e:
            print("stream_file_md5 fial: ", e)
            return ""
