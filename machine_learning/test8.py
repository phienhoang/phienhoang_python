#file main.py
import numpy as np
#import thư viện scipy.optimize để train thuật toán
import scipy.optimize as opt
import matplotlib.pyplot as plt
from functions import *

data = np.loadtxt('data2.txt',delimiter=',')
#Lấy các cột đầu của data và thêm cột 1 vào để làm X
X = np.c_[np.ones(data.shape[0]), data[:,:-1]]
#lấy cột cuối làm y
y = data[:,-1]
#Vòng lặp từ mũ 2 đến mũ 8
for i in range(2,9):
	#thêm một cột feature vào bên phải X với giá trị bằng x1 mũ i
	X = np.c_[X, X[:,1]**i]
#Lấy kích thước y làm m
m = y.size
#Lấy số cột của X làm n
n = X.shape[1]
#tính min và max của x1
min_x = np.min(X[:,1])
max_x = np.max(X[:,1])
#tạo ma trận xp có giá trị từ min_x – 30 đến max_x + 30, step là 0.5 (mỗi giá trị lệch nhau 0.5)
xp = np.arange(min_x - 30, max_x + 30, 0.5)
#thêm x0 bằng 1 cho xp
xp = np.c_[np.ones(xp.size), xp]
#thực hiện thêm polynomial feature như đã làm với X
for i in range(2,9):
	xp = np.c_[xp, xp[:,1]**i]
#Normalize X
[X, mu, sig] = Normalize(X)
#thực hiện normalize xp bằng mu và sigma tính từ X
xp -= mu
xp /= sig
xp[:,0] = 1

#khởi tạo theta ban đầu bằng 0
itheta = np.zeros(n)
#biến l chính là lambda, bạn có thể thay đổi
# biến này để thấy sự khác biệt khi không dùng regularization (l = 0)
# và có dùng l != 0
l = 0
# hàm J_reg rút gọn, chỉ nhận 1 parameter t
j = lambda t: J_reg(X, y, t, l)
# hàm grad_reg rút gọn, chỉ nhận 1 parameter t
g = lambda t: grad_reg(X, y, t, l)

theta = opt.fmin_cg(j, itheta, g)
#thêm tiêu đề biểu đồ
plt.title(f'Polynomial regression with lambda = {l}')

#plot bộ training set, cần đảo ngược quá trình normalize bằng cách * sigma + mu
plt.plot(X[:,1]*sig[1] +mu[1], y, 'rx')
#plot đường dự đoán
plt.plot(xp[:,1]*sig[1] +mu[1], xp@theta)

#Thêm chú thích
plt.legend(['Training example', 'Prediction line'])
plt.xlabel('Change in water level')
plt.ylabel('Water flowing out of the dam')

plt.show()