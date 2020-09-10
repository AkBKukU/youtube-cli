
import os
import time

class Util():

    def progress_bar(self,name,start_time, done):
        """Progress with time"""
        width = os.get_terminal_size().columns
        start = name + " ["
        end = "] 100% 00:00:00-00:00:00 "
        elapsed = time.time() - start_time
        remaining = (elapsed / ( done if done != 0 else 0.001)) * (1 - done)
        fluff = len(start) + len(end)

        bar = round(done*(width-fluff))
        space = width-fluff-bar
        print("\r" + start, end='', flush=True)
        for j in range(bar):
            print("=", end='', flush=True)
        for j in range(space):
            print(" ", end='', flush=True)
        print("] ", end='', flush=True)
        print(round(done*100), end='', flush=True)
        elp=time.strftime("%H:%M:%S", time.gmtime(elapsed))
        rem=time.strftime("%H:%M:%S", time.gmtime(remaining))
        print("% "+ elp + "-" + rem, end='', flush=True)
        if done == 1:
            print("\n")


