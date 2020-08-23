from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

"""F = G + H
F: Total cost of the node,
G: Distance between the current node and the start node,
H: Heuristic - estimated distance from the current node to the end node"""


matrix = [
  [1, 1, 1, 1],
  [1, 0, 1, 0],
  [1, 1, 1, 1]
]

grid = Grid(matrix=matrix)
start = grid.node(0, 0)
end = grid.node(3, 2)
# finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
finder = AStarFinder()
path, runs = finder.find_path(start, end, grid)
print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))
