# Problem:
# A permutation of length n is an ordering of the positive integers {1,2,…,n}.
# For example, π=(5,3,2,1,4) is a permutation of length 5.

# Given: A positive integer n≤7.
# Return: The total number of permutations of length n, followed by a list of
# all such permutations (in any order).

with open("../dataset", "r") as file:
  n = int(file.read())

a = []
while n > 0:
  a.append(n)
  n -= 1

def permutations(list):
  if len(list) <= 1:
    yield list
  else:
    for perm in permutations(list[1:]):
      for i in range(len(perm)+1):
        yield perm[:i] + list[0:1] + perm[i:]

count = 0
for p in permutations(a):
  print str(p).strip('[]').replace(',', '')
  count += 1

print count
