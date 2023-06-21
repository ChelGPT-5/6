def find_min_max(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    min_elem = matrix[0][0]
    max_elem = matrix[0][0]
    min_i, min_j = 0, 0
    max_i, max_j = 0, 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] < min_elem:
                min_elem = matrix[i][j]
                min_i, min_j = i, j
            elif matrix[i][j] > max_elem:
                max_elem = matrix[i][j]
                max_i, max_j = i, j
    print("Минимальный элемент:", min_elem, "Индексы:", min_i, min_j)
    print("Максимальный элемент:", max_elem, "Индексы:", max_i, max_j)


matrix = [[2, 49, 12], [7, 46, 14], [22, 75, 45]]
find_min_max(matrix)