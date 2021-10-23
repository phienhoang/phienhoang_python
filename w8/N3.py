def analis_zip(*iterable):
    sentinal = object
    iterators = [iter(it) for it in iterable]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for  it in (iterators):
            value = next(it,sentinal)
            if value is sentinal:
                return
            values.append(value)
        yield list(values)
for i in analis_zip(["Alex", "Bob", "Alice", "John", "Ann"],[ 25,17, 34, 24, 42],["M", "M", "F", "M", "F"]):
    print(i)


def analis_map(function,iterable):
    for el in iterable:
        yield function(el)


def analis_enumerate(iterable,start=0):
    for i in iterable:
        yield start,i
        start += 1
