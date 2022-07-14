import numpy as np
def Intrinsic_Matrix(fx, fy, cx, cy):
    InMatrix = np.array([[fx, 0, cx],
                         [0, fy, cy],
                         [0, 0, 1]])
    return InMatrix
x, y, z, w = input("Your configuration and parameters is: ")
print(Intrinsic_Matrix(x, y, z, w))