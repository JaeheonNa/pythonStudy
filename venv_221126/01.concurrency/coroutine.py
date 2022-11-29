import requests
import time
import aiohttp
import asyncio

# 서브루틴 시  11.43초.
# 코루틴 시 90% 감소.


def subroutine_fetcher(session, url):
    with session.get(url) as response:
        return response.text


def subroutine_main(urls):
    with requests.session() as session:
        result = [subroutine_fetcher(session, url) for url in urls]
        print(result)


async def coroutine_fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def coroutine_main(urls):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        result = await asyncio.gather(*[coroutine_fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    urls = ["https://naver.com", "https://google.com",
            "https://instagram.com"] * 10

    # start = time.time()
    # subroutine_main(urls)
    # end = time.time()
    # print(end-start)

    start = time.time()
    asyncio.run(coroutine_main(urls))
    end = time.time()
    print(end-start)
