# Problem:
# A permutation of length n is an ordering of the positive integers {1,2,…,n}.
# For example, π=(5,3,2,1,4) is a permutation of length 5.

# Given: A positive integer n≤7.
# Return: The total number of permutations of length n, followed by a list of
# all such permutations (in any order).

s = (1..Integer(ARGV[0])).to_a.permutation.map { |p| p.join(" ") }
puts s.length, s
