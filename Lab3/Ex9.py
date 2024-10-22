# Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field. Example:
# # FIELD
# [[1, 2, 3, 2, 1, 1],
#  [2, 4, 4, 3, 7, 2],
#  [5, 5, 2, 5, 6, 4],
#  [6, 6, 7, 6, 7, 5]]
# Will return : [(2, 2), (3, 4), (2, 4)]
def find_blocked_spectators(matrix):
    blocked_spectators = []

    for row in range(1, len(matrix)):
        for col in range(len(matrix[0])):
            current_height = matrix[row][col]
            blocked = False
            for previous_row in range(row):
                if matrix[previous_row][col] >= current_height:
                    blocked = True
            if blocked:
                blocked_spectators.append((row, col))

    return blocked_spectators

stadium = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

result = find_blocked_spectators(stadium)
print(result)

