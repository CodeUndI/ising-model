import numpy as np
import pandas as pd
import singleFlipDynamic as sf
import matplotlib.pyplot as plt
from timeit import default_timer as timer

start = timer() # mierzenie czasu wykonwyania

#sf.SaveSpinsAndTrajectory(5,1,100000)
sf.SaveMagAndPod([1,3.5],10,10000)

end = timer()
print(end - start)

