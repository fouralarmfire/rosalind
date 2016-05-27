# Problem
# Given: A DNA string at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G' and 'T' occur.
s = 'AGGGCCGGGGATTTCAAATGTCACGTTGCGTTCCACAACAGACAAAGTCGCTACAACTTGCATTT'

# third attempt - works
print [s.count(c) for c in 'ACGT']

# second attempt after more research - works
print s.count("A"), s.count("G"), s.count("C"), s.count("T")

# first attempt - works
x = {}
l = list(s)
for letter in l:
	x[letter] = l.count(letter)

for key, value in x.items():
	print value