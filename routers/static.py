from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def init(app: FastAPI, directory: str, route: str = "/static", name: str = "static"):
    app.mount(route, StaticFiles(directory=directory), name=name)
    return app
