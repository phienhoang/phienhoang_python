import numpy as np
from functions import *
import matplotlib.pyplot as plt

raw = np.loadtxt('data.txt', delimiter=',')

y = raw[:,2]

X = np.zeros((np.size(y),np.size(raw,1)))

X[:,0] = 1

X[:,1:] = raw[:,0:2]
theta = np.array([123.32,234.34,45.12])
print(computeCost_Vec(X,y,theta))
