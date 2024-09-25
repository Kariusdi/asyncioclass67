import asyncio
import math

def position_max_min(distance):
    max_result = [i for i, j in enumerate(distance) if j == max(distance)]
    min_result = [i for i, j in enumerate(distance) if j == min(distance)]
    return max_result, min_result

async def distance(end_point, start_point):
    z = (end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) **2
    await asyncio.sleep(1)
    d = round(math.sqrt(z), 2)
    return d

async def main(): 
    start_point = [3, 3]
    point_locations = [[6, 9], [2, 8], [3, 7], [4, 6], [3, 5], [7, 4], [5, 3], [1, 2], [6, 1], [8, 2]]
    
    tasks = [asyncio.create_task(distance(point, start_point)) for point in point_locations]
    distance_result = await asyncio.gather(*tasks)
    
    print(f"\nDistance calculation result: {distance_result}\n")
    
    max_result, min_result = position_max_min(distance_result)
    
    print(f"\nTotal of the farthest point => {len(max_result)}")
    for max in max_result:
        print(f"Farthest point at {point_locations[max]} with {distance_result[max]} km.")
    
    print(f"\nTotal of the closest point => {len(min_result)}")
    for min in min_result:
        print(f"Closest point at {point_locations[min]} with {distance_result[min]} km.")

if __name__ == "__main__":
    asyncio.run(main())  