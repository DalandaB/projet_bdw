

def grille():
    grid = []
    for row in range(8):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(9):
            grid[row].append(0)  # Append a cell
    #J'avais confondu == avec =
    for row in range(1,7):
        if row == 1 or row == 6:
            for column in range(1,8,4):
                grid[row][column] = 1
                grid[row][column + 1] = 1
                #grid[row][column+1] = 1
        else:
            for column in range (1,8,2): 
                grid[row][column] = 1

    grid[3][2] = 1 
    grid[4][2] = 1 
    # Vérifiez les dimensions de la grille
    assert len(grid) == 8 and all(len(row) == 9 for row in grid), "Grille incorrecte"
    return grid


tableau = grille()
print(tableau)

#le problème c'était l'indentation