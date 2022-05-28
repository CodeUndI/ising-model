l = [1.23, 5.234, 6.234, -0.678]

textfile = open("cos.txt", "w")
for i in l:
    textfile.write(str(i) + "\n")
textfile.close()