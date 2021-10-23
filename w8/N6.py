import itertools

def get_combinations(s, n):
    list_combinations = sorted([''.join(sorted(x)) for i in range(1,n+1) for x in itertools.combinations(s,i)])
    list_combinations.sort(key= lambda x: len(x))
    return list_combinations


print(get_combinations("cat", 2))