matrix = [
    ["7", "i", "3"],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", "#", " "],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]

rows_num = len(matrix)
columns_num = len(matrix[0])
matrix_string = " "
symbols_num = 0

for col in range(columns_num):
    for row in range(rows_num):
        if matrix[row][col].isalpha():
            matrix_string += matrix[row][col]
            symbols_num = 0
        else:
            symbols_num += 1
            if symbols_num == 2:
                matrix_string += " "

print(matrix_string)
