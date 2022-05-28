import random
import numpy as np
import pandas as pd
import math

def SaveMagAndPod(range_T, L, steps, orderly = True):
    """Zwraca przedział czasowy, wartości magnetyzacji, wartości podatności"""
    T = np.linspace(range_T[0], range_T[1], 20)
    mag = []
    pod = []
    for i in T:
        m, p = MCSIsingForMagAndPod(L, i, steps, orderly)
        mag.append(m)
        pod.append(p)
    saveList(T, "partTimeL"+str(L)+".txt")
    saveList(mag, "magnetizationL"+str(L)+".txt")
    saveList(pod, "pliancyL"+str(L)+".txt")
    return T, mag, pod


def MCSIsingForMagAndPod(L, T, steps, orderly = True):
    """Zwraca wartość magnetyzacji i podatności magnetycznej w jednej symulacji"""
    data = np.ones((L, L))
    if orderly != True:         # ustawia losowe wartości spinów
       for i in range(L):
           for j in range(L):
               u = random.random()
               if u >= 0.5:
                   data[i,j] = -1
    m = [sum(sum(data))/L**2]
    for i in range(int(steps)):
        m.append(MCSFlip(data,L,T))
    mag = sum(np.abs(m))/(steps+1)
    pod = L**2*(sum([i**2 for i in m])-mag**2)/T
    return mag, pod

def SaveSpinsAndTrajectory(L, T, steps, orderly = True):
    m, t, data_list = MCSIsing(L, T, steps, orderly)
    saveList(m, 'mListL'+str(L)+'.txt')

def MCSIsing(L, T, steps, orderly = True):
    """Dla zadanej wielkości tworzy siatkę spinów,
    zwraca listę średnich wartości spinów po każdym kroku MC
    """
    data = np.ones((L, L))
    data_list = [data]
    if orderly != True:         # ustawia losowe wartości spinów
       for i in range(L):
           for j in range(L):
               u = random.random()
               if u >= 0.5:
                   data[i,j] = -1
    m = [sum(sum(data))/L**2]
    t = list(range(0,steps+1))
    saveData(data, 'spinsL' + str(L) +'T'+str(T)+ 'stateNumber0.csv')
    for j in range(4):
        for i in range(int(steps/4)):
            m.append(MCSFlip(data,L,T))
        data_list.append(data)
        saveData(data_list[j+1], 'spinsL'+str(L)+'stateNumber'+str(j+1)+'.csv')
    return m, t, data_list


def MCSFlip(data,L,T):
    """Sekewencja zmiany spinów dla 1 kroku Monte Carlo"""
    for i in range(L**2):
        singleFlip(data, L, T)
    return sum(sum(data))/L**2

def singleFlip(data, L, T):
    """Sekwencyjna zmiana pojedynczego spinu
    data - siatka spinów
    L - długość siatki !musi być poprawna!"""
    i, j = math.floor(random.random()*L), math.floor(random.random()*L)
    E = 0
    if i == L-1 or j ==L-1:

        if i == L-1 and j != L-1:
            E = 2*data[i, j]*(data[i-1, j] + data[0, j] + data[i, j-1] + data[i, j+1])

        elif i != L-1 and j == L-1:
            E = 2 * data[i, j] * (data[i - 1, j] + data[i + 1, j] + data[i, j - 1] + data[i, 0])

        else:
            E = 2 * data[i, j] * (data[i - 1, j] + data[0, j] + data[i, j - 1] + data[i, 0])

    else: E = 2*data[i, j]*(data[i-1, j] + data[i+1, j] + data[i, j-1] + data[i, j+1])

    if E <= 0:
        data[i, j] = -data[i, j]
    else:
        x = random.random()
        if x < math.exp(-E/T):
            data[i, j] = -data[i, j]

def saveList(list,name):
    """Zapisuje listę do pliku txt"""
    textfile = open(name,"w")
    for i in list:
        textfile.write(str(i) + "\n")
    textfile.close()

def saveData(data,name):
    """ Zapisauje dane do pliku csv
    data - tablica dwuwymiarowa
    name - string w formacie nazwa.csv """
    df = pd.DataFrame(data=data.astype(float))
    df = df.astype(int)
    df.to_csv(name, sep=' ', header=False, index=False)