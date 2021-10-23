import itertools

def get_combinations_with_r(s, n):
	return sorted(''.join(sorted(i)) for i in itertools.combinations_with_replacement(s, n))

	
print(get_combinations_with_r("cat", 2))
