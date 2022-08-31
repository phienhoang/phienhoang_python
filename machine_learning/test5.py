
from functions import *
[X,y] = Loadtxt('data1.txt')
Theta = NormEqn(X,y)
inp = np.array([1,1650,3])
predict = predict(inp,Theta)
print('%.2f'%(predict))