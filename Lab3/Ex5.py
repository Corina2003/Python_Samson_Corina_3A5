#Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
def replace(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows):
        for j in range(num_cols):
            if i > j:
                matrix[i][j] = 0

    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = replace(matrix)

for row in result:
    print(row)