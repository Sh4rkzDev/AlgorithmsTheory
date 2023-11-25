import matplotlib.pyplot as plt
from time import time
import bt
import greedy
import lp
import lpa
import input

AX = [5, 7, 10, 15, 20, 50, 75, 100, 200]

def getGraph():
    tests = ["5.txt", "7.txt", "10_varios.txt", "15.txt", "20.txt", "50.txt", "75.txt", "100.txt", "200.txt"]
    timesBT = []
    timesGreedy = []
    timesLP = []
    timesLPA = []

    for path in tests:
        dataset = input.ReadInputs("tests/" + path)

        startGreedy = time()
        greedy.hittingSetGreedy(dataset)
        endGreedy = time()
        timesGreedy.append(endGreedy - startGreedy)

        startBT = time()
        bt.solucionOptima(dataset)
        endBT = time()
        timesBT.append(endBT - startBT)

        startLP = time()
        lp.solution_lp(dataset)
        endLP = time()
        timesLP.append(endLP - startLP)

        startLPA = time()
        lpa.solution_lp_approx(dataset)
        endLPA = time()
        timesLPA.append(endLPA - startLPA)

    fig, ax = plt.subplots()
    ax.plot(AX, timesBT, label= 'Backtracking Algorithm')
    ax.plot(AX, timesLP, label= 'Linear Programming Algorithm')
    ax.plot(AX, timesLPA, label= 'Linear Programming (Approximated) Algorithm')
    ax.plot(AX, timesGreedy, label= 'Greedy Algorithm')
    ax.set(xlabel='quantity of requests [n]', ylabel='time [s]', title='Complexity of algorithms')
    ax.grid()
    
    plt.legend()
    ax.ticklabel_format(style='plain') #prevent scientific notation
    fig.savefig('graphic.png')
    plt.show()

if __name__ == "__main__":
    getGraph()
