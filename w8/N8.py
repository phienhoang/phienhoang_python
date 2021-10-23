import itertools

def compress_string(s):
	a = itertools.groupby(s)
	b = []
	c = []
	for key, value in a:
		b.append(int(key))
		c.append(len(list(value)))
	return list(zip(c,b))
print(compress_string('1222311'))