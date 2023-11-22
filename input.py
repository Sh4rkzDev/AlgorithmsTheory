import sys

def ReadInputs():
    """
    It processes the file passed as parameter in the Command Line, and returns a list of lists of the subset of players that
    each sports journalist wants to see playing
    """
    args = sys.argv
    if len(args) != 2:
        raise RuntimeError("You should provide a data set")
    
    sets = []
    with open(args[1]) as f:
        subset = f.readline().split(',')
        sets.append(subset)

    return sets
