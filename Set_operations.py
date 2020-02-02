'''#set Union
set1 = {1,2,3,4,0,-1,-2}
set2 = {-1,-2,5,6,7,8,1,2,0,7}
set1 = set1.union(set2)
print(set1)

#Set Intersection (you can store value in different set)
set1 = {-1,-2,-3,0,1}
set2 = {0,1,2,3,4,5}
set1 = set1.intersection(set2)
print(set1)

#Intersection update (Used to update the available set itself)
set1 = {1,2,3,4,0,-1,-2}
set2 = {0,1,2,3,-3,-5,-6}
set1.intersection_update(set2)
print(set1)

#Difference
set1 = {-1,-2,-3,-4,0}
set2 = {-1,0,-2,-3,4,5}
set1 = set1.difference(set2)
print(set1)

#Difference update
set1 = {1,2,3,4,5,-1,-2,0}
set2 = {0,1,2,3,-1,4,5,7,8,9}
set1.difference_update(set2)
print(set1)
'''
#Symmetric difference
set1 = {0,1,2,3,-1}
set2 = {0,-1,-2,-3,-4}
set3 = set1.symmetric_difference(set2)
print(set3)
'''
#Symmetric difference update
set1 = {0,1,2,3,-1}
set2 = {0,-1,-2,-3,-4}
set1.symmetric_difference_update(set2)
print(set1)

#disjoint
set1 = {0,1,2,3,4}
set2 = {1,0,-1,-2,-3}
print(set1.isdisjoint(set2))
set3 = {5,6,7,8}
print(set1.isdisjoint(set3))

#superset
set1 = {1,2,3,4,5}
set2 = {4,5}
print(set1.issuperset(set2))
print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set2.issubset(set1))
'''
