import numpy as np
import pandas as pd
import singleFlipDynamic as sf
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import os

def savePlotForMag(path):
    data = saveMagPlots(path)
    plt.plot(data[1], data[0],'-ro', label = 'L10', markersize=4)
    plt.plot(data[3], data[2], '-bo',label = 'L50', markersize=4)
    plt.plot(data[5], data[4], '-go', label = 'L100', markersize=4)
    plt.title('Zależność podatnośći od temperatury')
    plt.xlabel("T")
    plt.ylabel("\u03A7")
    plt.grid()
    plt.legend()
    plt.savefig("podatność.pdf", format='pdf', bbox_inches='tight')
    print(os.getcwd())

def saveMagPlots(path):
    os.chdir(path)
    data = []
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{path}\{file}"
            data.append(getFromTxt(file_path))
    return data

def saveSpinsFromData(file):
    "nazwa pliku bez końcówki .csv"
    plt.imshow(getFromFile(file+'.csv'))
    plt.savefig(file+'.pdf')

def getFromTxt(file):
    my_file = open(file,"r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    content_list.pop(-1)
    value_list = [float(i) for i in content_list]
    return value_list

def getFromFile(file):
    return np.loadtxt(open(file,'rb'), delimiter=" ", skiprows=0)

# --------------------------------------------------
#mag_path = "D:\!!! STUDIA\SEMESTR 4\FIZYKA UKŁADÓW ZŁOŻONYCH\SYMULACJA MODELU ISINGA\ising-model\ForMag\pierwszaSymulacja"
#mag_path2 = "D:\!!! STUDIA\SEMESTR 4\FIZYKA UKŁADÓW ZŁOŻONYCH\SYMULACJA MODELU ISINGA\DoMagnetyzacji\symulacja2"
#pod_path = "D:\!!! STUDIA\SEMESTR 4\FIZYKA UKŁADÓW ZŁOŻONYCH\SYMULACJA MODELU ISINGA\DoPodatności\symulacja2"

#savePlotForMag(pod_path)

#data = saveMagPlots("D:\!!! STUDIA\SEMESTR 4\FIZYKA UKŁADÓW ZŁOŻONYCH\SYMULACJA MODELU ISINGA\DoTrajektorii\L50")
#data = saveMagPlots("D:\!!! STUDIA\SEMESTR 4\FIZYKA UKŁADÓW ZŁOŻONYCH\SYMULACJA MODELU ISINGA\DoTrajektorii\L10")
#data = saveMagPlots("D:\!!! STUDIA\SEMESTR 4\FIZYKA UKŁADÓW ZŁOŻONYCH\SYMULACJA MODELU ISINGA\DoTrajektorii\L100")
data = saveMagPlots("D:\!!! STUDIA\SEMESTR 4\FIZYKA UKŁADÓW ZŁOŻONYCH\SYMULACJA MODELU ISINGA\DoTrajektorii\L50nr2")

for i in data:
    plt.plot(i)
plt.grid()
plt.title("T=1.7    L=50")
plt.xlabel("t [MCS]")
plt.ylabel("m")
plt.savefig("trajektorieL50.pdf", format='pdf', bbox_inches='tight')
plt.show()
