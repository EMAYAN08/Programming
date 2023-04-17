"""PROBLEM DESCRIPTION:
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        
    def find(self, prefix):
        node = self.root
        results = []
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self._search(node, prefix, results)
        return results
        
    def _search(self, node, prefix, results):
        if node.is_word:
            results.append(prefix)
        for char in node.children:
            self._search(node.children[char], prefix + char, results)
            
def autocomplete(s, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie.find(s)
    
# Example usage:
words = ["dog", "deer", "deal"]
results = autocomplete("de", words)
print(results) # prints ["deer", "deal"]


"""Code Explanation:
The code defines two classes: TrieNode and Trie. The TrieNode class represents a single node in a trie, and has two properties: children, 
which is a dictionary mapping characters to child nodes, and is_word, which is True if the node represents the end of a word.
The Trie class represents a trie data structure, and has two methods: insert, which inserts a word into the trie, and find, 
which finds all words in the trie that have a given prefix. The find method works by traversing the trie starting from the root node, 
following the path of characters in the prefix, 
and then recursively searching all child nodes to find all complete words.

The autocomplete function takes a query string s and a list of words words, and returns a list of all words in words that have s as a prefix. 
It creates a trie from words using the Trie class, and then calls the find method of the trie with the query string s to find all matching words.

Finally, the code includes an example usage of the autocomplete function with the sample input ["dog", "deer", "deal"] and query string "de", which should return ["deer", "deal"]"""