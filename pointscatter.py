import numpy as np
import matplotlib.pyplot as plt
from scrapy.spidermiddlewares import depth

Intrinsic_Matrix = np.array([[431.4655346201811, 0, 424.0],
                             [0, 431.4655346201811, 240],
                             [0, 0, 1]])

Rotation_Matrix = np.array([[0, -1, 0],
                            [0, 0, -1],
                            [1, 0, 0]])
examples_image_path = "/Users/leoxu/Desktop/Python/Mirror Python/220623/RGB/45.256859768.png"
points = np.fromfile("/Users/leoxu/Desktop/Python/Mirror Python/220623/lidar/45.256859768", dtype=np.float32)
points = points.reshape(-1, 4)[:, :3]
x, y, z = points[:, 0], points[:, 1], points[:, 2]
translation = np.array([[0.084],
                        [0.025],
                        [-0.05]])
final_x = np.array([])
final_y = np.array([])
final_z = np.array([])
u = np.array([])
v = np.array([])
depth = np.array([])
for i in range(len(x)):
    Each_point = np.array([x[i], y[i], z[i]]).reshape(3, -1)
    x[i], y[i], z[i] = np.dot(Rotation_Matrix, [x[i], y[i], z[i]])
    x_1, y_1, z_1 = np.dot(Rotation_Matrix, translation)
    point_x = [[x[i] - x_1] for k in x]
    point_y = [[y[i] - y_1] for k in y]
    point_z = [[z[i] - z_1] for k in z]

    Huge_matrix = np.array([point_x, point_y, point_z]).reshape(3, -1)
    print(Huge_matrix)
    for j in range(len(point_x)):
        u[j], v[j], depth[j] = np.dot(Intrinsic_Matrix, Huge_matrix[:, j])
        print(u)

