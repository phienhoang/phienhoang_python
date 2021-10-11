class pract:
    def __init__(self,*args):
        self.__args = args
    def __str__(self):
        return  f'{self.__args}'
    def __add__(self, other):
        return np.add(self.__args, other.__args)
    def __sub__(self, other):
        return np.subtract(self.__args, other.__args)

if __name__ == '__main__':
    N = int(input())
    sumx = 0
    sumy = 0
    sumz = 0

    for i in range(N):
        x,y,z = list(map(float,input().split()))
        sumx += x
        sumy += y
        sumz += z
    a = float(sumx/N)
    b = float(sumy/N)
    c = float(sumz/N)
    print('точка центра {}'.format(pract(a,b,c)))