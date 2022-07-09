# Here is an example of 2D translation matrix
import numpy as np
def Translation_Matrix(tx, ty, x, y):
    T = np.array([[1, 0, tx], [0, 1, ty]])
    T = T[:, 2]
    T = T.reshape(2, -1)
    Coordinate = np.array([x, y])
    Coordinate = Coordinate.reshape(2, -1)
    return print(T + Coordinate)
a = int(input('Your x coordinate is: '))
b = int(input('Your y coordinate is: '))
ta = int(input('Amount of translation in x direction: '))
tb = int(input('Amount of translation in y direction: '))
print(Translation_Matrix(ta, tb, a, b))
