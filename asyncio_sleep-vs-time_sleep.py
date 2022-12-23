"""
time.sleep() - blocks entire execution of the script
asyncio.sleep() - non blocking, ask event loop to run something else while await finishes execution
"""


import asyncio
import time


async def timeFun1():
    for _ in range(0, 3):
        print('Test1')
        time.sleep(1)


async def timeFun2():
    for _ in range(0, 3):
        print('Test2')
        time.sleep(1)


async def asyncFun1():
    for _ in range(0, 3):
        print('Test1')
        await asyncio.sleep(1)


async def asyncFun2():
    for _ in range(0, 3):
        print('Test2')
        await asyncio.sleep(1)


async def main():
    # await asyncio.gather(asyncFun1(), asyncFun2())
    await asyncio.gather(timeFun1(), timeFun2())

start = time.time()
asyncio.run(main())
end = time.time()
print("Execution Time = ", (end-start))
# asyncio.sleep() -  Took 3 seconds
# time.sleep() - Took 6 seconds
