import asyncio

async def fibonacci(n):
    print("Fibonacci starter: ", n)
    await asyncio.sleep(1)
    print("Fibonacci", n, "is processing...")
    a, b = 0, 1
    if n <= 1:
        print(n, "is done")
        return n
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        print(n, "is done")
        return b

async def main():
    n = 10
    coros = [asyncio.create_task(fibonacci(i)) for i in range(n)]
    done, pending = await asyncio.wait(coros)
    # Extracting results from the completed tasks
    results = [task.result() for task in done]
    print(results)  # This will print the list of results from all tasks

asyncio.run(main())