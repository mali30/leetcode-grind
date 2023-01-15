my_set = {1, 2, 3, 4, 4, 5}
another_set = set()
another_set.add(1)
another_set.add(1)
print(another_set)
print(my_set)

# union of sets
# Union of A and B is a set of all elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print('union', set1.union(set2))

# Intersection of A and B is a set of elements that are common in both the sets.
print('intersection', set1.intersection(set2))

# Difference of the set B from set A(A - B) is a set of elements that are only in A but not in B.
# Similarly, B - A is a set of elements in B but not in A.
print('difference', set1.difference(set2))
print('difference', set2.difference(set1))

# number example
a = 1
a = 2
print(a)



my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(4)
my_set.add(4)
my_set.remove(4)
print(my_set)