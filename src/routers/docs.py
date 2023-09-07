# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2022-05-27 16:33:27.684089
# @Last Modified by: CPS
# @Last Modified time: 2022-05-27 16:33:27.685083
# @file_path "W:\CPS\MyProject\python-tools\ps-tools\src\routers"
# @Filename "docs.py"
# @Description: 功能描述
#

from fastapi import FastAPI, APIRouter

from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

from config import get_settings

router = APIRouter()


def init(app: FastAPI, swagger_route: str = "/docs", redoc_route: str = "/redoc"):
    config = get_settings()

    if not config.DEV:
        return

    if not config.swagger_enable:
        return

    swagger_ui_oauth2_redirect_url = app.swagger_ui_oauth2_redirect_url

    # 将 /docs 重置到离线
    @router.get(config.swagger_route, include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=swagger_ui_oauth2_redirect_url,
            swagger_js_url="/static/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger-ui.css",
        )

    # swagger 验证问题
    @router.get(swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()

    # redoc 重置到离线
    @router.get(config.redoc_route, include_in_schema=False)
    async def redoc_html():
        return get_redoc_html(
            openapi_url=app.openapi_url,
            title=app.title + " - ReDoc",
            redoc_js_url="/static/redoc.standalone.js",
        )

    app.include_router(router)

    return app


if __name__ == "__main__":
    pass
