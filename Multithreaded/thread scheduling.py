import threading
import time

# Define the event function
def schedule_event(name, start):
   now = time.time()
   elapsed = int(now - start)
   print('Elapsed:', elapsed, 'Name:', name)

# Start time
start = time.time()
print('START:', time.ctime(start))

# Schedule events using Timer
t1 = threading.Timer(3, schedule_event, args=('EVENT_1', start))
t2 = threading.Timer(2, schedule_event, args=('EVENT_2', start))

# Start the timers
t1.start()
t2.start()

t1.join()
t2.join()
# End time
end = time.time()
print('End:', time.ctime(end))

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def schedule_event(name, start):
   now = time.time()
   elapsed = int(now - start)
   print('elapsed=',elapsed, 'name=', name)

start = time.time()
print('START:', time.ctime(start))
scheduler.enter(2, 1, schedule_event, ('EVENT_1', start))
scheduler.enter(5, 1, schedule_event, ('EVENT_2', start))

scheduler.run()

# End time
end = time.time()
print('End:', time.ctime(end))

import sched
from datetime import datetime
import time

def addition(a,b):
   print("Performing Addition : ", datetime.now())
   print("Time : ", time.monotonic())
   print("Result {}+{} =".format(a, b), a+b)

s = sched.scheduler()

print("Start Time : ", datetime.now())

event1 = s.enter(4, 1, addition, argument = (5,6))
print("Event Created : ", event1)
s.run()
print("End Time : ", datetime.now())

