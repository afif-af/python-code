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

