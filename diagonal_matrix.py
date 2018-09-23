def diagonal_matrix(matrix):
    matrix_len = len(matrix[0])
    print range(matrix_len)
    for i in range(matrix_len):
        print matrix[i][i] 
        
    print range(matrix_len-1,-1,-1)
    for i in range(matrix_len-1,-1,-1):
        print matrix[matrix_len-1-i][i] 

diagonal_matrix([[1,  5,  9,  7],
              [ 6, 3,  5, -2],
              [ -1,  7,  7,  8],
              [7,  1, 3,  4]])