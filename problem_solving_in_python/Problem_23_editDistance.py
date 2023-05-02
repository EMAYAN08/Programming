"""
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. 
For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
Given two strings, compute the edit distance between them.

"""
def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # Create a matrix of zeros with size (m+1)x(n+1)
    d = [[0] * (n + 1) for i in range(m + 1)]
    
    # Initialize the first row and column of the matrix
    for i in range(1, m + 1):
        d[i][0] = i
    for j in range(1, n + 1):
        d[0][j] = j
    
    # Fill in the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1
    
    # Return the edit distance
    return d[m][n]

s1 = "kitten"
s2 = "sitting"
print(edit_distance(s1, s2))  # Output: 3
