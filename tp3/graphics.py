import matplotlib.pyplot as plt
from random import randint
from time import time
import workout

NUMTESTS = 10
MINTESTS = 2000
MAXTESTS = MINTESTS * NUMTESTS
MIN = 1
MAX = 100
AX = [i for i in range(MINTESTS, MAXTESTS+1, MINTESTS)]

def cuad(n):
    return 0.0000002 * n**2

def getGraph():
    tests = []
    for i in range(1, NUMTESTS+1):
        earnings, energies = [], []
        quant = MINTESTS * i
        energy = 100
        onePerc = quant // 100
        for j in range(quant):
            earnings.append((randint(MIN, MAX)))
            energies.append(energy)
            if j // onePerc == 0: energy -= 1
        aux = (earnings, energies)
        tests.append(aux)

    times = []
    numberTest = 1
    for earn, energy in tests:
        start = time()
        workout.getWorkOut(earn, energy)
        end = time()
        dt = end - start
        print("Finished test ", numberTest)
        numberTest += 1
        times.append(dt)

    complexity = [cuad(n) for n in AX]

    fig, ax = plt.subplots()
    ax.plot(AX, times, label= 'Dynamic Programming')
    ax.plot(AX, complexity, label= 'O(n x n)')
    ax.set(xlabel='quantity of workouts [n]', ylabel='time [s]', title='Complexity of the algorithm')
    ax.grid()
    
    plt.legend()
    ax.ticklabel_format(style='plain') #prevent scientific notation
    fig.savefig('graphic.png')
    plt.show()

def main():
    getGraph()

if __name__ == "__main__":
    main()

