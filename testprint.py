#!/usr/bin/python3
import time
import os
width = os.get_terminal_size().columns

# percent
done = 0.0

# name of job
name = "This is a video title"

start = "Uploading: " + name + " ["
end = "] 100% 00:00:00 "
fluff = len(start) + len(end)
start_time = time.time()

while not done > 1:
    done += 0.01 
    bar = round(done*(width-fluff))
    space = width-fluff-bar
    print("\r" + start, end='', flush=True)
    for j in range(bar):
        print("=", end='', flush=True)
    for j in range(space):
        print(" ", end='', flush=True)
    print("] ", end='', flush=True)
    print(round(done*100), end='', flush=True)
    dur=time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
    print("% "+ dur, end='', flush=True)
    time.sleep(0.1)
print()

