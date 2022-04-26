# Trie
#   Node
#       value: char
#       children : list 26
#       isEndOfWord: boolean
# insert(word: str)
# index = ord(char) - ord('a')

#%% Implement using Array/List
# class Trie:
#     ALPHABET_SIZE = 26 # class variable or static variable

#     def __init__(self):
#         self.root = self.Node(' ')

#     class Node: # Inner Class of Trie
#         def __init__(self, char):
#             self.value = char   # instance variable
#             self.children = [None] * Trie.ALPHABET_SIZE # This is a waste of space
#             self.isEndOfWord = False

#         def __str__(self):
#             return 'Value={}'.format(self.value)

#     def insert(self, word):
#         current = self.root
#         for ch in word:
#             idx = ord(ch) - ord('a')
#             if current.children[idx] == None:
#                 current.children[idx] = self.Node(ch)
#             current = current.children[idx]
#         current.isEndOfWord = True

#%% Implement using Hash Table
# class Trie:
#     def __init__(self):
#         self.root = self.Node(' ')

#     class Node: # Inner Class of Trie
#         def __init__(self, char):
#             self.value = char   # instance variable
#             self.children = {}
#             self.isEndOfWord = False

#         def __str__(self):
#             return 'Value={}'.format(self.value)

#     def insert(self, word):
#         current = self.root
#         for ch in word:
#             current.children[ch] = current.children.get(ch, self.Node(ch))
#             # if current.children.get(ch) == None:
#             #     current.children[ch] = self.Node(ch)
#             current = current.children[ch]
#         current.isEndOfWord = True

#%% A better abstraction
class Trie:
    ALPHABET_SIZE = 26 # class variable or static variable

    def __init__(self):
        self.root = self.Node(' ')

    class Node: # Inner Class of Trie
        def __init__(self, char):
            self.value = char   # instance variable
            # Every time we changed the data structure for the self.children, 
            # our code breaks at a lot of places in the Trie class.
            # Thus we need a better abstraction of Node class
            self.children = {}  # Hash table implementation
            # self.children = [None] * Trie.ALPHABET_SIZE   # List implementation
            self.isEndOfWord = False

        def hasChild(self, ch):
            return self.children.get(ch)    # Hash table implementation
            # return self.children[ord(ch)-ord('a')] != None  # List implementation
        
        def addChild(self, ch):
            # Hash table implementation
            self.children[ch] = Trie.Node(ch) # To be checked?
            # List implementation
            # self.children[ord(ch)-ord('a')] = Trie.Node(ch) # To be checked?
        
        def getChild(self, ch):
            return self.children.get(ch)    # Hash table implementation
            # return self.children[ord(ch)-ord('a')]      # List implementation
        
        def getChildren(self):
            return self.children.values()   # Hash table implementation
        
        def hasChildren(self):
            return bool(self.children)      # Hash table implementation
        
        def removeChild(self, ch):
            self.children.pop(ch)           # Hash table implementation

        def __str__(self):
            return 'Value={}'.format(self.value)

    def insert(self, word):
        current = self.root
        for ch in word:
            if not current.hasChild(ch):
                current.addChild(ch)
            current = current.getChild(ch)
        current.isEndOfWord = True

    def contains(self, word):
        if word == None:
            return False
        current = self.root
        for ch in word:
            if not current.hasChild(ch):
                return False
            current = current.getChild(ch)
        return current.isEndOfWord
    
    def traverse(self):
        self.__traverse(self.root)
    
    def __traverse(self, node):
        # pre-order: visit the root first
        # print(node.value)      
        # for child in node.getChildren():
        #     self.__traverse(child)
            
        # post-order: visit the root last
        for child in node.getChildren():
            self.__traverse(child)        
        print(node.value)
        
    def remove(self, word):
        if word == None:
            return
        self.__remove(self.root, word, 0)
    
    def __remove(self, node, word, idx):
        if idx == len(word):
            node.isEndOfWord = False
            return
        
        ch = word[idx]
        child = node.getChild(ch)
        if child == None:
            return
        self.__remove(child, word, idx+1)
        if not child.hasChildren and not child.isEndOfWord:
            node.remvoeChild(ch)
    
    def findWords(self, prefix):
        words = []
        lastNode = self.findLastNodeOf(prefix)
        self.__findWords(lastNode, prefix, words)
        return words
        
    def __findWords(self, node, prefix, words):
        if node == None:
            return
        
        if node.isEndOfWord:
            words.append(prefix)
        
        for child in node.getChildren():
            self.__findWords(child, prefix+child.value, words)
        
    def findLastNodeOf(self, prefix):
        if prefix == None:
            return
        current = self.root
        for ch in prefix:
            child = current.getChild(ch)
            if child == None:
                return
            current = child
        return current

def main():
    trie = Trie()
    trie.insert('cat')
    trie.insert('can')
    trie.insert('canada')
    print('Done insertion.')

    print('\nCheck contains')
    print(trie.contains('can'))
    print(trie.contains('ca'))
    print(trie.contains('canadian'))
    print(trie.contains(''))
    print(trie.contains(None))

    print('\nCheck traverse')
    trie2 = Trie()
    trie2.insert('care')
    trie2.traverse()

    print('\nCheck remove')
    trie2.insert('car')
    trie2.remove('care')
    trie2.remove('book')
    trie2.remove('')
    trie2.remove(None)
    print(trie2.contains('car'))
    print(trie2.contains('care'))

    print('\nCheck autocompletion')
    trie3 = Trie()
    trie3.insert('car')
    trie3.insert('card')
    trie3.insert('care')
    trie3.insert('careful')
    trie3.insert('egg')
    print(trie3.findWords('car'))
    print(trie3.findWords('care'))
    print(trie3.findWords('card'))
    print(trie3.findWords('cargo'))
    print(trie3.findWords('c'))
    print(trie3.findWords(''))
    print(trie3.findWords(None))


if __name__ == '__main__':
    main()
