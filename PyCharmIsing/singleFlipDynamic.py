import random
import numpy as np
import pandas as pd
import math

def MCSIsing(L, T, steps, orderly = True):
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
    for j in range(4):
        for i in range(int(steps/4)):
            m.append(MCSFlip(data,L,T))
        data_list.append(data)

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