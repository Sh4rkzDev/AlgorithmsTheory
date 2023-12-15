import input
import bt
import greedy
import lp
import lpa
from time import time

def getTime(name, func, dataset):
    start = time()
    res = func(dataset)
    end = time()
    print("------------------------------")
    print(name, ":")
    print("")
    print(f'Solution: {len(res)}')
    print(f'Time: {end - start} seconds')
    print("------------------------------")

def compareAlgorithms():
    """
    Compare algorithms by time and their solutions.
    """

    dataset = input.ReadInputs()

    getTime("Greedy", greedy.hittingSetGreedy, dataset)

    getTime("Backtracking", bt.solucionOptima, dataset)

    getTime("Linear Programming", lp.solution_lp, dataset)

    getTime("Linear Programming (Approximated)", lpa.solution_lp_approx, dataset)

if __name__ == "__main__":
    compareAlgorithms()
