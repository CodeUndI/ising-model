import numpy as np
import pandas as pd
import singleFlipDynamic as sf
import matplotlib.pyplot as plt
from timeit import default_timer as timer

start = timer() # mierzenie czasu wykonwyania


sf.SaveTrajectory(10, 100, 1.7, 10000, orderly=False)
sf.SaveTrajectory(10, 50, 1.7, 5000, orderly=False)



#sf.SaveMagAndPod([1,3.5],10,50000)
#sf.SaveMagAndPod([1,3.5],50,50000)
#sf.SaveMagAndPod([1,3.5],100,50000)

end = timer()
print(end - start)

