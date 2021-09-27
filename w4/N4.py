import time
from functools import wraps
def createfile(file):
    def timer(func):
        @wraps(func)
        def wrap_timer(*args):
            start_time = time.perf_counter()
            rejultat = func(*args)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            if rejultat == None:
                rejultat = '-'
            with open(file,'w') as f:
                f.write('Start time: {}\n'.format(start_time))
                f.write('Arg: {}\n'.format(args))
                f.write('Rejultat: {}\n'.format(rejultat))
                f.write('End time: {}\n'.format(end_time))
                f.write('Run time: {}\n'.format(run_time))
                f.write('Name_func: {}\n'.format(func.__name__))
            return rejultat
        return wrap_timer
    return timer

@createfile('/home-local/student/Desktop/new.txt')
def div(x,y):
    res = x+y
    print(res)
    return res
div(2,5)
print(div.__name__)
