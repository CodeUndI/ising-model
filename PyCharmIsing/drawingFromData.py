import numpy as np
import pandas as pd
import singleFlipDynamic as sf
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt

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

saveSpinsFromData('spinsL10stateNumber4')
