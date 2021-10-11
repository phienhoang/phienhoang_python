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
    x = pract(1,2,3)
    y = pract(4,5,6)
    z = x@y
    s = abs(z)
    print('площадь: {}'.format(s))