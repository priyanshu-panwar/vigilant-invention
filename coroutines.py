"""
- coroutine is a regular function with the ability to pause its execution when encountering an operation that will take long time to complete.
- while coroutine waits for long running operation, you can run other code.
- async : creates coroutine
- await : pauses coroutine
"""

import asyncio
import random
import time


async def square(n: int) -> int:
    wait = random.randint(0, 3)
    await asyncio.sleep(wait)
    return n*n


async def fun() -> int:
    print("Let's have fun!")
    await asyncio.sleep(3)
    return 100


async def main() -> None:
    start = time.time()
    # x = await square(10)
    # print("Square of 10 = ", x)
    # x = await square(5)
    # print("Square of 5 = ", x)
    x = await fun()
    print(x)
    end = time.time()
    print("Execution Time = ", (end-start))

asyncio.run(main())
