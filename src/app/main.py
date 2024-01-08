"""File Main"""
from fastapi import FastAPI

from .api import controller


app = FastAPI()

app.include_router(controller.router, prefix="/v1", tags={"controller"})
