import asyncio
import time

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 6
move_pairs = 30

# 1 = 18 sec
# 2 = 18 sec
# 3 = 18 sec
# 4 = 18 sec
# 5 = 18 sec
# 6 = 19 sec
# 10 = 32 sec
# 11 = 35 sec
# 12 = 38 sec
# 15 = 47 sec
# 24 = 75 sec

# Again notice that I declare the main() function as a async function
async def main(x):
    start_counter = time.perf_counter()
    for i in range (move_pairs):
        time.sleep(my_compute_time)
        print(f"Board - {x+1} {i+1} Judit made a move")
        # Here our opponent is making their turn and now we can move onto the next board.
        await asyncio.sleep(opponent_compute_time)
        print(f"Board - {x+1} {i+1} Opponent made a move")
    print(f"Board - {x+1} >>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - start_counter)}")
    return round(time.perf_counter() - start_counter)

async def async_io():
    # Again same structure as in async-io.py
    tasks = []
    for i in range(opponents):
        tasks += [main(i)]
    await asyncio.gather(*tasks)
    print(f"Board exhibition finished in {round(time.perf_counter() - start_time)} secs.")


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")