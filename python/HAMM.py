#Counting Point Mutations

#Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
#is the number of corresponding symbols that differ in s and t.

#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#Return: The Hamming distance dH(s,t).

with open ("../dataset", "r") as file:
  data=file.read().replace('\n', ' ')

arr = data.split()

one = arr[0]
two = arr[1]

print sum([x != y for x, y in zip(one, two)])
