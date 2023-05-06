"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. 
You can only swap elements of the array.
Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

"""
def sort_rgb(arr):
    n = len(arr)
    i, r, b = 0, 0, n-1
    
    while i <= b:
        if arr[i] == 'R':
            arr[i], arr[r] = arr[r], arr[i]
            i += 1
            r += 1
        elif arr[i] == 'B':
            arr[i], arr[b] = arr[b], arr[i]
            b -= 1
        else:
            i += 1
    
    return arr

print(sort_rgb(['G', 'B', 'R', 'R', 'B', 'R', 'G'])) #output: ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
