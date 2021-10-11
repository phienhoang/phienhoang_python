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
    def skaliap(self,other):
        return self.x * other.x + self.y * other.y + self.z * other.z


if __name__ == '__main__':
    x = pract(1,2,3)
    y = pract(4,5,6)
    z = pract(5,3,7)
    s = x@y
    v = pract.skaliap(z,s)
    if v > 0:
        pass
    else:
        v = -v
    print('Объём: {}'.format(v))