import threading
import time
import random

def thread_function(id):
    print(f"Hi, I'm thread {id}")
    sleep_time = random.uniform(1, 5)
    time.sleep(sleep_time)
    print(f"Thread {id} says goodbye after sleeping for {sleep_time:.2f} seconds")

threads = []

for i in range(3):
    thread = threading.Thread(target=thread_function, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()