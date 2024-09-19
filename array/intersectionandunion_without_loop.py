list1 = [2, 3, 4, 5, 6, 7]
list2 = [4, 5, 8, 9, 10]

intersection = list(set(list1) & set(list2))
union = list(set(list1) | set(list2))

print("Union:", union)
print("Intersection:", intersection)

# Note 
# here & operator is used as intersection operator
# and | operator is used as union operator





#using list comprehension
# list1 = [2, 3, 4, 5, 6, 7]
# list2 = [4, 5, 8, 9, 10]


# intersection = [x for x in list1 if x in list2]

# union = list1 + [x for x in list2 if x not in list1]

# print("Union:", union)
# print("Intersection:", intersection)
