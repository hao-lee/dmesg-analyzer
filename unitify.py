def to_b(num):
	return num/1
def to_kb(num):
	return num/1024
def to_mb(num):
	return num/1024/1024
def to_gb(num):
	return num/1024/1024/1024

# We can't control zero digits in number, but we can handle it in string
def format_to_string(f):
	s = str(f) # convert to string to retain the precision
	l = list(s)
	idx = len(l) - 1
	while True:
		if l[idx] == '0' or l[idx] == '.':
			del l[idx]
			idx = idx - 1
		else:
			break
	s = ''.join(l)
	return s

def unitify(num):
	value = to_gb(num)
	if value >= 1:
		return "%s GB" %format_to_string(value)
	value = to_mb(num)
	if value >= 1:
		return "%s MB" %format_to_string(value)
	value = to_kb(num)
	if value >= 1:
		return "%s KB" %format_to_string(value)
	value = to_b(num)
	return "%s B" %format_to_string(value)

if __name__ == "__main__":
	print(unitify(0x100))
	print(unitify(1234))
	print(unitify(0xfff))
	print(unitify(4098))
	print(unitify(12345678))
	print(unitify(111111111111))