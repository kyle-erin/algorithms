def zero_matrix(arr):
    cols = {}
    rows = {}

    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == 0:
                cols[i] = True
                rows[j] = True

    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if i in cols or j in rows:
                arr[i][j] = 0

a = [[2, 3, 4, 7, 1], [1, 1, 5, 1, 1], [5, 4, 2, 3, 0]]
print(a)
zero_matrix(a)
print(a)
