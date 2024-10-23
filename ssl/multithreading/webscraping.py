#Scenario is for IO bound task
# basic web scrapping  -> involves in making numerous requests to web pages these tasks are IO bound because they
#spend a lot of time using waiting for the response from the servers. Multithreading can significantly improve
#performance by allowing multiple web pages to be fetched concurrently.


# https://python.langchain.com/docs/introduction/


# https://python.langchain.com/docs/concepts/


# https://python.langchain.com/docs/tutorials/


import threading 

import requests

from bs4 import BeautifulSoup

urls = [
'https://python.langchain.com/docs/introduction/',


'https://python.langchain.com/docs/concepts/',


'https://python.langchain.com/docs/tutorials/'

]

def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f' {len(soup.text)} are the characters which will be there in all the urls')


threads = []

for url in urls:
    thread=threading.Thread(target=fetch_contents, args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


print('all pages fetched')
