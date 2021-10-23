import itertools

def get_permutations(s, n):
	return sorted(''.join(i) for i in itertools.permutations(s,n))
print(get_permutations("cat", 2))