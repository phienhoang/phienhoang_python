class pract:
    def __init__(self,*args):
        self.__args = args
    def __str__(self):
        return  f'{self.__args}'
    def __add__(self, other):
        return np.add(self.__args, other.__args)
    def __sub__(self, other):
        return np.subtract(self.__args, other.__args)
    def distance(self):
        s = 0
        for i in self.__args:
            s += i**2
        distance = s**0.5
        return distance


if __name__ == '__main__':
    N = int(input())
    list_ = []
    dis = {}

    for i in range(N):
        a,b,c = list(map(int,input().split()))
        n = pract(a,b,c)
        vector = (a,b,c)
        distance = n.distance()
        list_.append(distance)
        dis[vector] = distance
    max_distance = max(list_)
    for vector_ in dis.keys():
        if dis[vector_] == max_distance:
            print('Vector {} have the farthest distance = {}'.format(vector_,max_distance))
