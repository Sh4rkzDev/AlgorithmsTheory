import sys

def ReadInputs(path = None):
    """
    It process the file passed as parameter in the Command Line, and return a list of tuples representing the requests of each media
    """
    args = sys.argv
    if len(args) != 2 and path is None:
        raise RuntimeError("You should provide a data set")
    requests = []
    if path is None: path = args[1]
    with open(path) as f:
        for line in f:
            requests.append(tuple(line.rstrip("\n").split(",")))
    return requests
