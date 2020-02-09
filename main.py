import heuristics as h
import cplexSolver as cps
import matplotlib.pyplot as plt
import numpy as np
import glob


def getFile(fileName):
    f = open(fileName, "r")
    data = f.read().split("\n")
    f.close()
    box_size = int(data[1])
    numobj = int(data[0])
    object_list = data[2:numobj + 2]
    for i in range(numobj):
        object_list[i] = int(object_list[i])
    return box_size, object_list, numobj


def testFile(fileName):
    box_size, object_list, numobj = getFile(fileName)
    return [h.first_fit(box_size, object_list), h.next_fit(box_size, object_list), h.best_fit(box_size, object_list),cps.solveWithCplex(box_size,object_list,numobj)]


def plotDataSetResults(directory, capacities, volume):
    X = np.arange(4)
    ax = plt.subplot()
    data = np.zeros([4, 4])
    i = 0
    j = 0
    files = glob.glob(directory + '/*')
    for file in files:
        print(file)
        result = testFile(file)
        data[0][j] += result[0]
        data[1][j] += result[1]
        data[2][j] += result[2]
        data[3][j] += result[3]
        i += 1
        if (i == 20):
            i = 0
            data[0][j] /= 20.0
            data[1][j] /= 20.0
            data[2][j] /= 20.0
            data[3][j] /= 20.0
            j += 1
    data[0] = np.sort(data[0])
    data[1] = np.sort(data[1])
    data[2] = np.sort(data[2])
    data[3] = np.sort(data[3])
    ax.bar(X - 0.40, data[0], color='b', width=0.2, align='center')
    ax.bar(X - 0.20, data[1], color='g', width=0.2, align='center')
    ax.bar(X + 0.00, data[2], color='r', width=0.2, align='center')
    ax.bar(X+ 0.20, data[3], color='y',width=0.2, align='center')
    ax.set_title('Set : ' + directory + ' : volume V = ' + volume)
    ax.set_xlabel('Nombre d\'objets à ranger')
    ax.set_ylabel('Nombre moyen de boites')
    ax.legend(labels=["first fit", "next fit", "best fit","cplex"])
    ax.set_xticks(X)
    ax.set_xticklabels(capacities)
    plt.show()


dirlist = glob.glob('Falken*')
capacitieslist = [['120', '250', '500', '1000'], ['60', '120', '249', '501']]
volume = ['150', '1000']
for d in range(2):
    print(dirlist[d])
    plotDataSetResults(dirlist[d], capacitieslist[d], volume[d])
