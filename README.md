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

## Problem 17

- Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
Design a binary tree node class with the following methods:
- is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. 
- Otherwise, it should lock it and return true.
- unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
- You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.

## Problem 18

- Implement regular expression matching with the following special characters:
- . (period) which matches any single character
- asterisk * which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
- For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
- Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

## Problem 19

- Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
- Do this in constant space and in one pass.

## Problem 20

- Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string 
``` 
"([])[]({})" 
``` 
you should return true.
- Given the string 
```
"([)]" or "((()"
```
you should return false.

## Problem 21

- Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
- Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

## PROBLEM 22

- You are given an array of non-negative integers that represents a two-dimensional elevation map wnbhere each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
- Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
- For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
- Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

## Problem 23

- The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. 
- For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
- Given two strings, compute the edit distance between them.

## Problem 24

- Suppose you are given a table of currency exchange rates, represented as a 2D array. 
- Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.
- There are no transaction costs and you can trade fractional quantities.

## Problem 25

- Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
- Recall that the median of an even-numbered list is the average of the two middle numbers. 
- For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

```
2
1.5
2
3.5
2
2
2

```

## Problem 26

- Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).
- For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). 
- There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
As another example, given the string "google", you should return "elgoogle".

## Problem 27

- Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. 
- You can only swap elements of the array.Do this in linear time and in-place.
- For example, given the array 
```['G', 'B', 'R', 'R', 'B', 'R', 'G']``` 
it should become ```['R', 'R', 'R', 'G', 'G', 'B', 'B']```

## Problem 28

- Given the root to a binary search tree, find the second largest node in the tree. 











