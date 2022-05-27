import numpy as np
import pandas as pd
import singleFlipDynamic as sf

x = np.ones((50,50))    #tworzy tablice 10x10 wypełnioną 1

print(x)

def saveData(data,name):
    """ Zapisauje dane do pliku csv
    data - tablica dwuwymiarowa
    name - string w formacie nazwa.csv """
    df = pd.DataFrame(data=data.astype(float))
    df = df.astype(int)
    df.to_csv(name, sep=' ', header=False, index=False)

for i in range(10000):
    sf.MCSFlip(x,len(x),2.26)
print(x)