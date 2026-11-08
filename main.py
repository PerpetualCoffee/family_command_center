# main.py

from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/") #"/items/{id}", response_class=HTMLResponse)
async def read_root(request: Request): #(request: Request, id: str):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "Family Command Center"}
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload="True")