import numpy as np

def predict(X,Theta):
    return X@Theta
def computeCost_Vec(X,y,Theta):
    error = predict(X,Theta) - y
    m = np.size(y)
    J = (1/(2*m))*np.transpose(error)@error
    return J

def GradientDescent(X,y,alpha=0.02,iter=5000): #giá trị mặc định của alpha là 0.02, iter(số vòng lặp tối đa) là 5000
    theta = np.zeros(np.size(X,1))

    #array lưu lại các giá trị J trong quá trình lặp
    # kích thước là iter*2, cột đầu chỉ là các số từ 1 đến iter đểtiện cho việc plot. kích thước được  vào qua một tupple
    J_hist = np.zeros((iter,2))
    m = np.size(y)
    X_T = np.transpose(X)
    pre_cost = computeCost_Vec(X,y,theta)
    for i in range(0,iter):
        printProgressBar(i,iter)
        error = predict(X,theta) -y
        theta = theta - (alpha/m)*(X_T@error)
        cost = computeCost_Vec(X,y,theta)
        if np.round(cost,15) == np.round(pre_cost,15):
            print('Reach optima at I = %d; J = %.6f'%(i,cost))
            J_hist[i:,0] = range(i,iter)
            J_hist[i:,1] = cost
            break
        pre_cost = cost
        J_hist[i,0] = i
        J_hist[i,1] = cost
    yield theta
    yield J_hist


def printProgressBar (iteration, total, suffix = ''):
    percent = ("{0:." + str(1) + "f}").format(100 * ((iteration+1) / float(total)))
    filledLength = int(50 * iteration // total)
    bar = '=' * filledLength + '-' * (50- filledLength)
    print('\rTraining: |%s| %s%%' % (bar, percent), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def Normalize(X):
    n = np.copy(X)
    n[0,0] = 100
    s = np.std(n,0,dtype=np.float64)
    mu = np.mean(n,0)
    n = (n-mu)/s
    n[:,0] = 1
    yield n
    yield mu
    yield s

def Loadtxt(path):
    try:
        raw = np.loadtxt(path, delimiter=',')
        X = np.zeros((np.size(raw,0),np.size(raw,1)))
        X[:,0] = 1
        X[:,1:] = raw[:,:-1]
        y = raw[:,-1]
        yield X
        yield y
    except:
        return 0

def NormEqn(X,y):
    return np.linalg.pinv(X.T@X)@(X.T@y)

#Hàm cost regularized nhận các parameter X, y, theta
#và parameter regularization lambda mặc định là 0
def J_reg(X, y, theta, l = 0):
    # m là số example, bằng độ dài của y
    m = y.size
    # vì chúng ta chỉ cần regularized các theta từ 1 -> n, ta sẽ tạo
    # một biến tạm là các theta này
    t = theta[1:]
    # error bằng h(x) - y
    err = predict(X, theta) - y
    # hạng tử regularization bằng lambda * tổng bình phương
    # các theta chia 2m
    regular = (l * (t.T @ t)) / (2 * m)
    # J bằng bình phương error / 2m + hạng tử regularization
    J = (err.T @ err) / (2 * m) + regular
    # trả về kết quả
    return J


def grad_reg(X, y, theta, l = 0):
	#m là số training example
	m = y.size
	#n là số feature (số cột của X)
	n = X.shape[1]
	#grad là vector thể hiện “độ dốc” cần trả về
	grad = np.zeros(n)
    # tính error = h(x) – y
    #tính error = h(x) – y
	err = predict(X, theta) - y
	#tính cost gradient cho theta 0, không có regularization term
	grad[0] = (1/m)*(X[:,0].T@err)
	#tính cost gradient cho các theta còn lại với regularization term
	grad[1:] = (1/m)*(X[:,1:].T@err) + (l/m)*theta[1:]
	#trả về ma trận grad là vector các cost gradient cho từng theta
	return grad


def norm_eqn_reg(X,y, l=0):
    #n là số feature
    n = X.shape[1]
    # tạo identity matrix n*n
    L = np.eye(n)
    # gán phần tử 0,0 bằng 0
    L[0, 0] = 0
    # nhân tử đầu tiên
    a = np.linalg.pinv(X.T @ X + l * L)
    # nhân tử thứ 2
    b = X.T @ y

    # tính theta
    theta = a @ b
    return theta

