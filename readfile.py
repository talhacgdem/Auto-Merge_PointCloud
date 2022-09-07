import visualize
import distance

path = "files/pts2.pts"

ptsFile = open(path, 'r')
lines = ptsFile.readlines()


def getCoordinates(line):
    linearr = str(line).split(' ')
    # arr = {"x": linearr[0], "y": linearr[1], "z": linearr[2]}
    arr = [float(linearr[0]), float(linearr[1]), float(linearr[2])]
    return arr


lineNumber = 1
coordinates = []

num_rows = int(lines[0])
lines.pop(0)

for line in lines:
    if lineNumber > 1000000:
        break

    coordinates.append(getCoordinates(line))
    print("On line : {} / {}".format(lineNumber, num_rows))
    lineNumber += 1


distance.findClosest(coordinates)

# print("##################################")
# print("Visualing...")
# print("##################################")
# visualize.toVisual(coordinates)
