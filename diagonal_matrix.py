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


#calculate left to right diagonal summ
#calculate right to left diagonal summ
#return different between them

def diagonalDifference(arr):
    # Write your code here
    nrows = len(arr)
    ncols = len(arr[0])

    index = lcount = rcount = 0
    #left to right
    while index < nrows:
        lcount += arr[index][index]
        index += 1
    index = 0
    rindex = (nrows - 1)
    while index < ncols:
        rcount += arr[index] [rindex]
        index += 1
        rindex -= 1

    if lcount > rcount:
        return lcount - rcount
    if lcount < rcount:
        return rcount - lcount
    else:
        return 0
