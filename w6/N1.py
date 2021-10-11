class ComplexCalculate:
    def __init__(self,x,y):
        self.real = x
        self.imag = y
    def __str__(self):
        return  f'({self.real},{self.imag}j)'
    def __add__(self, other):
        return ComplexCalculate(self.real + other.real,self.imag - other.imag)
    def __sub__(self, other):
        return ComplexCalculate(self.real - other.real,self.imag - other.imag)
    def __mul__(self, other):
        return ComplexCalculate(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
    def __truediv__(self, other):
        return ComplexCalculate((self.real*other.real+self.imag*other.imag)/(other.real**2+other.imag**2),
                               (-self.real * other.imag + self.imag * other.real)/(other.real**2+other.imag**2))
    def __neg__(self):
        return ComplexCalculate(-self.real,-self.imag)
    def __abs__(self):
        return ((self.real**2+self.imag**2)**0.5)

if __name__ == '__main__':
    x = ComplexCalculate(3,-5)
    y = ComplexCalculate(-1,2)
    print(x,y)
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print('-x =',-x)
    print('abs(x) =',abs(x))