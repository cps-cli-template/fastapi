import sys

from loguru import logger
from starlette.routing import Match
from fastapi import FastAPI, Request


def init(app: FastAPI):
    @app.middleware("http")
    async def log_middle(request: Request, call_next):
        logger.info(f"{request.method} {request.url}")
        routes = request.app.router.routes
        logger.debug("Params:")
        for route in routes:
            match, scope = route.matches(request)
            if match == Match.FULL:
                for name, value in scope["path_params"].items():
                    logger.debug(f"\t{name}: {value}")
        logger.debug("Headers:")
        for name, value in request.headers.items():
            logger.debug(f"\t{name}: {value}")

        response = await call_next(request)
        return response
