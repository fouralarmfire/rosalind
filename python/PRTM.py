# Problem:
# In a weighted alphabet, every symbol is assigned a positive real number called a weight.
# A string formed from a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.
# The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.

# Given: A protein string P of length at most 1000 aa.
# Return: The total weight of P. Consult the monoisotopic mass table.

with open ("../monoisotopic-mass-table", "r") as file:
  monoisotopic_mass_table = file.read().replace('\n', ' ')

mmt = monoisotopic_mass_table.split()
mmt = dict(zip(mmt[0::2], mmt[1::2]))
for e in mmt:
  mmt[e] = float(mmt[e])

with open ("../dataset", "r") as file:
  protein = file.read().replace('\n', '')

total = 0
for i in protein:
  total += mmt[i]

print("%.3f" % total)
