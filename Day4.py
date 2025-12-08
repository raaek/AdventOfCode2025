import numpy as np

paper_matrix = []
with open("day4_input.txt") as file:
    for line in file.readlines():
        clean_line = line.replace(".", "0").replace("@", "1")
        row = [int(element) for element in clean_line.rstrip()]
        paper_matrix.append(row)

matrix = np.array(paper_matrix)
print(matrix)
padded = np.pad(matrix, [(1, 1), (1, 1)], mode="constant", constant_values=0)
print(padded)


def add_eight_neighbours(matrix_element: tuple) -> int:
    (x, y) = matrix_element
    submatrix = padded[x - 1 : x + 2, y - 1 : y + 2]
    sum = submatrix.sum() - submatrix[1][1]
    return sum


paper_rolls_with_less_than_four_neighbours: int = 0

for row_index in range(1, padded.shape[0] - 1):
    for column_index in range(1, padded.shape[0] - 1):
        coordinate = (row_index, column_index)
        if padded[row_index][column_index] == 1:
            sum = add_eight_neighbours(coordinate)
            if sum < 4:
                paper_rolls_with_less_than_four_neighbours += 1

print(paper_rolls_with_less_than_four_neighbours)
