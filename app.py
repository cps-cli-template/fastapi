# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date:
# @Last Modified by: CPS
# @Last Modified time: 2022-05-26 20:55:54.506017
# @file_path "D:\CPS\MyProject\外接项目\PSD文件解析\psd-tools"
# @Filename "app.py"
# @Description: 功能描述
#
from typing import *
from fastapi import FastAPI, Header, Query
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)


app = FastAPI(docs_url=None, redoc_url=None, title="Psd文件解析接口")
app.mount("/static", StaticFiles(directory="static"), name="static")

# 将 /docs 重置到离线
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


# swagger 验证问题
@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


# redoc 重置到离线
@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )


@app.get("/")
async def root():
    return {}


@app.get("/test/{item}", tags=["test"])
async def test(item: Any):
    return {"input": item}


@app.get("/exit", tags=["test"])
async def Exit():
    exit()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=4040, log_level="info", reload=True)
