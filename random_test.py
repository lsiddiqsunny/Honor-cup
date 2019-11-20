import random

list = []
for i in range(32*32):
    list.append(i)
random.shuffle(list)

f = open("16.txt", "w+")
for i in range(1800, 2099):
    f.write(str(i).zfill(4) + ".png\n")
    random.shuffle(list)
    j = 0
    for k in list:
        if j == 0:
            f.write(str(k))
        else:
            f.write(" " + str(k))
        j = j + 1
    f.write("\n")
f.close()
