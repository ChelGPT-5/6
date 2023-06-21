def add_col(matrix):
    for i in range(len(matrix)):
        if matrix[i].count(1) % 2 == 1:
            matrix[i].append(1)
        else:
            matrix[i].append(0)
    return matrix


matrix = [
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 1, 1, 1]
]

new_matrix = add_col(matrix)
for row in new_matrix:
    print(row)
