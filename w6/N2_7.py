class pract:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return  f'({self.x},{self.y},{self.z})'
    def __add__(self, other):
        return pract(self.x + other.x,self.y + other.y,self.z + other.z)
    def __sub__(self, other):
        return pract(self.x - other.x,self.y - other.y,self.z - other.z)
    def __matmul__(self, other):
        return pract(self.y*other.z - other.y*self.z , self.z*other.x - other.z*self.x , self.x*other.y - other.x*self.y) 
    def __abs__(self):
        return ((self.x**2+self.y**2+self.z**2)**0.5)


if __name__ == '__main__':
    N = int(input())
    list_vector = []
    P = 0

    for i in range(N):
        a,b,c = list(map(int,input().split()))
        n = pract(a,b,c)
        list_vector.append(n)
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                v1 = list_vector[i] - list_vector[j]
                v2 = list_vector[k] - list_vector[j]
                if v1@v2 != 0:
                    s = (1/2) * abs(v1@v2)
                    if s > P :
                        P = s
                        T1 = list_vector[i]
                        T2 = list_vector[j]
                        T3 = list_vector[k]
print(P,T1,T2,T3)