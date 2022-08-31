import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('test1.txt', delimiter=',')
theta = np.loadtxt('theta.txt',delimiter=',')
X = np.zeros((np.size(x,0),np.size(x,1)))
y = np.copy(x[:,-1])
X[:,0] = 1
n = np.size(x,1) - 1
X[:,1:] = x[:,0:n]
print(X)
predict = X@theta
predict = predict*10000
print('%d nguoi: %.2f' %(X[0,1]*10000,predict[0]))
np.savetxt('value.txt', predict, fmt='%.6f')


#plot giá trị thực tế (không lấy cột bias 1 đầu)
# X[:,1:] là x-axis của biểu đồ, không lấy cột đầu;
# y là y-axis, rx là red x, plot dữ liệu bằng dấu x màu đỏ
plt.plot(X[:,1:], y,'rx')
plt.plot(predict/10000,y,'-b') # đường màu xanh
plt.show()
