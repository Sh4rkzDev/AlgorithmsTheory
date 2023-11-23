import sys

def ReadInputs():
    """
    It process the file passed as parameter in the Command Line, and return a list of the earnings of the workout through the days
    and a list of the energy consumed day by day.
    """
    args = sys.argv
    if len(args) != 2:
        raise RuntimeError("You should provide a data set")
    earnings = []
    energy = []
    with open(args[1]) as f:
        n = int(f.readline())
        for _ in range(n):
            earnings.append(int(f.readline()))
        for _ in range(n):
            energy.append(int(f.readline()))
    return earnings, energy
