# import os, re

# received_packages = re.compile(r"(\d) received")
# status = ("no response", "alive but losses", "alive")

# for suffix in range(20, 30):
#     ip = "192.168.178." + str(suffix)
#     ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
#     print("... pinging ", ip)
#     while True:
#         line = ping_out.readline()
#         if not line:
#             break
#         n_received = received_packages.findall(line)
#         if n_received:
#             print(ip + ": " + status[int(n_received[0])])



import os, re
import threading

def thread_job(args):
    # lock.acquire()
    global counter, received_packages, status
    ip = counter + str(args)
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])
    # lock.release()


# lock = threading.Lock()
received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")
counter = "192.168.178."
threads = [threading.Thread(target=thread_job, args=(i,)) for i in range(20,30)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print('finish')