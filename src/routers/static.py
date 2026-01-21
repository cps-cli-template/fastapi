from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.config import get_settings


def init(app: FastAPI):
    config = get_settings()

    if config.static_enable:
        app.mount(
            config.static_route,
            StaticFiles(directory=config.static_path),
            name="static",
        )

    return app
