from fastapi import FastAPI, Form, HTTPException
import fastapi
import fastapi.responses as responses
from .settings import app, TEMPLATES_PATH, templates, list_of_events
import typing
import app.chatGPT as chatGPT 
import markdown #? Это библиотека которая из текста с Markdown-разметкой делает в html
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import HTMLResponse

@app.get("/")
async def root(request: fastapi.Request):
    try:
        return templates.TemplateResponse(
            request=request,
            name="home.html",
            context={"message": "///"}
        )
    except Exception as e:
        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={"message": "///"}
        )

@app.post("/")
async def rootPost(
    request: fastapi.Request,
    name: typing.Annotated[str, Form()]
):  
    response = chatGPT.get_chat_response(name)
    list_of_events.append([name, response])
    response_html = markdown.markdown(response, extensions=["extra"])
    return templates.TemplateResponse("home.html", {"request": request, "message": response_html})



@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: fastapi.Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "message": "Страница не найдена!"},
            status_code=404
        )
    return templates.TemplateResponse(
        "error.html",
        {"request": request, "message": "Произошла ошибка!"},
        status_code=exc.status_code
    )