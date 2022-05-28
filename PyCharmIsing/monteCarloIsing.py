import numpy as np
import pandas as pd
import singleFlipDynamic as sf
import matplotlib.pyplot as plt


def saveData(data,name):
    """ Zapisauje dane do pliku csv
    data - tablica dwuwymiarowa
    name - string w formacie nazwa.csv """
    df = pd.DataFrame(data=data.astype(float))
    df = df.astype(int)
    df.to_csv(name, sep=' ', header=False, index=False)

m, t, data  = sf.MCSIsing(10,2.16,10000, orderly=False)

plt.plot(t, m)
plt.show()
print(data)