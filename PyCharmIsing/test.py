import numpy as np

l = [1.23, 5.234, 6.234, -0.678]

textfile = open("cos.txt", "w")
for i in l:
    textfile.write(str(i) + "\n")
textfile.close()

t = [1,2,3,4,5,6,7]

np.sum(t**2)

print(t)