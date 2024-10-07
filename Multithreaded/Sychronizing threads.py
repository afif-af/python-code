import threading

counter = 10

def increment(theLock, N):
   global counter
   for i in range(N):
      theLock.acquire()
      counter += 1
      theLock.release()

lock = threading.Lock()
t1 = threading.Thread(target=increment, args=[lock, 2])
t2 = threading.Thread(target=increment, args=[lock, 10])
t3 = threading.Thread(target=increment, args=[lock, 4])

t1.start()
t2.start()
t3.start()

# Wait for all threads to complete
for thread in (t1, t2, t3):
   thread.join()

print("All threads have completed")
print("The Final Counter Value:", counter)


print("\n \n")
import threading

counter = 0


# Consumer function
def consumer(cv):
    global counter
    with cv:
        print("Consumer is waiting")
        cv.wait()  # Wait until notified by increment
        print("Consumer has been notified. Current Counter value:", counter)


# increment function
def increment(cv, N):
    global counter
    with cv:
        print("increment is producing items")
        for i in range(1, N + 1):
            counter += i  # Increment counter by i

        # Notify the consumer
        cv.notify()
        print("Increment has finished")


# Create a Condition object
cv = threading.Condition()

# Create and start threads
consumer_thread = threading.Thread(target=consumer, args=[cv])
increment_thread = threading.Thread(target=increment, args=[cv, 5])

consumer_thread.start()
increment_thread.start()

consumer_thread.join()
increment_thread.join()

print("The Final Counter Value:", counter)

print("\n \n")
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
        print_time(self.name, self.counter, 3)


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threads = []

# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# Start the new Threads
thread1.start()
thread2.start()

# Join the threads
thread1.join()
thread2.join()

print("Exiting Main Thread")