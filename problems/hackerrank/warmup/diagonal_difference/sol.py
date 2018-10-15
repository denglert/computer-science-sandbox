def diagonalDifference(arr):

    n = len(arr)

    lr_diag_sum = 0
    rl_diag_sum = 0

    for i in range(n):

        lr_diag_sum = += arr[i][i]
        rl_diag_sum = += arr[i][n-1-i]


    return abs(lr_diag_sum - rl_diag_sum)

