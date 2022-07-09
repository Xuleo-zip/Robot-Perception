# Here is an example of Rotation Matrix
import numpy as np
def Rotation_Matrix(angle, x, y):
    angle = angle * np.pi / 180 # Here we need to convert to radius
    Rotate = np.array([[np.cos(angle), -np.sin(angle)],
                       [np.sin(angle), np.cos(angle)]])
    Rotate = Rotate.reshape(2, -1)
    Coordinate = np.array([x, y])
    Coordinate = Coordinate.reshape(2, -1)
    return np.dot(Rotate, Coordinate)
ang = int(input("Angles you would like to rotate: "))
x_c = int(input("Your x coordinate is: "))
y_c = int(input("Your y coordinate is: "))
Converted = np.array(Rotation_Matrix(ang, x_c, y_c), dtype=int)
print(Converted)

