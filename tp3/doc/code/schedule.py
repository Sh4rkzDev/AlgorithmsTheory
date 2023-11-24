def getSchedule(matrix):
    res = [""] * len(matrix)
    i = len(matrix) - 1
    rest = False
    for idx in range(len(matrix)-1, -1, -1):
        if rest:
            res[idx] = "Rest"
            rest = False
            i = idx - 1
            continue
        while i != 0 and matrix[idx][i] == matrix[idx][i-1]:
            i -= 1
        if i == 0: rest = True
        res[idx] = "Train"
        i -= 1
    return res
