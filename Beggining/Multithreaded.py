
#     threading.activeCount() − Returns the number of thread objects that are active.
#     threading.currentThread() − Returns the number of thread objects in the caller's thread control.
#     threading.enumerate() − Returns a list of all thread objects that are currently active.
# Thread class that implements threading.
#     run() − The run() method is the entry point for a thread.
#     start() − The start() method starts a thread by calling the run method.
#     join([time]) − The join() waits for threads to terminate.
#     isAlive() − The isAlive() method checks whether a thread is still executing.
#     getName() − The getName() method returns the name of a thread.
#     setName() − The setName() method sets the name of a thread.


import _thread
import time

def print_name(name, *arg):
   print(name, *arg)

name="thread..."
_thread.start_new_thread(print_name, (name, 1))
_thread.start_new_thread(print_name, (name, 1, 2))

time.sleep(0.5)
print("\n")

import threading
import time

def print_name(name, *args):
    print(name, *args)

name = "thread..."

# Create and start threads
thread1 = threading.Thread(target=print_name, args=(name, 1))
thread2 = threading.Thread(target=print_name, args=(name, 1, 2))

thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Threads are finished...exiting")
print("\n")

import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      # Get lock to synchronize threads
      threadLock.acquire()
      print_time(self.name, self.counter, 3)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print ("Exiting Main Thread")
print("\n")

import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      process_data(self.name, self.q)
      print ("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = q.get()
         queueLock.release()
         print ("%s processing %s" % (threadName, data))
      else:
         queueLock.release()
         time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")

print("\n")

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
print("\n")

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

print("\n")
from threading import Thread

def addition_of_numbers(x, y):
   result = x + y
   print('Addition of {} + {} = {}'.format(x, y, result))

def cube_number(i):
   result = i ** 3
   print('Cube of {} = {}'.format(i, result))

def basic_function():
   print("Basic function is running concurrently...")

Thread(target=addition_of_numbers, args=(2, 4)).start()
Thread(target=cube_number, args=(4,)).start()
Thread(target=basic_function).start()
print("\n")
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, 5, self.counter)
      print ("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
print ("Exiting Main Thread")
print("\n")
import _thread
import time


# Define a function for the thread
def thread_task(threadName, delay):
    for count in range(1, 6):
        time.sleep(delay)
        print("Thread name: {} Count: {}".format(threadName, count))


# Create two threads as follows
try:
    _thread.start_new_thread(thread_task, ("Thread-1", 2,))
    _thread.start_new_thread(thread_task, ("Thread-2", 4,))
except:
    print("Error: unable to start thread")

while True:
    pass

thread_task("test", 0.3)
print("\n")

from threading import Thread
from time import sleep

def my_function(arg):
   for i in range(arg):
      print("child Thread running", i)
      sleep(0.5)
thread = Thread(target = my_function, args = (10, ))
thread.start()
print("thread finished...exiting")
print("\n")

import threading
import time

class MyThread(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print("Starting " + self.name)
      print_time(self.name, self.counter)
      print("Exiting " + self.name)

def print_time(threadName, counter):
   while counter:
      time.sleep(1)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)
thread3 = MyThread(3, "Thread-3", 3)

# Start new Threads
thread1.start()
thread3.start()

print("Exiting Main Thread")

from threading import Thread
from time import sleep

def my_function_1(arg):
   for i in range(arg):
      print("Child Thread 1 running", i)
      sleep(0.5)

def my_function_2(arg):
   for i in range(arg):
      print("Child Thread 2 running", i)
      sleep(0.1)

# Create thread objects
thread1 = Thread(target=my_function_1, args=(5,))
thread2 = Thread(target=my_function_2, args=(3,))

# Start the first thread and wait for it to complete
thread1.start()
thread1.join()

# Start the second thread and wait for it to complete
thread2.start()
thread2.join()

print("Main thread finished...exiting")

from threading import Thread
from time import sleep

def my_function_1(arg):
   for i in range(arg):
      print("Child Thread 1 running", i)
      sleep(0.5)

def my_function_2(arg):
   for i in range(arg):
      print("Child Thread 2 running", i)
      sleep(0.1)

# Create thread objects
thread1 = Thread(target=my_function_1, args=(5,))
thread2 = Thread(target=my_function_2, args=(3,))

# Start the first thread and wait for 0.2 seconds
thread1.start()
thread1.join(timeout=0.2)

# Start the second thread and wait for it to complete
thread2.start()
thread2.join()

print("Main thread finished...exiting")

from threading import Thread
import threading
from time import sleep

def my_function_1(arg):
   print("This tread name is", threading.current_thread().name)

# Create thread objects
thread1 = Thread(target=my_function_1, name='My_thread', args=(2,))
thread2 = Thread(target=my_function_1, args=(3,))

print("This tread name is", threading.current_thread().name)

# Start the first thread and wait for 0.2 seconds
thread1.start()
thread1.join()

# Start the second thread and wait for it to complete
thread2.start()
thread2.join()

from threading import Thread
import threading
from time import sleep

def my_function_1(arg):
   threading.current_thread().name = "custom_name"
   print("This tread name is", threading.current_thread().name)

# Create thread objects
thread1 = Thread(target=my_function_1, name='My_thread', args=(2,))
thread2 = Thread(target=my_function_1, args=(3,))

print("This tread name is", threading.current_thread().name)

# Start the first thread and wait for 0.2 seconds
thread1.start()
thread1.join()

# Start the second thread and wait for it to complete
thread2.start()
thread2.join()


import threading

def addition_of_numbers(x, y):
   print("This Thread name is :", threading.current_thread().name)
   result = x + y

def cube_number(i):
   result = i ** 3
   print("This Thread name is :", threading.current_thread().name)

def basic_function():
   print("This Thread name is :", threading.current_thread().name)

# Create threads with custom names
t1 = threading.Thread(target=addition_of_numbers, name='My_thread', args=(2, 4))
t2 = threading.Thread(target=cube_number, args=(4,))
t3 = threading.Thread(target=basic_function)

# Start and join threads
t1.start()
t1.join()

t2.start()
t2.join()

t3.name = 'custom_name'  # Assigning name after thread creation
t3.start()
t3.join()

print(threading.current_thread().name)  # Print main thread's name