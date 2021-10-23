import itertools

def maximize(lists, m):
	list_kvadpat = list(max(i)**2 for i in lists)
	list_sum = list(j for j in itertools.accumulate(list_kvadpat))
	return max(list_sum) % m

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print(maximize(lists, m=1000))