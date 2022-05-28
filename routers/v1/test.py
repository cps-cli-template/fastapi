# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-05-28 09:35:31.583430
# @Last Modified by: CPS
# @Last Modified time: 2022-05-28 09:35:31.583430
# @file_path "D:\CPS\MyProject\demo\cps-cli\cps-cli-template-fastapi\routers\v1"
# @Filename "test.py"
# @Description: 功能描述
#

from typing import *
from fastapi import APIRouter, HTTPException, Query, Path
from pydantic import BaseModel, Field

router = APIRouter(
    tags=["test", "v1"], prefix="/v1", responses={404: {"description": "Not found"}}
)


Req_example = {"request_str": "test_str", "request_int": 123}


class Req(BaseModel):
    request_str: str = Field(
        default="string", title="请求字符串", max_length=32, min_length=3
    )
    request_int: int = Field(title="请求的字符串", gt=33, lt=12)

    class Config:
        schema_extra: Req_example


@router.get("/", description="测试接口get")
async def test_get(test_params: str = None):
    return {"msg": "api v1 test", "input_param": test_params}


@router.get("/test", description="测试接口get")
async def test_get(test_params: str = Query(default=None)):
    return {"test_params": test_params}


@router.post("/test", description="post")
async def test_post(req: Req):
    return {"test_params": Req.request_str}
