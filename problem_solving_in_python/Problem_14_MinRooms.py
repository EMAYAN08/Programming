"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
def min_rooms(intervals):
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])

    num_rooms = 0
    end_ptr = 0

    for i in range(len(intervals)):
        if start_times[i] < end_times[end_ptr]:
            num_rooms += 1
        else:
            end_ptr += 1

    return num_rooms

print(min_rooms([(30, 75), (0, 50), (60, 150)]))
