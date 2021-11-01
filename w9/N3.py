import numpy as np
class PrintAverage(Exception):
    pass

class PrintDispersion(Exception):
    pass

class PrintAmountOfElements(Exception):
    pass

def A_coroutine():
    print("Starting coroutine")
    s = []
    try:
        while True:
            try:
                x = yield
                s.append(x)
                average = np.mean(s)
                dispersion = np.var(s)
                n = len(s)

            except PrintAverage:
                yield average
            except PrintDispersion:
                yield dispersion
            except PrintAmountOfElements:
                yield n
    finally:
        print("Stop coroutine")

coroutine = A_coroutine()
next(coroutine)
for i in range(12):
    coroutine.send(i)
    if i%2 == 0:
        print("Average:", coroutine.throw(PrintAverage))
        next(coroutine)
    if i%3 == 0:
        print("Dispersion:", coroutine.throw(PrintDispersion))
        next(coroutine)
    if i%4 == 0:
        print('Amount Of Elements:', coroutine.throw(PrintAmountOfElements))
        next(coroutine)

print()
print(coroutine.throw(PrintAverage))
next(coroutine)

print(coroutine.throw(PrintDispersion))
next(coroutine)

print(coroutine.throw(PrintAmountOfElements))
next(coroutine)

coroutine.close()
