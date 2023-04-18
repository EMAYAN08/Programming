
"""

Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period."""




def length_longest_path(file_system: str) -> int:
    """
    Returns the length of the longest absolute path to a file in the file system.

    :param file_system: str, representing the file system in the specified format
    :return: int, the length of the longest absolute path to a file in the file system
    """
    # Split the input string into individual directory and file names
    paths = file_system.split('\n')
    
    # Initialize a dictionary to keep track of the length of the longest path to each directory at each level
    longest_path_lengths = {0: 0}
    
    # Initialize a variable to keep track of the length of the longest absolute path
    longest_path_length = 0
    
    for path in paths:
        # Count the number of leading tabs to determine the depth of the current directory
        depth = path.count('\t')
        
        # Remove the leading tabs and get the name of the directory or file
        name = path.lstrip('\t')
        
        # If the current path is a directory, update the dictionary with the length of the longest path to this directory
        if '.' not in name:
            # Calculate the length of the longest path to the current directory as the length of the longest path to the parent directory plus the length of the current directory name plus one (for the slash separator)
            longest_path_lengths[depth + 1] = longest_path_lengths[depth] + len(name) + 1
        else:
            # If the current path is a file, calculate its absolute path length as the length of the longest path to its parent directory plus the length of the file name
            path_length = longest_path_lengths[depth] + len(name)
            
            # If the current path is longer than the current longest path, update the longest path length
            longest_path_length = max(longest_path_length, path_length)
            
    return longest_path_length

file_system = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(length_longest_path(file_system))  # Output: 20

file_system = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(length_longest_path(file_system))  # Output: 32

