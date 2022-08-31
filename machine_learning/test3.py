import numpy as np
import matplotlib.pyplot as plt
from functions import *

raw = np.loadtxt('data.txt',delimiter=',')
X = np.copy(raw)
X[:,1] = X[:,0]
X[:,0] = 1
y = raw[:,1]
[Theta,J_hist] = GradientDescent(X,y)
predict = predict(X,Theta) * 10000
plt.figure(1)
plt.plot(X[:,1],y,'rx')
plt.plot(X[:,1],predict/10000,'-b')
plt.figure(2)
plt.plot(J_hist[:,0],J_hist[:,1], '-r')
plt.show()