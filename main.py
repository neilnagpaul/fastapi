from fastapi import FastAPI
from nicegui import ui

app = FastAPI()


@ui.page("/")
def index():
    return ui.label("Hello, world!")


ui.run_with(app)
