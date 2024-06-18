def get_matrix(n, m, value):
    matrix=[]
    for i in range(n):
        matrix.append(i)
        for j in range(m):
            #принт для дебага
            print(i , j, matrix[i])
            matrix[i] = (j)

    return matrix

result1 = get_matrix(3, 5, 10)
# print(result1)