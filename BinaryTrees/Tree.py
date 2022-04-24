# Tree
# Node (value, leftChild, rightChild)
# insert(value)
# find(value) -> boolean
class Node:
    def __init__(self, value, leftChild = None, rightChild = None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild

    def __str__(self):
        return 'Node={}'.format(self.value)

    def __repr____(self):
        return 'Node={}'.format(self.value)

class Tree:
    def __init__(self, root = None):
        self.root = root

    def insert(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.leftChild == None:
                    current.leftChild = node
                    break
                current = current.leftChild
            else:
                if current.rightChild == None:
                    current.rightChild = node
                    break
                current = current.rightChild

    def find(self, value):
        current = self.root
        while current:
            if value < current.value:
                current = current.leftChild
            elif value > current.value:
                current = current.rightChild
            else:
                return True
        return False

    def height(self):
        return self.__height(self.root)

    def __height(self, root):
        if root == None:
            rturn -1
        if self.__isLeaf(root):
            return 0
        return 1 + max(self.__height(root.leftChild),
                       self.__height(root.rightChild))

    def min_BST(self): # O(log n)
        if self.root == None:
            raise Exception('Empty tree.')
        current = self.root
        last = current
        while current != None:
            last = current
            current = current.leftChild
        return last.value

    def min(self): # O(n)
        return self.__min(self.root)

    def __min(self, root):
        if self.__isLeaf(root):
            return root.value
        left = self.__min(root.leftChild)
        right = self.__min(root.rightChild)
        return min(left, right, root.value)

    def __isLeaf(self, node):
        return node.leftChild == None and node.rightChild == None

    def traversePreOrder(self):
        self.__traversePreOrder(self.root)

    def traverseInOrder(self):
        self.__traverseInOrder(self.root)

    def traversePostOrder(self):
        self.__traversePostOrder(self.root)

    def __traversePreOrder(self, root):
        if not root:
            return
        # root -> left -> right
        print(root.value)
        self.__traversePreOrder(root.leftChild)
        self.__traversePreOrder(root.rightChild)

    def __traverseInOrder(self, root):
        if not root:
            return
        # left -> root -> right
        self.__traverseInOrder(root.leftChild)
        print(root.value)
        self.__traverseInOrder(root.rightChild)

    def __traversePostOrder(self, root):
        if not root:
            return
        # left -> right -> root
        self.__traversePostOrder(root.leftChild)
        self.__traversePostOrder(root.rightChild)
        print(root.value)

    def equals(self, other):
        if other == None:
            return False
        return self.__equals(self.root, other.root)

    def __equals(self, first, second): # pre-order traversal
        if first == None and second == None:
            return True
        if first != None and second != None:
            return first.value == second.value and \
                   self.__equals(first.leftChild, second.leftChild) and \
                   self.__equals(first.rightChild, second.rightChild)
        return False

    def isBST(self):
        return self.__isBST(self.root, float('-inf'), float('inf'))

    def __isBST(self, node, min_val, max_val):
        if node == None:
            return True
        if node.value < min_val or node.value > max_val:
            return False

        return self.__isBST(node.leftChild, min_val, node.value) and \
               self.__isBST(node.rightChild, node.value, max_val)

    def swapRoot(self):
        self.root.leftChild, self.root.rightChild = \
        self.root.rightChild, self.root.leftChild

    def nodesAtDistance(self, distance):
        self.__nodesAtDistance(self.root, distance)

    def __nodesAtDistance(self, node, distance):
        if node == None:
            return
        if distance == 0:
            print(node.value)
            return
        self.__nodesAtDistance(node.leftChild, distance - 1)
        self.__nodesAtDistance(node.rightChild, distance - 1)

    def nodesListAtDistance(self, distance):
        nodes_list = []
        self.__nodesListAtDistance(self.root, distance, nodes_list)
        return nodes_list

    def __nodesListAtDistance(self, node, distance, nodes_list):
        if node == None:
            return
        if distance == 0:
            nodes_list.append(node.value)
            return
        self.__nodesListAtDistance(node.leftChild, distance - 1, nodes_list)
        self.__nodesListAtDistance(node.rightChild, distance - 1, nodes_list)

    def traverseLevelOrder(self):
        i = 0
        while i <= self.height():
            nodes_list = self.nodesListAtDistance(i)
            for node in nodes_list:
                print(node)
            i += 1

def main():
    tree = Tree()
    tree.insert(7)
    tree.insert(4)
    tree.insert(9)
    tree.insert(1)
    tree.insert(6)
    tree.insert(8)
    tree.insert(10)
    print('done')
    print(tree.find(10))
    # print(tree.find(11))
    print('\nPre-order traversal:')
    tree.traversePreOrder()
    print('\nIn-order traversal:')
    tree.traverseInOrder()
    print('\nPost-order traversal:')
    tree.traversePostOrder()
    print('\nHeight of tree:', tree.height())
    print('\nMinimum value in the tree:', tree.min())

    tree2 = Tree()
    tree2.insert(7)
    tree2.insert(4)
    tree2.insert(9)
    tree2.insert(1)
    tree2.insert(6)
    tree2.insert(8)
    tree2.insert(10)
    print('Equal?', tree.equals(tree2))
    print('Is BST?', tree.isBST())
    tree.swapRoot()
    print('Is BST?', tree.isBST())
    tree.swapRoot()
    print('Nodes at distance 0:')
    tree.nodesAtDistance(0)
    print('Nodes at distance 1:')
    tree.nodesAtDistance(1)
    print('Nodes at distance 2:')
    tree.nodesAtDistance(2)
    print('Nodes at distance 5:')
    tree.nodesAtDistance(5)
    print('Nodes list at distance 0:', tree.nodesListAtDistance(0))
    print('Nodes list at distance 1:', tree.nodesListAtDistance(1))
    print('Nodes list at distance 2:', tree.nodesListAtDistance(2))
    print('Nodes list at distance 5:', tree.nodesListAtDistance(5))
    print('\nLevel order traversal:')
    tree.traverseLevelOrder()

if __name__ == '__main__':
    main()
