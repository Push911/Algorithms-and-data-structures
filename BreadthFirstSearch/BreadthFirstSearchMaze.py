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

maze = []


def createMaze():
	maze.append(["#", "#", "#", "#", "#", "O", "#"])
	maze.append(["#", " ", " ", " ", "#", " ", "#"])
	maze.append(["#", " ", "#", " ", "#", " ", "#"])
	maze.append(["#", " ", "#", " ", " ", " ", "#"])
	maze.append(["#", " ", "#", "#", "#", " ", "#"])
	maze.append(["#", " ", " ", " ", "#", " ", "#"])
	maze.append(["#", "#", "#", "#", "#", "X", "#"])


def setStartEndPositions():
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


def printMaze(moves):
	startPosition, _ = setStartEndPositions()
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


def moveIsValid(moves):
	startPosition, _ = setStartEndPositions()
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
		print(path, moves, currentPosition, "maze")
		return False

	return True


def findEnd(moves):
	startPosition, endPosition = setStartEndPositions()
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

	print(currentPosition, endPosition)
	if currentPosition == endPosition:
		print("Found: ", moves)
		printMaze(moves)
		return True

	return False


createMaze()
start, end = setStartEndPositions()
print(start, end)
path = ""
add = ""
while not findEnd(add):
	add = path
	for direction in ["L", "R", "U", "D"]:
		tried = add + direction
		print("MM:", tried, "A:", add, "MP:", path)
		# print(maze.maze[maze.moves[0], [maze.moves[1]]])
		if moveIsValid(tried):
			path = tried
			print("Valid:", direction, "MM:", path)
			print(printMaze(path))
