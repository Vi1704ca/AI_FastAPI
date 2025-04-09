from fastapi import FastAPI
import fastapi.templating as templating
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

TEMPLATES_PATH = os.path.abspath(os.path.join(__file__, "..", "..", "templates"))
STATIC_PATH = os.path.abspath(os.path.join(__file__, "..", "..", "static"))

templates = templating.Jinja2Templates(directory=TEMPLATES_PATH)

app_static = StaticFiles(directory=STATIC_PATH)

app.mount (
    path="/static",
    app=app_static,
    name="static"
)

list_of_events = []

TOKEN_API = "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"