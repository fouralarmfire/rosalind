# Problem:
#For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is
#the ratio of the total number of transitions to the total number of transversions, where symbol
#substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance.

# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
# Return: Return: The transition/transversion ratio R(s1,s2).

def read_fasta(fasta):
  name, seq = None, []
  for line in fasta:
    line = line.rstrip()
    if line.startswith('>'):
      if name: yield (name, ''.join(seq))
      name, seq = line, []
    else:
      seq.append(line)
  if name: yield (name, ''.join(seq))

sequences = []
with open('../../dataset') as fasta:
    for name, seq in read_fasta(fasta):
      sequences.append(seq)

one = sequences[0]
two = sequences[1]

transitions = { 'A':'G', 'G':'A', 'T':'C', 'C':'T' }
mutations = [0 if transitions[n1] == n2 else 1 for n1, n2 in zip(one, two) if n1 is not n2]

#The same algorithm as above but maybe easier to read
#mutations = []
#for n1, n2 in zip(one, two):
  #if n1 is not n2:
      #if transitions[n1] == n2:
        #mutations.append(0)
      #else:
        #mutations.append(1)

print mutations.count(0) / float(mutations.count(1))
