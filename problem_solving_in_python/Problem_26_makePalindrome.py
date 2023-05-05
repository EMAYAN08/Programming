"""
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. 
If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).
For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). 
There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
As another example, given the string "google", you should return "elgoogle".

"""

def make_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
    
    i, j = 0, n-1
    res = []
    while i <= j:
        if s[i] == s[j]:
            res.append(s[i])
            i += 1
            j -= 1
        elif dp[i+1][j] < dp[i][j-1]:
            res.append(s[i])
            i += 1
        else:
            res.append(s[j])
            j -= 1
    
    return ''.join(res + res[::-1][1:]) if res else s[0]

