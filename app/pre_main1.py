from typing import Optional
from fastapi import FastAPI

app = FastAPI()
# ip:port/docs --> swagger 처럼 문서 보여줌. FastAPI 내장 기능.


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello")
def read_fastapi_hello():
    return {"Hello": "FastAPI"}


# {item_id} --> 동적 라우팅. 해당 값을 인자로 받음. /item/123?q=hello --> item_id = 123, q=hello로 찍힘.
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
