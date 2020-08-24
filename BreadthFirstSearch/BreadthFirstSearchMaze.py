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


def createMaze():
	maze = [["#", "#", "#", "#", "#", "O", "#"],
	        ["#", " ", " ", " ", "#", " ", "#"],
	        ["#", " ", "#", " ", "#", " ", "#"],
	        ["#", " ", "#", " ", " ", " ", "#"],
	        ["#", " ", "#", "#", "#", "#", "#"],
	        ["#", " ", " ", " ", " ", " ", "#"],
	        ["#", "#", "#", "#", "#", "X", "#"]]
	return maze


def setStartEndPositions(maze):
	startPosition, endPosition = [], []
	rowNumber, columnNumber = -1, -1
	for row in maze:
		columnNumber = -1
		rowNumber += 1
		for column in row:
			columnNumber += 1
			if column == "O":
				startPosition = [rowNumber, columnNumber]
			if column == "X":
				endPosition = [rowNumber, columnNumber]
	return startPosition, endPosition


def printMaze(maze, moves):
	startPosition, _ = setStartEndPositions(maze)
	currentPosition = startPosition

	for move in moves:
		if move is "L":
			currentPosition[1] -= 1
		elif move is "R":
			currentPosition[1] += 1
		elif move is "U":
			currentPosition[0] -= 1
		elif move is "D":
			currentPosition[0] += 1

		if maze[currentPosition[0]][currentPosition[1]] is not "O":
			if maze[currentPosition[0]][currentPosition[1]] is not "X":
				maze[currentPosition[0]][currentPosition[1]] = "+"

	for row in maze:
		print(row)


def moveIsValid(maze, moves):
	startPosition, _ = setStartEndPositions(maze)
	currentPosition = startPosition
	for move in moves:
		if move is "L":
			currentPosition[1] -= 1
		elif move is "R":
			currentPosition[1] += 1
		elif move is "U":
			currentPosition[0] -= 1
		elif move is "D":
			currentPosition[0] += 1

		if not (0 <= currentPosition[1] < len(maze[0]) and 0 <= currentPosition[0] < len(maze)):
			return False
		elif maze[currentPosition[0]][currentPosition[1]] is "#":
			return False

	return True


def findEnd(maze, moves):
	startPosition, endPosition = setStartEndPositions(maze)
	currentPosition = startPosition

	for move in moves:
		if move is "L":
			currentPosition[1] -= 1
		elif move is "R":
			currentPosition[1] += 1
		elif move is "U":
			currentPosition[0] -= 1
		elif move is "D":
			currentPosition[0] += 1

	if currentPosition == endPosition:
		print("Found: ", moves)
		printMaze(maze, moves)
		return True

	return False


mz = createMaze()
start, end = setStartEndPositions(mz)
path = queue.Queue()
path.put("")
add = ""
while not findEnd(mz, add):
	add = path.get()
	for direction in ["L", "R", "U", "D"]:
		tried = add + direction
		# print("MM:", tried, "A:", add, "MP:", path)
		# print(maze.maze[maze.moves[0], [maze.moves[1]]])
		if moveIsValid(mz, tried):
			path.put(tried)
		# print("Valid:", direction, "MM:", path)
