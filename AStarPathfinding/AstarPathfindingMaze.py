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

        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)]:
            nodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

            if (len(maze)) < nodePosition[0] < 0 or (len(maze[0])) < nodePosition[1] < 0:
                continue

            if maze[nodePosition[0]][nodePosition[1]] != 0:
                continue

            newNode = Node(currentNode, nodePosition)

            children.append(newNode)

        for child in children:

            for closedChild in closedList:
                if child is closedChild:
                    continue

            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g + child.h

            for openNode in openList:
                if child == openNode and child.g > openNode.g:
                    continue

            openList.append(child)


def main():
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)
    path = aStar(maze, start, end)
    print(path)


main()
