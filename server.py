import uvicorn


# 터미널에 uvicorn app.main:app --reload 치는 대신,,
# python server.py 실행.
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)
