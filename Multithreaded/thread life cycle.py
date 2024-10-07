import threading

def func(x):
   print('Current Thread Details:', threading.current_thread())
   for n in range(x):
      print('{} Running'.format(threading.current_thread().name), n)
   print('Internal Thread Finished...')

# Create thread objects
t1 = threading.Thread(target=func, args=(2,))
t2 = threading.Thread(target=func, args=(3,))

# Start the threads
print('Thread State: CREATED')
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()
print('Threads State: FINISHED')

# Simulate main thread work
for i in range(3):
   print('Main Thread Running', i)

print("Main Thread Finished...")

import threading
import time

# Create a semaphore
semaphore = threading.Semaphore(2)

def worker():
   with semaphore:
      print('{} has started working'.format(threading.current_thread().name))
      time.sleep(2)
      print('{} has finished working'.format(threading.current_thread().name))

# Create a list to keep track of thread objects
threads = []

# Create and start 5 threads
for i in range(5):
   t = threading.Thread(target=worker, name='Thread-{}'.format(i+1))
   threads.append(t)
   print('{} has been created'.format(t.name))
   t.start()

# Wait for all threads to complete
for t in threads:
   t.join()
   print('{} has terminated'.format(t.name))

print('Threads State: All are FINISHED')
print("Main Thread Finished...")

