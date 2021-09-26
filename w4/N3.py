def swap(fun):
    def wrapper(*args,**kwargs):
        args = reversed(args)
        fun(*args,**kwargs)
    return wrapper
@swap
def div(x,y,show=False):
    res = x/y
    if show:
        print(res)
    return res
div(2,4,show=True)