from queue import PriorityQueue # use Python's build-in Priority Queue class to implement Dijkstra's Algorithm
from Path import Path
# An Object Oriented Implementation
class WeightedGraph:
    def __init__(self):
        self.nodes = {} # key: label; value: Node(label)

    class Node:
        def __init__(self, label):
            self.label = label
            self.edges = [] # a list of edges connected to this node

        def addEdge(self, target, weight):
            self.edges.append(WeightedGraph.Edge(self, target, weight))

        def getEdges(self):
            return self.edges

        def __str__(self):
            return self.label

        def __repr__(self):
            return self.label

    class Edge:
        def __init__(self, fromNode, toNode, weight):
            self.fromNode = fromNode
            self.toNode = toNode
            self.weight = weight

        def __str__(self):
            return '{}-{}->{}'.format(self.fromNode, self.weight, self.toNode)

        def __repr__(self):
            return '{}-{}->{}'.format(self.fromNode, self.weight, self.toNode)

    def addNode(self, label):
        self.nodes[label] = self.nodes.get(label, self.Node(label))

    def addEdge(self, from_node, to_node, weight):
        fromNode = self.nodes.get(from_node)
        toNode = self.nodes.get(to_node)
        if not fromNode or not toNode:
            raise Exception('Invalid node(s).')

        fromNode.addEdge(toNode, weight)
        toNode.addEdge(fromNode, weight)

    def print(self):
        for node in self.nodes.values():
            edges = node.getEdges()
            if bool(edges):
                print('{} has edge(s) {}'.format(node, edges))

    def getShortestDistance(self, from_node, to_node):
        fromNode = self.nodes[from_node]
        toNode = self.nodes[to_node]
        if not fromNode or not toNode:
            raise Exception('Invalid node(s).')

        distances = {}
        for node in self.nodes.values():
            distances[node] = float('inf')
        distances[fromNode] = 0

        visited = set()

        queue = PriorityQueue()
        queue.put((0, fromNode))

        while not queue.empty():
            current = queue.get()[1]
            visited.add(current)

            for edge in current.getEdges():
                if edge.toNode in visited:
                    continue
                newDistance = distances[current] + edge.weight
                if newDistance < distances[edge.toNode]:
                    distances[edge.toNode] = newDistance
                    queue.put((newDistance, edge.toNode))

        return distances[self.nodes[to_node]]

    def getShortestPath(self, from_node, to_node):
        fromNode = self.nodes[from_node]
        toNode = self.nodes[to_node]
        if not fromNode or not toNode:
            raise Exception('Invalid node(s).')

        distances = {}
        for node in self.nodes.values():
            distances[node] = float('inf')
        distances[fromNode] = 0

        previousNodes = {}

        visited = set()

        queue = PriorityQueue()
        queue.put((0, fromNode))

        while not queue.empty():
            current = queue.get()[1]
            visited.add(current)

            for edge in current.getEdges():
                if edge.toNode in visited:
                    continue
                newDistance = distances[current] + edge.weight
                if newDistance < distances[edge.toNode]:
                    distances[edge.toNode] = newDistance
                    previousNodes[edge.toNode] = current
                    queue.put((newDistance, edge.toNode))

        return self.__buildPath(previousNodes, toNode)

    def __buildPath(self, previousNodes, toNode):
        stack = []
        stack.append(toNode)
        previous = previousNodes.get(toNode)
        #print(toNode, previous, previousNodes)
        while previous:
            stack.append(previous)
            previous = previousNodes.get(previous)

        path = Path()
        while stack:
            path.add(stack.pop().label)

        return path

    def hasCycle(self):
        visited = set()
        for node in self.nodes.values():
            if node not in visited and \
                self.__hasCycle(node, None, visited):
                return True
        return False

    def __hasCycle(self, node, parent, visited):
        visited.add(node)
        for edge in node.getEdges():
            if edge.toNode == parent:
                continue
            if edge.toNode in visited or \
               self.__hasCycle(edge.toNode, node, visited):
                return True
        return False

    def getMinimumSpanningTree(self):
        tree = WeightedGraph()

        if not self.nodes:
            return tree

        edges = PriorityQueue()
        startNode = next(iter(self.nodes.values()))
        tree.addNode(startNode.label)
        for edge in startNode.getEdges():
            edges.put((edge.weight, edge))

        if edges.empty():
            return tree

        while len(tree.nodes) < len(self.nodes):
            minEdge = edges.get()[1]
            nextNode = minEdge.toNode
            if tree.containsNode(nextNode.label):
                continue
            tree.addNode(nextNode.label)
            tree.addEdge(minEdge.fromNode.label, nextNode.label, minEdge.weight)

            for edge in nextNode.getEdges():
                if not tree.containsNode(edge.toNode.label):
                    edges.put((edge.weight, edge))

        return tree

    def containsNode(self, label):
        return label in self.nodes.keys()

graph = WeightedGraph()
graph.addNode('A')
graph.addNode('B')
graph.addNode('C')
graph.addEdge('A', 'B', 3)
graph.addEdge('A', 'C', 2)
graph.print()

print('\nShortest Distance and Path')
graph2 = WeightedGraph()
graph2.addNode('A')
graph2.addNode('B')
graph2.addNode('C')
graph2.addEdge('A', 'B', 1)
graph2.addEdge('A', 'C', 10)
graph2.addEdge('B', 'C', 2)
graph2.print()
print('Shortest distance between A and C:', graph2.getShortestDistance('A', 'C'))
print('Shortest path between A and C:', graph2.getShortestPath('A', 'C'))

print('\nCheck Cycle Detection')
graph2 = WeightedGraph()
graph2.addNode('A')
graph2.addNode('B')
graph2.addNode('C')
graph2.addEdge('A', 'B', 1)
graph2.addEdge('A', 'C', 10)
graph2.print()
print(graph2.hasCycle())
graph2.addEdge('B', 'C', 5)
graph2.print()
print(graph2.hasCycle())

print('\nMinimum Spanning Tree')
graph3 = WeightedGraph()
graph3.addNode('A')
graph3.addNode('B')
graph3.addNode('C')
graph3.addNode('D')
graph3.addEdge('A', 'B', 3)
graph3.addEdge('B', 'D', 4)
graph3.addEdge('C', 'D', 5)
graph3.addEdge('A', 'C', 1)
graph3.addEdge('B', 'C', 2)
graph3.print()
print('\nThe tree is:')
tree = graph3.getMinimumSpanningTree()
tree.print()


def main():
    pass

if __name__ == '__main__':
    main()
