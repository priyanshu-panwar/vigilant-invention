"""
- A task is a wrapper of a coroutine that schedules the coroutine to run on the event loop as soon as possible.
- The scheduling and execution occur in a non-blocking manner. In other words, you can create a task and execute other code instantly while the task is running.
- Notice that the task is different from the await keyword that blocks the entire coroutine until the operation completes with a result.
- It’s important that you can create multiple tasks and schedule them to run instantly on the event loop at the same time.
- To create a task, you pass a coroutine to the create_task() function of the asyncio package. The create_task() function returns a Task object.
"""

import asyncio
import time


async def callApi(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def showMessage():
    for _ in range(3):
        await asyncio.sleep(1)
        print('API call is in progress...')


async def main():
    start = time.perf_counter()
    messageTask = asyncio.create_task(showMessage())
    task1 = asyncio.create_task(callApi("Orange", 30))
    task2 = asyncio.create_task(callApi("Mango", 40))
    price = await task1
    print(price)
    print("Hey")
    price = await task2
    print(price)
    await messageTask
    end = time.perf_counter()
    print(f"Execution Time : {round(end-start, 0)}")

asyncio.run(main())

# Orange
# Mango
# API call is in progress...
# API call is in progress...
# API call is in progress...
# 30
# Hey
# 40
# Execution Time : 3.0
