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


class Uploader:
    @staticmethod
    async def save_file(data: bytes, output_path: str) -> bool:
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
    async def stream_file(file, output_path: str, batch_size: int = None) -> bool:
        """
        大文件上传，以流的形式按量读取保存文件，默10m
        """
        try:
            if not batch_size:
                # 每次写入文件的数据大小，这里代表10 MiB
                batch_size = 10 * 2 ** 20

            with open(output_path, "wb") as f:  # 分批写入数据
                # 从网络文件流分批读取数据到 b'',再写入文件
                for i in iter(lambda: file.file.read(batch_size), b""):
                    f.write(i)
                return True
        except:
            return False
