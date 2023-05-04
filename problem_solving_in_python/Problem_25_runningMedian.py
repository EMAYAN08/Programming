"""
Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers. 
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2

"""

import heapq

class RunningMedian:
    def __init__(self):
        self.min_heap = [] # contains the larger half of the data
        self.max_heap = [] # contains the smaller half of the data (inverted)
        
    def add_number(self, num):
        if not self.max_heap or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # rebalance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def get_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]

rm = RunningMedian()
for num in [2, 1, 5, 7, 2, 0, 5]:
    rm.add_number(num)
    print(rm.get_median())

