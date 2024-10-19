import time
import asyncio

async def producer(queue, id):
    counter = 0
    start_time = time.perf_counter()
    while counter <= 2:
        await queue.put(f"{id}-{counter}")
        print(f"Time: {round(time.perf_counter() - start_time, 2)} - Producer {id} produced-> Item: {id}-{counter}")
        counter += 1
        await asyncio.sleep(1)
    await queue.put(None)

async def consumer(queue):
    start_time = time.perf_counter()
    while True:
        item = await queue.get()
        if item is None:
            print(f'Time: {round(time.perf_counter() - start_time, 2)} - Consumer consumed None')
            break
        print(f'Time: {round(time.perf_counter() - start_time, 2)} - Consumer consumed Item: {item}')    

async def main():
    queue = asyncio.Queue()
    start_time = time.perf_counter()
    
    producer_tasks = [asyncio.create_task(producer(queue, id)) for id in ["A", "B", "C"]]
    consumer_task = asyncio.create_task(consumer(queue))

    await asyncio.gather(*producer_tasks, consumer_task)
    
    print(f"Time: {round(time.perf_counter() - start_time, 2)} sec")

if __name__ == "__main__":
    asyncio.run(main())