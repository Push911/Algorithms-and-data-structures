import math


"""F = G + H
F: Total cost of the node,
G: Distance between the current node and the start node,
H: Heuristic - estimated distance from the current node to the end node

Distance:
    Manhattan Distance - allowed to move in four directions only (up, down, left, right)
    h = abs(currentCell.x - goal.x) + abs(currentCell.y - goal.y),
    Diagonal Distance - allowed to move in eight directions only (any current cell neighbour)
    h = max(abs(currentCell.x - goal.x) + abs(currentCell.y - goal.y)),
    Euclidean Distance - allowed to move in any direction
    h = sqrt((currentCell.x - goal.x)^2 + (currentCell.y - goal.y)^2)"""


def distance(currentNode, endNode):
    return (currentNode.position[0] - endNode.position[0]) ** 2 + (currentNode.position[1] - endNode.position[1]) ** 2


def manhattan(currentNode, endNode):
    return abs(currentNode.position[0] - endNode.position[0]) + abs(currentNode.position[1] - endNode.position[1])


def euclidean(currentNode, endNode):
    return math.sqrt((currentNode.position[0] - endNode.position[0]) ** 2 +
                     (currentNode.position[1] - endNode.position[1]) ** 2)


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def aStar(maze, start, end):
    startNode = Node(None, start)
    startNode.f = startNode.g = startNode.h = 0
    endNode = Node(None, end)
    endNode.f = endNode.g = endNode.h = 0
    openList = []
    closedList = []
    openList.append(startNode)

    while len(openList) > 0:
        currentNode = openList[0]
        currentNodeIndex = 0
        for index, node in enumerate(openList):
            if node.f < currentNode.f:
                currentNode = node
                currentNodeIndex = index

        openList.pop(currentNodeIndex)
        closedList.append(currentNode)

        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]
        for newPosition in directions:
            nodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

            if (len(maze)) < nodePosition[0] < 0 or (len(maze[0])) < nodePosition[1] < 0:
                continue

            if maze[nodePosition[0]][nodePosition[1]] is "#":
                continue

            newNode = Node(currentNode, nodePosition)

            children.append(newNode)

        for child in children:
            for closedChild in closedList:
                if child is closedChild:
                    continue

            child.g = currentNode.g + 1
            child.h = distance(child, endNode)
            child.f = child.g + child.h

            for openNode in openList:
                if child is openNode and child.g > openNode.g:
                    continue

            openList.append(child)


def printMazePath(maze, moves):
    for move in moves:
        if maze[move[0]][move[1]] is "O":
            continue
        elif maze[move[0]][move[1]] is "X":
            continue
        maze[move[0]][move[1]] = "+"
    return maze


def setStartEndPositions(maze):
    start, end = (), ()
    for rowIndex, row in enumerate(maze):
        for colIndex, col in enumerate(row):
            if col is "O":
                start = (rowIndex, colIndex)
            if col is "X":
                end = (rowIndex, colIndex)
    return start, end


def createCostMaze(maze, currentPosition):
    costMaze = [[0 for _ in range(len(maze))] for _ in range(len(maze[0]))]
    start, end = setStartEndPositions(maze)
    currentNode = Node(None, currentPosition)
    currentNode.g = calculateDestinationToStart(maze, currentPosition)
    endNode = Node(None, end)
    endNode.f = endNode.g = endNode.h = 0
    for row in range(len(maze)):
        for column in range(len(maze[0])):
            if (row, column) != currentPosition and maze[row][column] is not "#":
                pos = (row, column)
                newNode = Node(currentNode, pos)
                newNode.g = currentNode.g + 1
                newNode.h = distance(newNode, endNode)
                newNode.f = newNode.g + newNode.h
                costMaze[row][column] = newNode.f
    return costMaze


def calculateDestinationToStart(maze, currentPosition):
    start, end = setStartEndPositions(maze)
    return max(currentPosition[0] - start[0], currentPosition[1]-start[1])


def main():
    maze = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "O", " ", " ", "#", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", " ", " ", " ", "#", "#", "#", "#", " ", "#"],
            ["#", " ", " ", " ", "#", " ", "X", "#", " ", "#"],
            ["#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]

    start, end = setStartEndPositions(maze)
    path = aStar(maze, start, end)
    mz = printMazePath(maze, path)
    for row in mz:
        for col in row:
            print(col, end=" ")
        print()

    # Cost maze for given current position
    costMaze = createCostMaze(maze, (1, 1))
    for row in costMaze:
        for col in row:
            if len(str(col)) is 1:
                print("", col, end=" ")
            else:
                print(col, end=" ")
        print()


main()
