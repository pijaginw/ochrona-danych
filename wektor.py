import sys

def textToNum(text):
	t = []
	for c in text:
		t.append(ord(c))

	print t
	return t

if __name__ == '__main__':
	if len(sys.argv) > 1:
		textToNum(sys.argv[1])