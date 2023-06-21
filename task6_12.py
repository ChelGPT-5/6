import random

def find_columns(matrix, H):
    with_H = []
    without_H = []
    for j in range(len(matrix[0])):
        if any(matrix[i][j] == H for i in range(len(matrix))):
            with_H.append(j)
        else:
            without_H.append(j)
    return with_H, without_H


M = 5
N = 7
H = 5

matrix = [[random.randint(0, 9) for j in range(N)] for i in range(M)]
print("матрица:")
for row in matrix:
    print(row)
with_H, without_H = find_columns(matrix, H)
print("столбцы с {}: {}".format(H, with_H))
print("столбцы без {}: {}".format(H, without_H))