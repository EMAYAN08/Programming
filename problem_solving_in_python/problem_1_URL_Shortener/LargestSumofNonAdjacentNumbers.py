"""Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?"""

def max_sum_non_adjacent(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)

    prev_prev = arr[0]
    prev = max(arr[0], arr[1])
    max_sum = prev

    for i in range(2, len(arr)):
        max_sum = max(prev, prev_prev + arr[i], max_sum)
        prev_prev = prev
        prev = max_sum

    return max_sum

print(max_sum_non_adjacent([5,1,1,5]))