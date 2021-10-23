def Fibonacci(a):
    yield 0
    yield 1
    _current1 = 0
    _current2 = 1
    b = 2
    while b < a :
        yield(_current1+_current2)
        _current1,_current2 = _current2, _current1+_current2
        b += 1
for i in Fibonacci(5):
    print(i, end = " ")
print()