# Problem:
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'.
# For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format.
# In this format, the string is introduced by a line that begins with '>', followed by some labeling information.
# Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
# 		Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated.

# read the dataset/fasta file
def read_fasta(fasta):
	name, seq = None, []
	for line in fasta:
		line = line.rstrip()
		if line.startswith(">"):
			if name: yield (name, ''.join(seq))
			name, seq = line, []
		else:
  		seq.append(line)
	if name: yield (name, ''.join(seq))

# calculate percentage of cytosine / guanine in string
def calc_percent(str, nuc1, nuc2):
	length = len(str)
	target = str.count(nuc1) + str.count(nuc2)
	percentage = 100 * float(target)/float(length)
	return percentage

# extract highest percentage
def give_highest(dictionary):
	ordered = sorted(dictionary.iteritems(), key=lambda (x, y): y)
	print ordered[-1]

# open files, specify nucleotides and pass in methods
def compute_content(dataset, nuc1, nuc2):
	genes = {}
	with open(dataset) as fasta:
		for name, seq in read_fasta(fasta):
			result = calc_percent(seq, nuc1, nuc2)
			genes[name] = result
	give_highest(genes)

