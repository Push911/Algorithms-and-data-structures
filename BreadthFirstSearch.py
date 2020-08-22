import collections


class SimpleGraph:
	def __init__(self):
		self.edges = {}

	def neighbours(self, id):
		return self.edges[id]


exampleGraph = SimpleGraph()
edges = {
	"A": ["B"],
	"B": ["A", "C", "D"],
	"C": ["A"],
	"D": ["E", "A"],
	"E": ["B"]
}
exampleGraph.edges = edges


class Queue:
	def __init__(self):
		self.elements = collections.deque()

	def isEmpty(self):
		return len(self.elements) == 0

	def set(self, x):
		self.elements.append(x)

	def get(self):
		return self.elements.popleft()


class BreadthFirstSearch:
	def __init__(self, graph, start):
		self.queue = Queue()
		self.graph = graph
		self.queue.set(start)
		self.reached = {start: True}

	def bfs(self):
		while not self.queue.isEmpty():
			current = self.queue.get()
			print(f"Visited {current} node")
			for next in self.graph.neigbours(current):
				if next not in self.reached:
					self.queue.set(next)
					self.reached[next] = True


bfs = BreadthFirstSearch(exampleGraph, "A")
