import time, aiohttp, asyncio
from aiohttp import web


async def multi_request(urls: list[str], data_list: list = list()) -> list:
    """
    @Description {description}

    - param urls             :{param} {description}
    - param data_list=list() :{list}  {description}

    @returns `{ list}` {description}
    @example
    ```py

    urls = ['https://1', 'https://2']
    params = []
    r = multi_request()
    asyncio.run()

    ```

    """
    tasks = []

    async def fetch(session, url):
        async with session.get(url) as response:
            if response.status != 200:
                response.raise_for_status()
            data = await response.text()
            return data

    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

    return responses


async def main(urls):
    start = time.time()
    res = await multi_request(urls)
    end = time.time()

    print('总耗时: ', round(end - start, 3))
    print(res)


if __name__ == '__main__':
    urls = ['http://localhost:4040/test/get/{0}'.format(e) for e in range(10)]

    task = main(urls)
    asyncio.run(task)
