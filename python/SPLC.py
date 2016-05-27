#Problem:

#After identifying the exons and introns of an RNA string, we only need to delete
#the introns and concatenate the exons to form a new string ready for translation.

#Given: A DNA string s (of length at most 1 kbp) and a collection of substrings
  #of s acting as introns. All strings are given in FASTA format.

#Return: A protein string resulting from transcribing and translating the exons
  #of s. (Note: Only one solution will exist for the dataset provided.)

# RNA Codon
with open ("../rna-codon", "r") as file:
  rna_codon = file.read().replace('\n', ' ')

rnal = rna_codon.split()
rnad = dict(zip(rnal[0::2], rnal[1::2]))

# Read fasta
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

sequences = []
with open ('../dataset') as fasta:
  for name, seq in read_fasta(fasta):
    sequences.append(seq)

# separates dna_string from substrings
dna_string = sequences.pop(0)

# remove introns, join exons
for i in sequences:
  dna_string = dna_string.replace(i, '')

# translate from dna to rna
coded = dna_string.replace('T', 'U')

# decode proteins
decoded = ''
for x in range(0, len(coded)-3, 3):
  decoded += rnad[coded[x:x+3]]
print decoded
