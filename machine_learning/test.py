import numpy as np
np.array(object, dtype=None, ndmin=0) # mảng, kiểu dữ liệu phần tử ma trận, số chiều tối thiểu khi return object.
_A = [[1,2,3],[4,5,6]]
_B = [[2,4,5],[7,8,21],[1,1,1]]
A = np.array(_A)
B = np.array(_B)
C = np.eye(3)
D = np.linalg.pinv(B)
E = np.transpose(A)
print(E)
print(B@D)
print(np.size(A,0))
print(np.size(A,1))
print(np.shape(A))