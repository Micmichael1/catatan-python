# matrix 2D
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix1 = [1,2,3]
print("matrix[0]:",matrix[0])
print("matrix[0][0]:",matrix[0][0])
print(matrix)
print(matrix1)
print("Semua isi matrix 2D:")
for row in matrix:
    for item in row:
        print(item)

# matrix 3D
matrix = [
    # list ke-0
    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ],
    # list ke-1
    [
    [11,12,13],
    [14,15,16],
    [17,18,19]
    ]
]
print("Matrix [0][0][0]: ",matrix[0][0][0])
print("Semua isi matrix 3D:")
for row1 in matrix:
    for row2 in row1:
        for item in row2:
            print(item)