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
    fig, ax = plt.subplots()
    ax.plot(AX, times, label= 'Dynamic Programming')
    ax.set(xlabel='quantity of workouts [n]', ylabel='time [s]', title='Complexity of the algorithm')
    ax.grid()
    
    plt.legend()
    ax.ticklabel_format(style='plain') #prevent scientific notation
    fig.savefig('graphic.png')
    plt.show()

'''
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
'''
def main():
    getGraph()
    #getComparison()

if __name__ == "__main__":
    main()


