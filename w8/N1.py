def print_map(function,iterable):
	a = iter(iterable)
	while True:
		try:
			element = next(a)
			print(function[element])
		except StopIteration:
			break

print_map([1,2,3,4,5],range(5))