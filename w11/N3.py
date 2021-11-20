import threading
import time
import sys

L = list(map(float,input().split()))
start = time.time()

def thread_job(args):
	global cym 
	cym += args
	sys.stdout.flush()
cym = 0
threads = [threading.Thread(target=thread_job, args=(i,)) for i in L]
for thread in threads:
	thread.start()
for thread in threads:
	thread.join()
print(cym)
print(time.time() - start)