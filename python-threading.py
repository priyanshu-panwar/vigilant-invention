from threading import Thread
from time import sleep, perf_counter


def task():
    print("Starting Task :::: ")
    sleep(1)
    print("Done")

# startTime = perf_counter()
# t1 = Thread(target=task)
# t2 = Thread(target=task)
# t1.start()
# t2.start()
# t1.join() # wait for the thread to terminate
# t2.join()
# endTime = perf_counter()

# print("Execution Time = ", (endTime-startTime), " seconds")
# Starting Task ::::
# Starting Task ::::
# Execution Time =  0.0014041000395081937  seconds
# Done
# Done


def newTask(id):
    print(f"Starting {id} Task ::::")
    sleep(1)
    print(f"Done {id} ")


startTime = perf_counter()

threads = []
for i in range(1, 11):
    thread = Thread(target=newTask, args=(i, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

endTime = perf_counter()

print("Execution Time = ", (endTime-startTime), " seconds")

# Starting 1 Task ::::
# Starting 2 Task ::::
# Starting 3 Task ::::
# Starting 4 Task ::::
# Starting 5 Task ::::
# Starting 6 Task ::::
# Starting 7 Task ::::
# Starting 8 Task ::::
# Starting 9 Task ::::
# Starting 10 Task ::::
# Done 10
# Done 7
# Done 6
# Done 4
# Done 3
# Done 9
# Done 5
# Done 1
# Done 2
# Done 8
# Execution Time =  1.0187656999914907  seconds
