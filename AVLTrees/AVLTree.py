# AVLTree
# AVLNode
# insert() - use recursion

# class AVLTree:
#     def __init__(self, value=None):
#         self.value = value
#         self.leftChild = None
#         self.rightChild = None

#     def insert(self, value):
#         if self.value == None:
#             self.value = value
#             return
#         if value < self.value:
#             if self.leftChild == None:
#                 self.leftChild = AVLTree(value)
#                 return
#             self.leftChild.insert(value)
#         else:
#             if self.rightChild == None:
#                 self.rightChild = AVLTree(value)
#                 return
#             self.rightChild.insert(value)

#     def __str__(self):
#         return 'Node={}'.format(self.value)

class Node:
    def __init__(self, value, leftChild = None, rightChild = None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.height = 0

    def __str__(self):
        return 'Node={}'.format(self.value)

    def __repr____(self):
        return 'Node({})'.format(self.value)

class AVLTree:
    def __init__(self, root = None):
        self.root = root

    def insert(self, value):
        self.root = self.__insert(self.root, value)
    
    def __insert(self, node, value):
        if node == None:
            return Node(value)
        
        if value < node.value:
            node.leftChild = self.__insert(node.leftChild, value)
        else:
            node.rightChild = self.__insert(node.rightChild, value)
        
        self.__setHeight(node)
        
        return self.__balance(node)
    
    def __rotateLeft(self, node):
        newRoot = node.rightChild
        node.rightChild = newRoot.leftChild
        newRoot.leftChild = node
        
        self.__setHeight(node)
        self.__setHeight(newRoot)
        return newRoot
    
    def __rotateRight(self, node):
        newRoot = node.leftChild
        node.leftChild = newRoot.rightChild
        newRoot.rightChild = node
        
        self.__setHeight(node)
        self.__setHeight(newRoot)
        return newRoot
    
    def __setHeight(self, node):
        node.height = 1 + max(self.__height(node.leftChild),
                              self.__height(node.rightChild))
    
    def __balance(self, node):
        if self.__isLeftHeavy(node):
            if self.__balanceFactor(node.leftChild) < 0:
                node.leftChild = self.__rotateLeft(node.leftChild)
            return self.__rotateRight(node)
            
        elif self.__isRightHeavy(node):
            if self.__balanceFactor(node.rightChild) > 0:
                node.rightChild = self.__rotateRight(node.rightChild)
            return self.__rotateLeft(node)
        return node

    def __height(self, node):
        return -1 if node == None else node.height

    def __isLeftHeavy(self, node):
        return self.__balanceFactor(node) > 1
    
    def __isRightHeavy(self, node):
        return self.__balanceFactor(node) < -1
    
    def __balanceFactor(self, node):
        return 0 if node == None else \
               self.__height(node.leftChild) - \
               self.__height(node.rightChild)

avltree = AVLTree()
avltree.insert(1)
avltree.insert(2)
avltree.insert(3)

def main():
    avltree = AVLTree()
    avltree.insert(1)
    avltree.insert(3)
    avltree.insert(2)


if __name__ == '__main__':
    main()
