# Programming
Tiny habits, remarkable results! 
Solving one programming problem everyday
## Problem 1

- Implement a URL shortener with the following methods:
- shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
- restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?

## Problem 2

- Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

- For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

- Follow-up: Can you do this in O(N) time and constant space?

## Problem 3

- Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

## Problem 4

- Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
- For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
- Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

## Problem 5

- There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. 
- The order of the steps matters.For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
- What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

## Problem 6

- Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

## Problem 7

- The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
- Hint: The basic equation of a circle is x2 + y2 = r2.

## Problem 8

- Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

## Problem 9

- You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
- record(order_id): adds the order_id to the log
- get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
- You should be as efficient with time and space as possible.

## Problem 10

- Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents
```bash
dir
    subdir1
    subdir2
        file.ext
```

- The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

- The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
```bash
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```
- The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
- We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
- Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

- Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.

## Problem 11

- Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
```
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
```
- Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

## Problem 12

- A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
- Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

## Problem 13

- Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given 
```
A = 3 -> 7 -> 8 -> 10
```
 
```
B = 99 -> 1 -> 8 -> 10
```
Return the node with value 8.

- In this example, assume nodes with the same value are the exact same node objects.
- Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

## Problem 14

- Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
- For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

## Problem 15

- Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
- For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return 
```
['the', 'quick', 'brown', 'fox']
```
- Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either 
```
['bed', 'bath', 'and', 'beyond]
```
 or 
 ```
 ['bedbath', 'and', 'beyond']
 ```

 ## Problem 16

 - You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
- Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. 
- If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
For example, given the following board:

```

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

```

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.





