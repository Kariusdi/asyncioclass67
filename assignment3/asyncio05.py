# When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon
import asyncio
import aiohttp
from time import ctime

async def get_api(client, url):
    async with client.get(url) as respone:
        return await respone.json()

async def fetch_hacker_news():
    async with aiohttp.ClientSession() as session:
        url = f"http://hacker-news.firebaseio.com/v0/item/24661271.json?print=pretty"
        task1 = asyncio.create_task(get_api(session, url))
        
        url2 = f"http://hacker-news.firebaseio.com/v0/item/24658683.json?print=pretty"
        task2 = asyncio.create_task(get_api(session, url2))
        
        news1 = await task1 # wait till task 1 is completed
        news2 = await task2 # wait till task 2 is completed
        print(f'{ctime()} {news1['title']}')
        print(f'{ctime()} {news2['title']}')

if __name__ == "__main__":
    asyncio.run(fetch_hacker_news())