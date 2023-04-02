#Write a program to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 11], [12, 13], [14, 15]]
result = multiply_matrices(matrix1, matrix2)
print(result)