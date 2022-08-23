import asyncio
import os
import random
import aiohttp
import time

async def download(session,url,id):
    async with session.get(url) as response:
        file_name=os.path.basename(url)+str(round(random.random() * (100 + id)))+'.jpg'

        with open(f'images/{file_name}','wb') as file:
            while True:
                chunk=await response.content.read(1024)
                if not chunk:
                    break
                file.write(chunk)
        return await response.release()

async def main(loop):
    url = 'https://get.wallhere.com/photo/mountains-snow-grass-water-plants-sky-1011450.jpg'
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks=[asyncio.create_task(download(session,url,i)) for i in range(20)]
        await asyncio.gather(*tasks)



if __name__=='__main__':
    startTime = time.time()
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    print(time.time() - startTime)