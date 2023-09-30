
def asItComes(data):
    total, longest, actual = 0, 0, 0
    for t in data:
        total += t[0]
        actual = total + t[1]
        if actual > longest:
            longest = actual
    return longest

def sortByScaloniAsc(data):
    data.sort(key = lambda item: item[0])
    total, longest, actual = 0, 0, 0
    for t in data:
        total += t[0]
        actual = total + t[1]
        if actual > longest:
            longest = actual
    return longest

def sortByScaloniDesc(data):
    data.sort(key = lambda item: 1/item[0])
    total, longest, actual = 0, 0, 0
    for t in data:
        total += t[0]
        actual = total + t[1]
        if actual > longest:
            longest = actual
    return longest

def sortByAssistAsc(data):
    data.sort(key = lambda item: item[1])
    total, longest, actual = 0, 0, 0
    for t in data:
        total += t[0]
        actual = total + t[1]
        if actual > longest:
            longest = actual
    return longest
