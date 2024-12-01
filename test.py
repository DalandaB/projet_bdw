grid = []
for row in range(8):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(9):
        grid[row].append(0)

print(grid)