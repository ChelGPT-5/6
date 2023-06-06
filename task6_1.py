def binary_search(arr, val):
    if len(arr) == 0:
        return -1 # элемент не найден
    else:
        mid = len(arr) // 2
        if arr[mid] == val:
            return mid # элемент найден
        elif val < arr[mid]:
            # поиск в левой половине списка
            return binary_search(arr[:mid], val)
        else:
            # поиск в правой половине списка
            result = binary_search(arr[mid+1:], val)
            if result == -1:
                return -1 # элемент не найден
            else:
                return mid + result + 1


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
val = int(input("введите число "))
pos = binary_search(arr, val)
if pos == -1:
    print("Элемент отсутствует")
else:
    print(f"позиция элемента = {pos + 1}")