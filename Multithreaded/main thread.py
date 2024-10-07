import threading

name = 'threadDemo'
print('Output:', name)
print(threading.current_thread())

import threading
import time

def func(x):
   time.sleep(x)
   if not threading.current_thread() is threading.main_thread():
      print('threading.current_thread() not threading.main_thread()')

t = threading.Thread(target=func, args=(0.5,))
t.start()

print(threading.main_thread())
print("Main thread finished")

import threading
import time

def func(x):
   print('Current Thread Details:',threading.current_thread())
   for n in range(x):
      print('Internal Thread Running', n)
   print('Internal Thread Finished...')

t = threading.Thread(target=func, args=(6,))
t.start()

for i in range(3):
   print('Main Thread Running',i)
print("Main Thread Finished...")

from threading import Thread
from time import sleep

def my_function_1():
   print("Worker 1 started")
   sleep(1)
   print("Worker 1 done")

def my_function_2(main_thread):
   print("Worker 2 waiting for Worker 1 to finish")
   main_thread.join()
   print("Worker 2 started")
   sleep(1)
   print("Worker 2 done")

worker1 = Thread(target=my_function_1)
worker2 = Thread(target=my_function_2, args=(worker1,))

worker1.start()
worker2.start()

for num in range(6):
   print("Main thread is still working on task", num)
   sleep(0.60)

worker1.join()
print("Main thread Completed")

