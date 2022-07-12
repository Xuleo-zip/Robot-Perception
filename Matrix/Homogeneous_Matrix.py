import numpy as np
def Homogeneous_Matrix(angle, origin, translation):
    angle = angle * np.pi / 180
    HMatrix = np.array([[np.cos(angle), -np.sin(angle), translation[0]],
                        [np.sin(angle), np.cos(angle), translation[1]],
                        [0, 0, 1]])
    origin = origin + [1]
    origin = origin.reshape(3, -1)
    return np.dot(HMatrix, origin)

