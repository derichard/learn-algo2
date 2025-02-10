def edit_distance(str1, str2):
    matrix = []
    for i in range(len(str1) + 1):
        row = []
        for j in range(len(str2) + 1):
            row.append(0)
        matrix.append(row)

    for i in range(len(matrix)):
        for j in range(len(row)):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
                
    return matrix[i][j]