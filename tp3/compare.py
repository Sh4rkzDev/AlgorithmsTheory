import input
import bt
import greedy
import lp
from time import time

def compareAlgorithms():
    """
    Compare algorithms by time and their solutions.
    """

    dataset = input.ReadInputs()

    startGreedy = time()
    resGreedy = greedy.hittingSetGreedy(dataset)
    endGreedy = time()

    print("------------------------------")
    print("Greedy:")
    print("")
    print(f'Solution: {len(resGreedy)}')
    print(f'Time: {endGreedy - startGreedy} seconds')
    print("------------------------------")

    startBT = time()
    resBT = bt.solucionOptima(dataset)
    endBT = time()

    print("------------------------------")
    print("Backtracking:")
    print("")
    print(f'Solution: {len(resBT)}')
    print(f'Time: {endBT - startBT} seconds')
    print("------------------------------")

    startLP = time()
    resLP = lp.solution_lp(dataset)
    endLP = time()

    print("------------------------------")
    print("Linear Programming:")
    print("")
    print(f'Solution: {len(resLP)}')
    print(f'Time: {endLP - startLP} seconds')
    print("------------------------------")

if __name__ == "__main__":
    compareAlgorithms()
