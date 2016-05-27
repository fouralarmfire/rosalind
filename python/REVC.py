# Problem: In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

# first, really long, messy attempt - works but ugh!
def replace(s):
	ls = list(s[::-1])
	for n, i in enumerate(ls):
		if i == 'A':
			ls[n] = 'T'
		if i == 'T':
			ls[n] = 'A'
		if i == 'G':
			ls[n] = 'C'
		if i == 'C':
			ls[n] = 'G'
	s = ''.join(ls)
	return s

# in bash:
rev r.txt | tr ATCG TAGC

# second attempt - works
def replace(s):
	r = []
	d = { 'A':'T', 'T':'A', 'C':'G', 'G':'C' }
	for nuc in s[::-1]:
		r.append(d[nuc])
	return ''.join[r]

