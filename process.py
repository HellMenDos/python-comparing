import requests
import random
import os 
from multiprocessing import Process
import time
def download(url,id):
    file_name=os.path.basename(url)+str(round(random.random() * (100 + id)))+'.jpg'
    with requests.get(url, stream=True) as response: 
        with open(f'images/{file_name}','wb') as file:
            print(id)
            for chunk in response.iter_content(chunk_size=8192): 
                file.write(chunk)

def main():
    url = 'https://get.wallhere.com/photo/mountains-snow-grass-water-plants-sky-1011450.jpg'
    th = [Process(target=download, args=(url,i)) for i in range(10)]
    for t in th:
        t.start()


if __name__=='__main__':
    startTime = time.time()
    main()
    print(time.time() - startTime)