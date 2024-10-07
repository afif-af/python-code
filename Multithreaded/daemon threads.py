import threading
from time import sleep

# function to be executed in a new thread
def run():
   # get the current thread
   thread = threading.current_thread()
   # is it a daemon thread?
   print(f'Daemon thread: {thread.daemon}')

# Create a new thread and set it as daemon
thread = threading.Thread(target=run, daemon=True)

# start the thread
thread.start()

print('Is Main Thread is Daemon thread:', threading.current_thread().daemon)

# Block for a short time to allow the daemon thread to run
sleep(0.5)

print("\n")
import threading
from time import sleep

# function to be executed in a new thread
def run():
   # get the current thread
   thread = threading.current_thread()
   # is it a daemon thread?
   print(f'Daemon thread: {thread.daemon}')

# Create a new thread
thread = threading.Thread(target=run)

# Using the daemon property set the thread as daemon before starting the thread
thread.daemon = True

# start the thread
thread.start()

print('Is Main Thread is Daemon thread:', threading.current_thread().daemon)

# Block for a short time to allow the daemon thread to run
sleep(0.5)

print("\n")
from time import sleep
from threading import current_thread
from threading import Thread


# function to be executed in a new thread
def run():
    # get the current thread
    thread = current_thread()
    # is it a daemon thread?
    print(f'Daemon thread: {thread.daemon}')
    thread.daemon = True


# create a new thread
thread = Thread(target=run)

# start the new thread
thread.start()

# block for a 0.5 sec for daemon thread to run
sleep(0.5)