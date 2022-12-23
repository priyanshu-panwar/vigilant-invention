"""
The asyncio.wait() function runs an iterable of awaitables objects and blocks until a specified condition.
asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)
"""
import asyncio


async def fun(message: str, result: int = 100, delay: int = 3) -> int:
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    pending = [
        fun("Hey Boy", 100, 1),
        fun("Hey Girl", 200, 2),
        fun("Hey Man", 300, 3)
    ]
    while pending:
        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
        print(done.pop().result())
    # Hey Girl
    # Hey Man
    # Hey Boy
    # 100
    # 200
    # 300

    # a, b, c = await asyncio.gather(fun("Hey Boy", 100, 1), fun("Hey Girl", 200, 2), fun("Hey Man", 300, 3))
    # print(a, b, c)
    # Hey Boy
    # Hey Girl
    # Hey Man
    # 100 200 300

asyncio.run(main())
