# Problem: a DNA string corresponding to a coding strand, its transcribed RNA string is formed by replacing all occurrences of 'T' in t with 'U' in u
# Given: A DNA string t having length at most 1000 nt
# Return: The transcribed RNA string of t.

t = 'GATGGAACTTGACTACGTAAATT'

u = s.replace('T', 'U')

# or in command line:
tr T U < rosalind_rna.txt