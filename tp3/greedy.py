from time import time
import input

def hittingSetGreedy(b):
    res = []
    considered = set()
    for idx, subset in enumerate(b):
        if subset in considered: continue
        maxElem = subset[0]
        countMax = 0
        consider = {}
        for elem in subset:
            consider[elem] = []
            repeated = 0
            for i in range(idx+1, len(b)):
                if b[i] in considered: continue
                for e in b[i]:
                    if e == elem:
                        repeated += 1
                        consider[elem] = consider[elem] + [i]
                        break
            if repeated > countMax:
                countMax = repeated
                maxElem = elem
        for i in consider[maxElem]:
            considered.add(b[i])
        res.append(maxElem)
    return res

def main():
    b = input.ReadInputs()
    start = time()
    sol = hittingSetGreedy(b)
    end = time()
    print("The solution using Greedy algorithm took ", end-start, "sec")
    print("Size of solution: ", len(sol))
    print(', '.join(sol))

if __name__ == "__main__":
    main()

