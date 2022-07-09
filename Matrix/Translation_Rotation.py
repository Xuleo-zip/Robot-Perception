import numpy as np
import matplotlib.pyplot as plt
def Translation_Rotation(angle, translation, point1, point2):
    angle = angle * np.pi / 180
    HMatrix = [[np.cos(angle), -np.sin(angle), translation[0]],
               [np.sin(angle), np.cos(angle), translation[1]],
               [0, 0, 1]]
    point1 = point1 + [1]
    point1 = np.array(point1)
    point2 = point2 + [1]
    point2 = np.array(point2)
    point3 = np.dot(point1, HMatrix)
    point4 = np.dot(point2, HMatrix)
    return point3, point4
Pre_point1 = input("Your first point is: ")
Pre_point1 = Pre_point1.split(",")
Pre_point1 = [float(j) for j in Pre_point1]
Pre_point2 = input("Your second point is: ")
Pre_point2 = Pre_point2.split(",")
Pre_point2 = [float(k) for k in Pre_point2]
Trans = input("Translate in x and y is: ")
Trans = Trans.split(",")
Trans = [float(i) for i in Trans]
Pre_x = [Pre_point1[0], Pre_point2[0]]
Pre_y = [Pre_point1[1], Pre_point2[1]]
ang = int(input("Angle to rotate: "))
Fpoints = Translation_Rotation(ang, Trans, Pre_point1, Pre_point2)
F_x = [Fpoints[0][0], Fpoints[1][0]]
F_y = [Fpoints[0][1], Fpoints[1][1]]
plt.plot(Pre_x, Pre_y, color='red')
plt.plot(F_x, F_y, color='blue')
plt.show()
