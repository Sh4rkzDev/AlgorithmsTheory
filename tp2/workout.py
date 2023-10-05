import input

def binary_search(arr, left, right):
    med = (left + right) // 2
    if arr[med] != 0 and arr[med+1] == 0: return arr[med]
    if arr[med] == 0:
        return binary_search(arr, left, med)
    return binary_search(arr, med, right)

def getWorkOut(earn, energy):
    matrix = []

    for idx, e in enumerate(earn):
        arr = [0] * len(energy)
        for i in range(idx+1):
            gain = min(e, energy[i])
            if i == 0:
                prevTwoDays = binary_search(matrix[idx-2], 0, len(matrix[idx-2])) + gain if idx > 1 else 0
                arr[i] = max(prevTwoDays, gain)
                continue
            contWorkOut = matrix[idx-1][i-1] + gain if idx > 0 else 0
            lastWorkOut = arr[i-1] if i > 0 else 0
            arr[i] = max(contWorkOut, lastWorkOut)
        matrix.append(arr)

    return matrix

def main():
    earn, energy = input.ReadInputs()
    getWorkOut(earn, energy)

if __name__ == "__main__":
    main()
