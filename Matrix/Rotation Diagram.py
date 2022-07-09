# Here is an example that shows rotation of a line
import matplotlib.pyplot as plt
import numpy as np
def Rotation_Matrix(angle, x, y, z, w):
    angle = angle * np.pi / 180
    RMatrix = [[np.cos(angle), -np.sin(angle)],
               [np.sin(angle), np.cos(angle)]]
    Point1 = [x, y]
    Point2 = [z, w]
    convert1 = np.array(np.dot(RMatrix, Point1))
    convert2 = np.array(np.dot(RMatrix, Point2))
    return convert1, convert2
angle1 = int(input("The angle of rotation: "))
x1 = int(input("First point x coordinate: "))
y1 = int(input("First point y coordinate: "))
z1 = int(input("Second point x coordinate: "))
w1 = int(input("Second point y coordinate:"))
Coords = Rotation_Matrix(angle1, x1, y1, z1, w1)
print(Coords)
all_x1 = [x1, z1]
all_y1 = [y1, w1]
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
plt.plot(all_x1, all_y1, color='blue')
all_x2 = [Coords[0][0], Coords[1][0]]
all_y2 = [Coords[0][1], Coords[1][1]]
plt.plot(all_x2, all_y2, color='red')
plt.show()
