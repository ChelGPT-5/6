import random

def create_random_matrix(rows, cols):
    matrix = [[random.randint(0, 9) for j in range(cols)] for i in range(rows)]
    return matrix


matrix = create_random_matrix(3, 4)
print(matrix)