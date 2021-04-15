import asyncio
from random import random
from asyncio.tasks import gather
import time

# When using asyncio.sleep(), each worker surrenders control while sleeping
# When using time.sleep(), each worker hogs the running thread
async def long_running_task(time_to_sleep):
    #print(f"begin sleep for {time_to_sleep}")
    await asyncio.sleep(time_to_sleep)
    #time.sleep(time_to_sleep)
    #print(f"Awake from {time_to_sleep}")444
    return f"{time_to_sleep:.2f}"

# Change the number of workers to see the impact of using async
# If using time.sleep() in long_running_task(), keep the number of workers low 
async def main():
    workers = 500
    times = [random() for x in range(workers)]
    tasks = [asyncio.create_task(long_running_task(x)) for x in times]
    return (await asyncio.gather(*tasks), f'Total time slept: {sum(times):.2f}')

# This function starts the async thread and waits for completion.
# Please note that the 
def run_the_async():
    result = asyncio.run(main())
    print(f"from here: {result}")

if __name__ == '__main__':
    s = time.perf_counter()
    run_the_async()
    elapsed = time.perf_counter() - s
    print(f"Execution time: {elapsed:0.2f} seconds.")