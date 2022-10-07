# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-10-07 13:40:04.574813
# @Last Modified by: CPS
# @Last Modified time: 2022-10-07 13:40:04.574813
# @file_path "D:\CPS\MyProject\Projects_Personal\cps-cli\template\fastapi\src\routers"
# @Filename "router_template.py"
# @Description: 功能描述
#
import os, sys

sys.path.append("..")

from fastapi import APIRouter, Path, HTTPException
from pathlib import Path as path
from pydantic import BaseModel, Field

router = APIRouter(
    tags=["test"],
    prefix="/test",
    responses={404: {"description": "Not found"}},
)


class PostParams(BaseModel):
    param1: str = ""
    param2: int = 0


@router.post("/post/{path_param}", description="post 请求模板", response_model=PostParams)
async def post(path_param: str = Path(), post_param: PostParams = PostParams()):
    try:
        res = post_param.dict()
        res.update({"path_param": path_param})

        return res
    except Exception as e:
        raise HTTPException(403, detail="请求失败")


@router.get("/get/{path_param}", description="get 请求模板", response_model=PostParams)
async def get(path_param: str = Path(), param1: str = "get", param2: int = 0):
    try:
        return PostParams(param1=param1, param2=param2)

    except Exception as e:
        # logger.error(str(e))
        raise HTTPException(402, detail="请求失败")
