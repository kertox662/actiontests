import math
import sys

def calcSphereVolume(radius):
    return math.pi * 4/3 * radius**3

def calcCubeVolume(side):
    return side**3

if len(sys.argv) < 2:
    print("Not enough args")
    exit(1)

for i in sys.argv[1:]:
    print("Sphere Volume with", i,"=",calcSphereVolume(int(i)))
    print("Cube Volume with", i,"=",calcCubeVolume(int(i)))