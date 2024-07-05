# Asynchronous breakfast
import asyncio
from time import sleep, time

# Concurrently breakfast
import asyncio
from time import sleep, time

async def make_coffee(): # 1
    print("coffee: prepare ingridients")
    sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5) # 2: pause, another tasks can be run
    print("coffee: ready")

async def fry_eggs(): # 1
    print("eggs: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3) # 2: pause, another tasks can be run
    print("eggs: ready")

async def toasted_bread():
    print("bread: prepare ingridients")
    sleep(1)
    print("bread: toasting")
    await asyncio.sleep(3) # 2: pause, another tasks can be run
    print("bread: ready")

async def main():
    start = time()
    coffee_task = asyncio.create_task(make_coffee()) # create task to set the schedule
    eggs_task = asyncio.create_task(fry_eggs())
    bread_task = asyncio.create_task(toasted_bread())
    await coffee_task
    await eggs_task
    await bread_task
    print(f"breakfast is ready in {time()-start} min")


asyncio.run(main()) # run top-level function concurrently