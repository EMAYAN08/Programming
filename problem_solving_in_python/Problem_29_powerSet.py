"""
The power set of a set is the set of all its subsets. 
Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3}, 
it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
You may also use a list or array to represent a set.

"""
def power_set(s):
    n = len(s)
    power_set_size = 2 ** n
    result = []

    # Generate all possible combinations
    for i in range(power_set_size):
        subset = []

        # Check the jth bit in i
        for j in range(n):
            if (i & (1 << j)) > 0:
                subset.append(s[j])

        result.append(subset)

    return result

set_input = [1, 2, 3]
result = power_set(set_input)
print(result)

