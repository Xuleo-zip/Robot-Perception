import numpy as np
def Inverse_Matrix(angle, orgin, fcoords, point):
    angle = angle * np.pi / 180
    Rotation_Matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    InverseMatrix = np.linalg.inv(Rotation_Matrix)
    translation = [[fcoords[0]-orgin[0]], [fcoords[1]-orgin[1]]]
    column_1, column_2 = InverseMatrix[:, 0], InverseMatrix[:, 1]
    NewHMatrix = np.array([[column_1[0], column_1[1], translation[0]],
                           [column_2[0], column_2[1], translation[1]],
                           [0, 0, 1]], dtype=object)
    point = np.array([point + [1]]).reshape(3, -1)
    return np.dot(NewHMatrix, point)
ang = int(input("Second Frame rotate degree is: "))
ori = input("Your orginal frame origin is: ").split(",")
ori = [float(i) for i in ori]
frcoords = input("Another frame origin in current frame is: ").split(",")
frcoords = [float(k) for k in frcoords]
poi = input("Your point position in other frame is: ").split(",")
poi = [int(j) for j in poi]
point_in_current_frame = Inverse_Matrix(ang, ori, frcoords, poi)
point_in_current_frame = np.delete(point_in_current_frame, 2)
print(point_in_current_frame)
