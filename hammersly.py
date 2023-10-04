import random

def generate_grid(width, height):
  """Generates a grid of the given width and height.

  Args:
    width: The width of the grid.
    height: The height of the grid.

  Returns:
    A list of lists, where each sublist represents a row in the grid.
  """

  grid = []
  for i in range(height):
    row = []
    for j in range(width):
      row.append(None)
    grid.append(row)
  return grid

def generate_subgrids(grid, subgrid_width, subgrid_height):
  """Generates sub-grids of the given width and height from the given grid.

  Args:
    grid: The grid to generate sub-grids from.
    subgrid_width: The width of the sub-grids.
    subgrid_height: The height of the sub-grids.

  Returns:
    A list of lists of lists, where each sublist represents a sub-grid in the grid.
  """

  subgrids = []
  for i in range(0, len(grid), subgrid_height):
    subgrid_row = []
    for j in range(0, len(grid[0]), subgrid_width):
      subgrid = []
      for k in range(i, i + subgrid_height):
        for l in range(j, j + subgrid_width):
          subgrid.append(grid[k][l])
      subgrid_row.append(subgrid)
    subgrids.append(subgrid_row)
  return subgrids

def generate_random_point_in_subgrid(subgrid):
  """Generates a random point in the given sub-grid.

  Args:
    subgrid: The sub-grid to generate a random point in.

  Returns:
    A tuple of (x, y) coordinates, where x and y are the coordinates of the random
    point in the sub-grid.
  """

  x = random.randint(0, len(subgrid[0]) - 1)
  y = random.randint(0, len(subgrid) - 1)
  return (x, y)

def generate_randomly_distributed_points(grid_width, grid_height, subgrid_width,
                                          subgrid_height):
  """Generates a set of randomly distributed points in a grid.

  Args:
    grid_width: The width of the grid.
    grid_height: The height of the grid.
    subgrid_width: The width of the sub-grids.
    subgrid_height: The height of the sub-grids.

  Returns:
    A set of randomly distributed points in the grid.
  """

  grid = generate_grid(grid_width, grid_height)
  subgrids = generate_subgrids(grid, subgrid_width, subgrid_height)

  random_points = set()
  for subgrid in subgrids:
    random_point = generate_random_point_in_subgrid(subgrid)
    random_points.add(random_point)

  return random_points

print(random_points = generate_randomly_distributed_points(10, 10, 2, 2))