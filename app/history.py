import fastapi
from .settings import app, templates, list_of_events
import fastapi.responses as responses

@app.get("/history")
async def read_history(request: fastapi.Request):
    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={"list_of_events": list_of_events}
    )