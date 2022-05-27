import numpy as np
import pandas as pd

x = np.ones((10,10))    #tworzy tablice 10x10 wypełnioną 1

x[1,2:5]=-1
print(x)

def saveData(data,name):
    """ Zapisauje dane do pliku csv
    data - tablica dwuwymiarowa
    name - string w formacie nazwa.csv """
    df = pd.DataFrame(data=data.astype(float))
    df = df.astype(int)
    df.to_csv(name, sep=' ', header=False, index=False)
