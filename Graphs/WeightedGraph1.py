# WeightedGraph
#       Node
#           - label
#       Edge -> Undirected
#           - from  - Node object
#           - to    - Node object
#           - weight
#       addNode(label)
#       addEdge(from, to, weight)

class WeightedGraph:
    def __init__(self):
        self.nodes = {} # key: label; value: Node(label)
        self.adjacencyList = {} # key: Node(label) ; value: list of Edge(Node)

    class Node:
        def __init__(self, label):
            self.label = label

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
        node = self.Node(label)
        self.nodes[label] = self.nodes.get(label, node)
        self.adjacencyList[node] = self.adjacencyList.get(node, [])

    def addEdge(self, from_node, to_node, weight):
        fromNode = self.nodes.get(from_node)
        toNode = self.nodes.get(to_node)
        if not fromNode or not toNode:
            raise Exception('Invalid node(s).')

        self.adjacencyList[fromNode].append(self.Edge(fromNode, toNode, weight))
        self.adjacencyList[toNode].append(self.Edge(toNode, fromNode, weight))

    def print(self):
        for source, targets in self.adjacencyList.items():
            if bool(targets):
                print('{} has edge(s) {}'.format(source, targets))

graph = WeightedGraph()
graph.addNode('A')
graph.addNode('B')
graph.addNode('C')
graph.addEdge('A', 'B', 3)
graph.addEdge('A', 'C', 2)
graph.print()

def main():
    pass

if __name__ == '__main__':
    main()
