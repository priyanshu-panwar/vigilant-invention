"""
- run multiple async operations and get the results once they are complete.
- asyncio.gather(*aws, return_exceptions=False)
    - aws : awaitable objects
    - return_exception = True : doesn't interrupt (returns exception in result)
    - return_exception = False : interrupts running tasks
"""


import asyncio
import random
import time


async def goodNight1():
    wait = random.randint(0, 3)
    await asyncio.sleep(wait)
    print("Task 1 Completed")


async def goodNight2():
    wait = random.randint(0, 3)
    await asyncio.sleep(wait)
    # raise Exception("I am exception")
    print("Task 2 Completed")


async def goodNight3():
    wait = random.randint(0, 3)
    await asyncio.sleep(wait)
    print("Task 3 Completed")


async def goodNight():
    wait = random.randint(0, 3)
    await asyncio.sleep(wait)
    print("Task Completed")


async def main():
    t1 = time.time()
    for _ in range(2):
        # await asyncio.gather(goodNight1(), goodNight2(), goodNight3(), return_exceptions=True)
        await asyncio.gather(goodNight(), goodNight(), goodNight(), return_exceptions=True)
        # await goodNight1()
        # await goodNight2()
        # await goodNight3()
        print("-----------------")
    t2 = time.time()
    print("Time Taken = ", (t2-t1))

asyncio.run(main())
