import requests
import time
import aiohttp
import asyncio
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def thread_fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def thread_main(urls):
    executor = ThreadPoolExecutor(max_workers=10)
    with requests.session() as session:
        params = [(session, url) for url in urls]
        results = list(executor.map(thread_fetcher, params))
        print(results)


async def coroutine_fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    async with session.get(url) as response:
        return await response.text()


async def coroutine_main(urls):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        result = await asyncio.gather(*[coroutine_fetcher(session, url) for url in urls])
        # print(result)


if __name__ == "__main__":
    urls = ["https://naver.com", "https://google.com",
            "https://instagram.com"] * 10

    google_apple_url = ["https://google.com", "https://apple.com"] * 50

    start1 = time.time()
    thread_main(google_apple_url)
    end1 = time.time()

    start2 = time.time()
    asyncio.run(coroutine_main(google_apple_url))
    end2 = time.time()

    print("멀티쓰레드(10) 환경", end="")
    print(end1 - start1)
    print("코루틴 환경", end="")
    print(end2 - start2)

# 비교 결과 멀티쓰레드(10) 보다 코루틴이 훨씬 빠름.
# 메모리 사용률도 멀티쓰레드 보다 코루틴이 훨씬 적음.
# 단, 모든 상황에서 코루틴이 월등한 것은 아님.
# 파이썬은 GIL(Global Interpreter Lock)이 적용돼 있음. 한 번에 한 개의 스레드만 유지하는 락. -> 스레드로 병렬성 연산을 하지 못함.
# 파이썬 멀티 쓰레딩은 동시성을 사용하여 io bound 코드에서 유용하게 사용할 수 있지만, 연산만 있는 cpu bound 코드에서는 GIL에 의해 원하는 결과를 얻을 수 없음.
