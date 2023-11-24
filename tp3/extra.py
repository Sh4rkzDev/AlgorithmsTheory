def hittingSetGreedy(b):
    res = set()
    considered = set()
    for idx, subset in enumerate(b):
        if subset in considered: continue
        max = subset[0]
        countMax = 0
        consider = {}
        for elem in subset:
            repeated = 0
            for i in range(idx+1, len(b)):
                if b[i] in considered: continue
                consider[elem] = consider.get(elem, []) + [i]
                for e in b[i]:
                    if e == elem: repeated += 1
            if repeated > countMax:
                countMax = repeated
                max = elem
        for i in consider[max]: considered.add(b[i])
        res.add(max)
    return res
