"""Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"."""

def longest_substring_with_k_distinct_characters(s, k):
    if k == 0 or len(s) == 0:
        return 0

    left, right = 0, 0
    char_freq = {}
    max_len = 0

    while right < len(s):
        # add the current character to the frequency dictionary
        char_freq[s[right]] = char_freq.get(s[right], 0) + 1

        # if the number of distinct characters in the substring is greater than k
        # move the left pointer and remove the leftmost character from the dictionary
        while len(char_freq) > k:
            char_freq[s[left]] -= 1
            if char_freq[s[left]] == 0:
                del char_freq[s[left]]
            left += 1

        # update the maximum length if necessary
        max_len = max(max_len, right - left + 1)

        right += 1

    return max_len

s = "abcba"
k = 2
result = longest_substring_with_k_distinct_characters(s, k)
print(result)  # output: 3 (the longest substring is "bcb")

