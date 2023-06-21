def matrix_sum(matrix):
    total_sum = 0
    column_sums = [0] * len(matrix[0])
    for row in matrix:
        for i, val in enumerate(row):
            total_sum += val
            column_sums[i] += val
    column_percents = [round(col_sum/total_sum * 100, 2) for col_sum in column_sums]
    return total_sum, column_percents


matrix = [[2, 9, 3], [1, 7, 6], [5, 5, 1]]
total_sum, column_percents = matrix_sum(matrix)
print("Сумма :", total_sum)
print("% :", column_percents)
