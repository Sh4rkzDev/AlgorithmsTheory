import input
import greedy
import bt
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


if __name__ == "__main__":
    compareAlgorithms()
