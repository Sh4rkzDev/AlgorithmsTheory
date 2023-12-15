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

def getTime(name, names, sol, func, dataset):
    names.append(name)
    sol.append(len(func(dataset)))

def getComparison():
    dataset = input.ReadInputs("tests/200.txt")
    names, sol = [], []

    getTime("Greedy", names, sol, greedy.hittingSetGreedy, dataset)

    getTime("Backtracking", names, sol, bt.solucionOptima, dataset)

    getTime("Linear Programming", names, sol, lp.solution_lp, dataset)

    getTime("Linear Programming (Approx)", names, sol, lpa.solution_lp_approx, dataset)

    fig, ax = plt.subplots()
    ax.barh(names, sol)
    ax.set(xlabel='Size of the solutions', ylabel='Algorithms', title='Optimality of differents algorithms')

    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)

    # Add x, y gridlines
    ax.grid(visible = True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.2)

    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')
    plt.show()

if __name__ == "__main__":
    getGraph()
    getComparison()
