from math import log10
import matplotlib.pyplot as plt
from random import randint
from time import time
import scaloneta
from extras import *

NUMTESTS = 10
MIN = 1000
MAX = 100000
AX = [MAX*i for i in range(1, NUMTESTS+1)]

def nLogn(x):
    return x*log10(x)

def getGraph():
    tests = []
    for i in range(1, NUMTESTS+1):
        aux = []
        for _ in range(MAX*i):
            aux.append((randint(MIN, MAX), randint(MIN, MAX)))
        tests.append(aux)

    times = []
    for i in range(len(tests)):
        start = time()
        scaloneta.main(tests[i])
        end = time()
        dt = end - start
        times.append(dt*100)
    nlogn = [nLogn(x/10000) for x in AX]
    fig, ax = plt.subplots()
    ax.plot(AX, times, label= 'Greedy Algorithm')
    ax.plot(AX, nlogn, label= 'O(nLogn)')
    ax.set(xlabel='quantity of videos [n]', ylabel='time [ms]', title='Complexity of the algorithm')
    ax.grid()
    
    fig.savefig('graphic.png')
    plt.legend()
    ax.ticklabel_format(style='plain') #prevent scientific notation
    plt.show()


def getComparison():
    test = []
    times = []
    for _ in range(NUMTESTS):
        test.append((randint(10, 100), randint(10, 100)))

    copy1 = test[:]
    copy2 = test[:]
    copy3 = test[:]
    copy4 = test[:]
    copy5 = test[:]

    times.append(scaloneta.main(copy1))
    times.append(asItComes(copy2))
    times.append(sortByScaloniAsc(copy3))
    times.append(sortByScaloniDesc(copy4))
    times.append(sortByAssistAsc(copy5))

    names = ["Our solution", "As it comes", "Sorted by Scaloni ASC", "Sorted by Scaloni DESC", "Sorted by assistants ASC"]

    fig, ax = plt.subplots()
    ax.barh(names, times)
    ax.set(xlabel='Total time', ylabel='Algoritms', title='Complexity of differents algorithms')
    
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

    fig.savefig('comparison.png')
    plt.show()

def main():
    getGraph()
    getComparison()

if __name__ == "__main__":
    main()


