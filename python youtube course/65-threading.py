# thread = a flow of execution

# io bound = things that wait for external input. like time.sleep

# cpu bound = things that wait for the program to run itself

# when functions are called, they are run one by one. With threads, you can set one thread to each function
# so that they can all run at the same time. This only works with functions that have time.sleep and stuff
# like that.

import threading
import time

def eat():
  time.sleep(3)
  print("Eaten")

def drink():
  time.sleep(4)
  print("Drank")

def left():
  time.sleep(5)
  print("Leften")

x = threading.Thread(target=eat)
x.start()

y = threading.Thread(target=drink)
y.start()

z = threading.Thread(target=left)
z.start()

print(threading.active_count()) # prints the number of threads at work, so should be 4 including the main thread.
print(threading.enumerate()) # prints the names of all the threads running

# this makes it so that the main thread can finish before the time.sleep threads finish.