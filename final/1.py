import time
import asyncio

async def process_data(data, delay):
    start = time.time()
    print(f"At t={time.time()-start:.2f} รอ {delay} วินาทีก่อนประมวลผลข้อมูลชุดนี้...")
    await asyncio.sleep(delay)
    
    sorted_data = sorted(data)
    print(f"At t={time.time()-start:.2f} ข้อมูลที่เรียงลำดับ: {sorted_data}")
    return sorted_data

async def main():
    start = time.time()
    dataset = {
        "data1": {
            "data": [5, 2, 3, 1, 4],
            "delay": 2
        },
        "data2": {
            "data": [50, 30, 10, 20, 40],
            "delay": 3
        },
        "data3": {
            "data": [500, 300, 100, 200, 400],
            "delay": 1
        }
    }
    
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(process_data(dataset[i]['data'], dataset[i]['delay'])) for i in dataset]
        
    for i in range(len(tasks)):
        print(f"At t={time.time()-start:.2f} ผลลัพธ์จาก data{i}: {tasks[i].result()}")

if __name__ == "__main__":
    asyncio.run(main())    