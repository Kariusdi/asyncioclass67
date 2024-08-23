import asyncio
import aiohttp
import time

async def get_api(client, url):
    start_time = time.perf_counter()  # Start the timer
    async with client.get(url) as respone:
        print(f'{time.ctime()} get {url}')
        res = await respone.json()
        elapsed_time = time.perf_counter() - start_time
        print(f'Asynchronous get ability={url} {len(res["pokemon"])} pokemons. Time taken: {elapsed_time} seconds')
        return res

async def fetch_pokemons_ability():
    async with aiohttp.ClientSession() as session:
        urls = ["https://pokeapi.co/api/v2/ability/battle-armor", "https://pokeapi.co/api/v2/ability/speed-boost"]
                
        tasks = [asyncio.create_task(get_api(session, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        pokemons = []
        for i in range(len(results)):
            for j in range(len(results[i]["pokemon"])):
                pokemons.append(results[i]["pokemon"][j]['pokemon']['name'])
            print(f'{time.ctime()} {pokemons}')
            pokemons.clear()
        
if __name__ == "__main__":
    asyncio.run(fetch_pokemons_ability())