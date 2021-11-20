import urllib.request
import time
import threading


urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]


def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


start = time.time()
# for url in urls:
#     read_url(url)
# print(time.time() - start)
threads = [threading.Thread(target=read_url, args=(i,)) for i in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(time.time() - start)