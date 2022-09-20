import math
import numpy as np
import os

#欧拉角到旋转矩阵
def Euler2RotationMatrix(angle):
    r, y, p = angle[0], angle[1], angle[2]

    R_x = [[1.0, 0.0, 0.0],
           [0.0, np.cos(r), -np.sin(r)],
           [0.0, np.sin(r), np.cos(r)]]

    R_y = [[np.cos(y), 0.0, np.sin(y)],
           [0.0, 1.0, 0.0],
           [0-np.sin(y), 0.0, np.cos(y)]]

    R_z = [[np.cos(p), -np.sin(p), 0.0],
           [np.sin(p), np.cos(p), 0.0],
           [0.0, 0.0, 1.0]]

    rotation_matrix = np.dot(R_z, np.dot(R_y, R_x))
    return rotation_matrix

#旋转矩阵到欧拉角
def RotationMatrix2Euler(rotation_matrix):
    R_11 = rotation_matrix[0][0]
    R_21 = rotation_matrix[1][0]
    R_31 = rotation_matrix[2][0]
    R_32 = rotation_matrix[2][1]
    R_33 = rotation_matrix[2][2]

    r = np.arctan(R_32 / R_33)
    y = np.arctan(R_21 / R_11)
    p = -np.arcsin(R_31)
    return [r, y, p]

#四元数转旋转矩阵
def Quaternion2RotationMatrix(quaternion):
    s, v1, v2, v3 = quaternion[0], quaternion[1], quaternion[2], quaternion[3]
    R = [[1-2*(v2**2+v3**2), 2*v1*v2-2*s*v3, 2*v1*v3+2*s*v2],
         [2*v1*v2+2*s*v3, 1-2*(v1**2+v3**2), 2*v2*v3-2*s*v1],
         [2*v1*v3-2*s*v2, 2*v2*v3+2*s*v1, 1-2*(v1**2+v2**2)]]
    return R

#旋转矩阵转四元数
def RotationMatrix2Quaternion(rotation_matrix):
    s = np.sqrt(1+rotation_matrix[0][0]+rotation_matrix[1][1]+rotation_matrix[2][2])
    v1 = (rotation_matrix[2][1] - rotation_matrix[1][2]) / (4 * s)
    v2 = (rotation_matrix[0][2] - rotation_matrix[2][0]) / (4 * s)
    v3 = (rotation_matrix[1][0] - rotation_matrix[0][1]) / (4 * s)
    return [s, v1, v2, v3]

#旋转向量到旋转矩阵
def AxisAngle2RotationMatrix(n, theta):
    identity = np.eye(3, dtype=np.float64)
    n = n.reshape(1,3)
    n_sym = np.array([[0.0, -n[0][2], n[0][1]],
                    [n[0][2], 0.0, -n[0][0]],
                    [-n[0][1], n[0][0], 0.0]])

    rotation_matrix = np.cos(theta) * identity
    rotation_matrix += (1-np.cos(theta)) * np.dot(n.T, n)
    rotation_matrix += np.sin(theta) * n_sym
    return rotation_matrix

#旋转矩阵到旋转向量
def RotationMatrix2AxisAngle(rotation_matrix):
    theta = np.arccos((rotation_matrix[0][0] + rotation_matrix[1][1] + rotation_matrix[2][2] - 1) / 2)
    vec = []
    eig_value, eig_vec = np.linalg.eig(rotation_matrix)

    for i in range(len(eig_value)):
        if eig_value[i].real == 1.0 and eig_value[i].imag == 0.0:
            vec = eig_vec[:, i]
    vec = vec / np.sqrt(sum(np.array(vec) ** 2))

    return [vec.real, theta]

#四元数到旋转向量
def Quaternion2AxisAngle(quaternion):
    theta = 2*np.arccos(quaternion[0])
    axis = quaternion[1:] / np.sin(theta /2)
    return [theta, axis]

#旋转向量到四元数
def AxisAngle2Quaternion(axis, angle):
    angle /= 2
    return [np.cos(angle), axis[0]*np.sin(angle), axis[1]*np.sin(angle), axis[2]*np.sin(angle)]

#=========读文件模块===========
#定义文件所在的工作目录
path='G:\\ubuntu\\2022.8.27pnp外参计算\华为图像\\insideHUAWEI1\\partphotos\地面影像trace'
#利用os.listdir()函数读取文件名
file_name_list=os.listdir(path)
#转为字符串
file_name=str(file_name_list)
# replace替换"["、"]"、" "、"'"
file_name = file_name.replace("[", "").replace("]", "").replace("'", "").replace(",", "\n").replace(" ", "")
# 创建并打开文件list.txt
f = open("文件list.txt", "w")
# 将文件下名称写入到"文件list.txt"
f.write(file_name)
f.close()


for line in open('文件list.txt'):
    line=line.replace("\n","")
    for i in open(path+"\\"+line):
        item=i.split("  ")
        file_name_out="out_"+line
        center=item[:3]
        quaternion=item[3:7]
        B=[float(quaternion[0]),float(quaternion[1]),float(quaternion[2]),float(quaternion[3])]#
        #中心坐标
        C=[float(center[0]),float(center[1]),float(center[2])]
        # 旋转矩阵计算
        R = np.linalg.inv(Quaternion2RotationMatrix(B))
        t=-np.dot(R,C)
        print(t)
        T=np.column_stack((R,t))
        print(T)
        with open(file_name_out,"w") as file:
            out=str(T).replace("[", "").replace("]","")
            file .write(out)
            file.close()


A=np.matrix([[],[],[]])
filenamein='24143trace'
print(A)



