def grid_traveler(m, n):

    grid_matrix =[[ 0 for col in range(n + 1)]
                    for row in range(m + 1)]
    
    grid_matrix[1][1] = 1

    for row in range(m + 1):
        for col in range(n + 1):
            current = grid_matrix[row][col]

            if row != m:    
                #Going down
                grid_matrix[row + 1][col] += current

            if col != n:    
                #Going right
                grid_matrix[row][col + 1] += current
        
    
    
    return grid_matrix[m][n]

print(grid_traveler(3,4))
print(grid_traveler(3,3))
print(grid_traveler(2,3))
print(grid_traveler(18,18))