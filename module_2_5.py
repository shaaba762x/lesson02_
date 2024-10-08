def getMatrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

res_1 = getMatrix(2, 3, 9)
res_2 = getMatrix(3, 5, 41)
res_3 = getMatrix(4, 2, 11)
print(res_1)
print(res_2)
print(res_3)