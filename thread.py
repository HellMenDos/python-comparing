import requests
import random
import os 
from threading import Thread
import time
def download(url,id):
    file_name=os.path.basename(url)+str(round(random.random() * (100 + id)))+'.jpg'
    with requests.get(url, stream=True) as response: 
        print(id)
        with open(f'images/{file_name}','wb') as file:
            for chunk in response.iter_content(chunk_size=8192): 
                file.write(chunk)

def main():
    url = 'https://get.wallhere.com/photo/mountains-snow-grass-water-plants-sky-1011450.jpg'
    th = [Thread(target=download, args=(url,i)) for i in range(10)]
    for t in th:
        t.start()

if __name__=='__main__':
    main()

