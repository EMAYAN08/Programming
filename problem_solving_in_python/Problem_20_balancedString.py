"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.

"""

def is_balanced(s):
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            # Check if the stack is empty before popping
            if not stack:
                return False
            # Pop the top element from the stack
            top = stack.pop()
            # Check whether the top and current character match
            if (top == '(' and char != ')') or \
               (top == '[' and char != ']') or \
               (top == '{' and char != '}'):
                return False
    # Check if the stack is empty after processing the input string
    return len(stack) == 0

print(is_balanced("([])[]({})")) # returns TRUE
print(is_balanced("([)]")) #returns FALSE
print(is_balanced("((()")) #returns FALSE
