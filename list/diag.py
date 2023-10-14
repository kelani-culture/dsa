def diagonal_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][n-i-1]
        
    return total

lst2D = [[1, 2, 3], 
         [4, 5, 6],
         [7, 8, 9]]

print(diagonal_sum(lst2D))