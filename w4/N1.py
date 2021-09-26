import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('n',help='the fibonacci number', type= int)
args = parser.parse_args()
n = args.n
def f(i):
    if i in (0,1):
        return 1
    return f(i-1) + f(i-2)
print(f(n))