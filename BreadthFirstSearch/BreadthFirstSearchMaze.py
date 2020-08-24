import queue

"""bfs(start, looking_for)
	create arrays (node_queue, visited_nodes, and traveled_path)
	add the start to the arrays
	while the queue is not empty
		take out the first element in the queue
		for each of the neighbors of this first element 
			if its not in the visited set and not blocked
				add this to the arrays
				if this contains what we are looking for
					return the backtrack of this node
				end if
			end if
		end for
	end while
end method"""


class Maze:
	def __init__(self):
		self.maze = []
		self.startPosition = []
		self.endPosition = []
		self.bfs()

	def createMaze(self):
		self.maze = [["#", "#", "#", "#", "#", "O", "#"],
		             ["#", " ", " ", " ", "#", " ", "#"],
		             ["#", " ", "#", " ", "#", " ", "#"],
		             ["#", " ", "#", " ", " ", " ", "#"],
		             ["#", " ", "#", "#", "#", " ", "#"],
		             ["#", " ", " ", " ", "#", " ", "#"],
		             ["#", "#", "#", "#", "#", "X", "#"]]

	def setStartEndPositions(self):
		rowNumber, columnNumber = -1, -1
		for row in self.maze:
			columnNumber = -1
			rowNumber += 1
			for column in row:
				columnNumber += 1
				if column == "O":
					self.startPosition = [rowNumber, columnNumber]
				if column == "X":
					self.endPosition = [rowNumber, columnNumber]

	def printMaze(self, moves):
		self.setStartEndPositions()
		currentPosition = self.startPosition

		for move in moves:
			if move is "L":
				currentPosition[1] -= 1
			elif move is "R":
				currentPosition[1] += 1
			elif move is "U":
				currentPosition[0] -= 1
			elif move is "D":
				currentPosition[0] += 1

			if self.maze[currentPosition[0]][currentPosition[1]] is not "O":
				if self.maze[currentPosition[0]][currentPosition[1]] is not "X":
					self.maze[currentPosition[0]][currentPosition[1]] = "+"

		for row in self.maze:
			print(row)

	def moveIsValid(self, moves):
		self.setStartEndPositions()
		currentPosition = self.startPosition
		for move in moves:
			if move is "L":
				currentPosition[1] -= 1
			elif move is "R":
				currentPosition[1] += 1
			elif move is "U":
				currentPosition[0] -= 1
			elif move is "D":
				currentPosition[0] += 1

			if not (0 <= currentPosition[1] < len(self.maze[0]) and 0 <= currentPosition[0] < len(self.maze)):
				return False
			elif self.maze[currentPosition[0]][currentPosition[1]] is "#":
				return False

		return True

	def findEnd(self, moves):
		self.setStartEndPositions()
		currentPosition = self.startPosition

		for move in moves:
			if move is "L":
				currentPosition[1] -= 1
			elif move is "R":
				currentPosition[1] += 1
			elif move is "U":
				currentPosition[0] -= 1
			elif move is "D":
				currentPosition[0] += 1

		if currentPosition == self.endPosition:
			print("Found: ", moves)
			self.printMaze(moves)
			return True

		return False

	def bfs(self):
		self.createMaze()
		path = queue.Queue()
		path.put("")
		add = ""
		while not self.findEnd(add):
			add = path.get()
			for direction in ["L", "R", "U", "D"]:
				tried = add + direction
				if self.moveIsValid(tried):
					path.put(tried)


mz = Maze()
