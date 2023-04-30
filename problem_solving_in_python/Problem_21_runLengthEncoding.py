"""
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. For example, 
the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.

"""

def run_length_encode(s):
    """
    Encodes a string using run-length encoding
    """
    encoded = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        encoded.append(str(count) + s[i])
        i += 1
    return ''.join(encoded)

def run_length_decode(s):
    """
    Decodes a string that has been run-length encoded
    """
    decoded = []
    i = 0
    while i < len(s):
        count = ''
        while s[i].isdigit():
            count += s[i]
            i += 1
        count = int(count)
        char = s[i]
        decoded.append(char * count)
        i += 1
    return ''.join(decoded)

# Example input string
s = 'AAAABBBCCDAA'

# Run-length encode the string
encoded = run_length_encode(s)
print(encoded) # Output: '4A3B2C1D2A'

# Run-length decode the encoded string
decoded = run_length_decode(encoded)
print(decoded) # Output: 'AAAABBBCCDAA'
