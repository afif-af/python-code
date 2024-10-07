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

