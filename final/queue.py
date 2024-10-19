import time
import asyncio

async def producer(queue, id):
    counter = 0
    timer = time.perf_counter()
    while counter <= 2:
        await queue.put(f"{id}-{counter}")
        print("Time: {:.2f} - Producer {} produced-> Item: {}-{}".format(time.perf_counter() - timer, id, id, counter))
        counter += 1
        await asyncio.sleep(1)
    await queue.put(None)

async def consumer(queue):
    timer = time.perf_counter()
    while True:
        item = await queue.get()
        if item is None:
            print('Time: {:.2f} - Consumer consumed None'.format(time.perf_counter() - timer, item))
            break
        print('Time: {:.2f} - Consumer consumed Item: {}'.format(time.perf_counter() - timer, item))    

async def main():
    queue = asyncio.Queue()
    producer_tasks = [asyncio.create_task(producer(queue, id)) for id in ["A", "B", "C"]]
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(*producer_tasks, consumer_task)

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    print("Time: {:.2f} sec".format(time.perf_counter() - start_time))