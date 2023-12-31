def getWorkOut(earn, energy):
    matrix = []

    for idx, e in enumerate(earn):
        arr = [0] * len(energy)
        for i in range(idx+1):
            gain = min(e, energy[i])
            if i == 0:
                arr[i] = matrix[idx-2][idx-2] + gain if idx > 1 else gain
                continue
            contWorkOut = matrix[idx-1][i-1] + gain if idx > 0 else 0
            lastWorkOut = arr[i-1]
            arr[i] = max(contWorkOut, lastWorkOut)
        matrix.append(arr)

    print("Highest possible profit: ", matrix[len(earn)-1][len(energy)-1])
    return matrix
