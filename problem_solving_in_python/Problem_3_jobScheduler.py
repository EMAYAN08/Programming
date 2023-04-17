"""Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds."""

import time
import threading

def job_scheduler(f, n):
    time.sleep(n/1000.0) # convert milliseconds to seconds
    f()

# Example usage
def print_hello():
    print("Hello")

job_thread = threading.Thread(target=job_scheduler, args=(print_hello, 5000))
job_thread.start()
