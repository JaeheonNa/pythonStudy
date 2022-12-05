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


# response_class=HTMLResponse --> 응답할 때 응답 값의 타입을 HTMLResponse로 하겠다는 의미.
# {id} --> 다이나믹 URL. {id} 값이 라우터(함수)의 인자로 넘어감. FastAPI는 Type을 힌트로 보고 매핑해줌.
# requeset:Request --> 요청 관련 정보. 라우터(함수)의 인자와 templateResponsec 인자에 반드시 있어야함.
@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("./items.html", {"request": request, "id": id, "data": "Hola Fast API"})
