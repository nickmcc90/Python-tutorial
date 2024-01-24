# daemon thread = a thread that runs in the background, not important for program to run.
# the program won't wait for daemon threads to complete before exiting.
# non-daemon threads stay alive until killed.

# ex. background tasks, garbage collection, waiting for input, long running processes.

import threading
import time

def timer():
  print()
  print()
  count = 0
  while True:
    time.sleep(1)
    count += 1
    print("logged in for: ",count, "seconds")

x = threading.Thread(target='timer', daemon=True)
x.start()

answer = input("Do you wish to exit?")


# the program will finish running (even the daemon) when the user inputs a response.

# we can set daemons externally, and check if statements are daemons

x.setDaemon(True)
print(x.isDaemon)