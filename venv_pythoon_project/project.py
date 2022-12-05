# ASGI : 웹서버와 파이썬 기반의 프로그램을 연결해주는 미들웨어
# 톰캣은 Java로 만들어진 WAS임.
# 파이썬으로 만들어진 프로그램을 돌릴 수 없음.
# 톰캣이 파이썬 코드를 읽지 못하기 때문.
# 톰캣으로 파이썬 프로그램을 돌릴 수 있도록 도와주는 미들웨어가 필요.
# 그게 바로 ASGI. 톰캣과 파이썬 프로그램 사이의 인터페이스라고 보면 됨.

# Uvicorn : ASGI의 구현체

# fastAPI 설치
# pip install fastapi

# uvicorn 설치
# pip install uvicorn[standard]

# 실행
# uvicorn app.main:app --reload
# 유비콘으로 app 폴더 밑에 main 파일의 app 객체를 실행. 코드가 수정됐을 경우 재시작.
