import numpy as np
from scipy.spatial.transform import Rotation
import os.path
import open3d as o3d
file_path = '/~/pose.txt'
pose = np.loadtxt(file_path, dtype=np.float32, skiprows=3, comments='#')
pose.reshape(-1, 8)
time, translation, rotation = pose[:, 0], pose[:, 1:4], pose[:, 4:]
path = '/~/lidar'
file_list = sorted(os.listdir(path))
i = 0
x_final, y_final, z_final = np.array([]), np.array([]), np.array([])
for file in file_list:
    if i == len(file_list): # It shoud not be 48+, otherwise get error
        continue
    lpoints = np.fromfile('/~/lidar/%s' % file, dtype=np.float32)
    lpoints = lpoints.reshape(-1, 4)[:, :3]
    x, y, z = lpoints[:, 0], lpoints[:, 1], lpoints[:, 2]
    r = (Rotation.from_quat(rotation[i, :])).as_matrix()
    t = translation[i, :]
    for j in range(len(x)):
        x[j], y[j], z[j] = np.dot(r, [x[j], y[j], z[j]]) + t
    x_final, y_final, z_final = np.append(x_final, x), np.append(y_final,y), np.append(z_final, z)
    i += 1
Coords = np.append(np.append(x_final, y_final), z_final)
Coords = Coords.reshape(3, -1)
pointcloud = o3d.geometry.PointCloud()
pointcloud.points = o3d.utility.Vector3dVector(Coords.T)
o3d.visualization.draw_geometries([pointcloud])