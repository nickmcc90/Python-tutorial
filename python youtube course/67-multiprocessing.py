# multiprocessing = better for cpu bound tasks (heavy cpu usage)
# multithreading = better for io bound tasks (waiting around)
# multiprocessing is running tasks in parallel on different cpu cores, bypasses GIL used for threading.

from multiprocessing import Process, cpu_count
import time

def counter(num):
  count = 0
  while count < num:
    count += 1

def main():
  
  a = Process(target='counter', args=(1000000000,)) # how long will it take for the program to get up to 1 billion?
  a.start()

  a.join() # this makes the thread syncronized with the main function such that the thread would have to finish before main finishes.

  print("finished in:", time.perf_counter(), "seconds")


if __name__ == '__main__':
  main()

# we can make this faster with multiprocessing.
  

def main():

  a = Process(target='counter', args=(500000000,)) # we have two things in half counting, should be faster.
  b = Process(target='counter', args=(500000000,)) # we have two things in half counting, should be faster.

  a.start()
  b.start()

  a.join()
  b.join()

   print("finished in:", time.perf_counter(), "seconds")
  



print(cpu_count()) # this shows you how many cpus you have on your computer. If you run more processes per cpu than
                    # your computer has, then it hinders performance.