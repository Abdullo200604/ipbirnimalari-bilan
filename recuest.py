import asyncio
import aiohttp

url = "http://10.50.5.37:8080/home"

REQUEST_COUNT = 100

async def fetch(session, i):
    try:
        async with session.get(url) as response:
            text = await response.text()
            print(f"[{i}] Status: {response.status}")
            return text
    except Exception as e:
        print(f"[{i}] Xato: {e}")
        return None

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(REQUEST_COUNT):
            tasks.append(fetch(session, i+1))
        await asyncio.gather(*tasks)

# Ishga tushurish
asyncio.run(main())
