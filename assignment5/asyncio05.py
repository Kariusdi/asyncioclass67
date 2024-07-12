from random import random
import asyncio

# coroutine to execute in a new task
async def cooking_coro(arg):
    # generate a random value between 0 and 1 plus 1
    value = random() + 1
    # report the every value that get into the function before await
    print(f'Microwave ({arg}): Cooking {value} seconds...')
    # block for a moment
    await asyncio.sleep(value)
    # report the first value that finished from await
    print(f'Microwave ({arg}): Finished cooking')
    # return name and time
    return [arg, value]
    

# main coroutine
async def main():
    tasks = ["Rice", "Noodle", "Curry"]
    # create many tasks
    tasks = [asyncio.create_task(cooking_coro(i)) for i in tasks]
    # wait for all tasks to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # print result
    print(f'Completed task: {len(done)}')
    # get the last arg from set (it's a return value in form of result)
    finished = done.pop().result()
    print(f'- {finished[0]} is completed in {finished[1]}')
    print(f'Uncompleted task: {len(pending)}')

# start the asyncio program
asyncio.run(main())