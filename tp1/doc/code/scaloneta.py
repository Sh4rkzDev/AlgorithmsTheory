import input

def main(data = None):
    params = []
    if not data:
        params = input.ReadInputs()
    else:
        params = data
    params.sort(key = lambda item: 1/item[1])

    total, longest, actual = 0, 0, 0
    for t in params:
        total += t[0]
        actual = total + t[1]
        if actual > longest:
            longest = actual
    print("It took: " , longest , "hs")
    return longest

if __name__ == "__main__":
    main()
