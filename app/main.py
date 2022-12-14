from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Path(__file__).resolve() --> 현재 파일의 경로.
# Path(__file__).resolve().parent --> 현재 파일의 상위 경로.
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

# StaticFiles = css, js등 스태틱한 파일들을 의미.
# app.mount("/static", StaticFiles(directory="static"), name="static")

# html 파일들의 위치.
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("./index.html", {"request": request, "title": "콜렉터 북북이"})


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    return templates.TemplateResponse("./index.html", {"request": request, "title": "콜렉터 북북이", "keyword": q})
