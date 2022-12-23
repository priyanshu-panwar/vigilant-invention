"""
Concurrency means multiple tasks can run at the same time. The asyncio built-in package allows you to run tasks concurrently using a single thread.
First, the main thread submits tasks to a task queue.
Second, the event loop constantly monitors the task queue and runs the task until it counters I/O tasks. In this case, the event loop pauses the task and hands it over to the OS.
Third, check for the completed IO tasks. If the task is completed, the OS will notify the program. The event loop then runs the unpaused tasks.
"""
