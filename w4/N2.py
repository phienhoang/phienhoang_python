def decorator(fun):
    def swap(lis):
        count = fun(lis)
        if count == 0:
            print('Нет')
        elif count > 10:
            print('Очень много')
        else:
            print(count)
    return swap
@decorator
def even(list):
    s = 0
    for i in list:
        if i%2 == 0:
            s += 1
    return s
even([1,3,5,9])
even([5,9,20,57,68,70,91,100])
even([2,4,6,20,22,40,48,50,90,100,120])