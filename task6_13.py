def sum_diag(matrix):
    sum_main = 0
    sum_side = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                sum_main += matrix[i][j]
            if i + j == len(matrix) - 1:
                sum_side += matrix[i][j]
    return sum_main, sum_side


matrix = [[9, 8, 3], [5, 3, 1], [1, 5, 8]]
sum_main, sum_side = sum_diag(matrix)
print("сумма элементов на главной диагонали:", sum_main)
print("сумма элементов на побочной диагонали:", sum_side)
