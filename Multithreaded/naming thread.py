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