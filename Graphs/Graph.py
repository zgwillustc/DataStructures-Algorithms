# Graph
#       Node
#              label:
#       addNode(label)
#       removeNode(label)
#       addEdge(from, to)
#       removeEdge(from, to)
#       print()
#               A is connected with [B, C]
#               B is connected with [A]
#               C is connected with [A]

class Graph:
    def __init__(self):
        self.nodes = {} # key: label; value: Node(label)
        self.adjacencyList = {} # key: Node(label) ; value: list of neighbors

    class Node:
        def __init__(self, label):
            self.label = label

        def __str__(self):
            return self.label

        def __repr__(self):
            return self.label

    def addNode(self, label):
        node = self.Node(label)
        self.nodes[label] = self.nodes.get(label, node)
        self.adjacencyList[node] = self.adjacencyList.get(node, [])

    def removeNode(self, label):
        node = self.nodes.get(label)
        if not node:
            return
        self.nodes.pop(label)
        self.adjacencyList.pop(node)
        for targets in self.adjacencyList.values():
            try:
                targets.remove(node)
            except:
                pass

    def addEdge(self, from_node, to_node):
        fromNode = self.nodes.get(from_node)
        toNode = self.nodes.get(to_node)
        if not fromNode or not toNode:
            raise Exception('Invalid node(s).')

        self.adjacencyList[fromNode].append(toNode)
        # add below if Undirected Graph
        # self.adjacencyList[toNode].append(fromNode)

    def removeEdge(self, from_node, to_node):
        fromNode = self.nodes.get(from_node)
        toNode = self.nodes.get(to_node)
        if not fromNode or not toNode:
            return

        try:
            self.adjacencyList[fromNode].remove(toNode)
        except:
            pass

    def print(self):
        for source, targets in self.adjacencyList.items():
            if bool(targets):
                print('{} is connected to {}'.format(source, targets))

    def traverseDepthFirst(self, label): # Recursion
        node = self.nodes.get(label)
        if not node:
            return
        visited = set()
        self.__traverseDepthFirst(node, visited)

    def __traverseDepthFirst(self, root, visited):
        print(root)
        visited.add(root)

        adjacencyList = self.adjacencyList.get(root)
        for node in adjacencyList:
            if node not in visited:
                self.__traverseDepthFirst(node, visited)

    def traverseDepthFirst_iter(self, label): # Iteration
        node = self.nodes.get(label)
        if not node:
            return

        stack, visited = [], set()
        stack.append(node)
        while stack:
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.add(current)

            for neighbor in self.adjacencyList.get(current):
                if neighbor not in visited:
                    stack.append(neighbor)

    def traverseBreadthFirst(self, label):
        node = self.nodes.get(label)
        if not node:
            return

        queue, visited = [], set()
        queue.append(node)
        while queue:
            current = queue.pop(0)
            if current not in visited:
                print(current)
                visited.add(current)

            for neighbor in self.adjacencyList.get(current):
                if neighbor not in visited:
                    queue.append(neighbor)

    def topologicalSort(self) -> list:
        stack, visited = [], set()
        for node in self.nodes.values():
            self.__topologicalSort(node, stack, visited)

        sorted_res = []
        while stack:
            sorted_res.append(stack.pop())

        return sorted_res

    def __topologicalSort(self, node, stack, visited):
        if node in visited:
            return
        visited.add(node)

        for neighbor in self.adjacencyList.get(node):
            self.__topologicalSort(neighbor, stack, visited)

        stack.append(node)

    def hasCycle(self) -> bool:
        all_nodes = set(self.nodes.values())
        visiting, visited = set(), set()
        while all_nodes:
            current = next(iter(all_nodes))
            if self.__hasCycle(current, all_nodes, visiting, visited):
                return True
        return False

    def __hasCycle(self, node, all_nodes, visiting, visited):
        all_nodes.remove(node)
        visiting.add(node)

        for neighbor in self.adjacencyList.get(node):
            if neighbor in visited:
                continue
            if neighbor in visiting:
                return True
            if self.__hasCycle(neighbor, all_nodes, visiting, visited):
                return True
        visiting.remove(node)
        visited.add(node)

        return False

def make_graph():
    graph = Graph()
    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addNode('D')
    graph.addEdge('A', 'B')
    graph.addEdge('A', 'C')
    graph.addEdge('A', 'D')
    graph.addEdge('B', 'D')
    graph.addEdge('C', 'D')
    graph.addEdge('B', 'C')
    graph.addEdge('D', 'B')
    graph.addEdge('D', 'C')
    return graph

graph = make_graph()
graph.print()
print('\nCheck remove edge')
graph.removeEdge('D', 'C')
graph.print()

print('\nCheck remove node')
graph.removeNode('C')
graph.print()

def make_graph2():
    graph = Graph()
    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addNode('D')
    graph.addEdge('A', 'B')
    graph.addEdge('A', 'C')
    graph.addEdge('D', 'C')
    graph.addEdge('B', 'D')
    return graph

print('\n')
graph2 = make_graph2()
graph2.print()
print('\nCheck Depth First Traversal using recursion')
graph2.traverseDepthFirst('A')
graph2.traverseDepthFirst('E')
print('\nCheck Depth First Traversal using iteration')
graph2.traverseDepthFirst_iter('A')
print('\nCheck Breadth First Traversal')
graph2.traverseBreadthFirst('A')

def make_graph3():
    graph = Graph()
    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('X')
    graph.addNode('P')
    graph.addEdge('A', 'P')
    graph.addEdge('B', 'P')
    graph.addEdge('X', 'A')
    graph.addEdge('X', 'B')
    return graph

print('\nCheck Topological Sort')
graph3 = make_graph3()
graph3.print()
print(graph3.topologicalSort())

def make_graph4():
    graph = Graph()
    graph.addNode('A')
    graph.addNode('B')
    graph.addNode('C')
    graph.addEdge('A', 'B')
    graph.addEdge('B', 'C')
    graph.addEdge('C', 'A')
    return graph

print('\nCheck Cycle Detection')
graph4 = make_graph4()
graph4.print()
print(graph4.hasCycle())

def main():
    pass

if __name__ == '__main__':
    main()
