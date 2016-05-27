#Problem

#The 20 commonly occurring amino acids are abbreviated by using 20 letters from the
#English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are
#constructed from these 20 symbols. Henceforth, the term genetic string will
#incorporate protein strings along with DNA strings and RNA strings.

#The RNA codon table dictates the details regarding the encoding of specific codons
#into the amino acid alphabet.

#Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#Return: The protein string encoded by s.

with open ("../rna-codon", "r") as file:
  data = file.read().replace('\n', ' ')

with open ("../dataset", "r") as file:
  coded = file.read().replace('\n', '')

rnal = data.split()
rnad = dict(zip(rnal[0::2], rnal[1::2]))

decoded = ''
for x in range(0, len(coded)-3, 3):
  decoded += rnad[coded[x:x+3]]
print decoded

