# rotate matrix 90deg
# with out allocating a new list in memory

def rotate(matrix):
    n = len(matrix) 
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    [mat.sort(reverse=True) for mat in matrix]
    return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))