path = "files/pts2.pts"

ptsFile = open(path, 'r')
lines = ptsFile.readlines()


def getCoordinates(line):
    linearr = str(line).split(' ')
    arr = {"x": linearr[0], "y": linearr[1], "z": linearr[2]}
    return arr


lineNumber = 0
coordinates = []
# Strips the newline character
for line in lines:
    if lineNumber > 100:
        break

    if lineNumber == 0:
        print("Toplam nokta sayısı : {:,}".format(int(line.strip())))
    else:
        coordinates.append(getCoordinates(line))

    lineNumber += 1


import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
