class Path:
    def __init__(self):
        self.nodes = []

    def add(self, label):
        self.nodes.append(label)

    def __str__(self):
        return str(self.nodes)

    def __repr__(self):
        return self.nodes
