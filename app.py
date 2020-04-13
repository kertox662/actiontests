import math

def calcSphereVolume(radius):
    return math.pi * 4/3 * radius**3

def calcCubeVolume(side):
    return side**3

print(calcSphereVolume(4))
print(calcCubeVolume(4))