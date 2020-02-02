#Sets
set1 = {2,3,7,0,1}
print(set1)
print(type(set1))
print(len(set1))

#add
set1.add(8)
print(set1)
set1.add(7)
print(set1)

#remove and discard
set2 = {2,0,1,-1,3,4,5}
set2.remove(3)
print(set2)
#set2.remove(8) # Throws error as 8 is not present in set
#print(set2)
set2.discard(4)
print(set2)
set2.discard(9)
print(set2)

#updated
set3 = {3,4,0,1,2}
set3.update([3,9,2,7])
print(set3)

#duplicate removal
List1 = [2,2,3,4,5,0,0,0]
List1 = set(List1)
print(List1)

#coversion
List1 = [2,0,0,5,5,5]
List1 = list(set(List1))
print(List1)

#Concat,(check unordered indexing) 
set1 = {7,8,2,0}
set2 = {0,4,5}
set3 = set1 + set2 # throws error. can not concat sets like this way

#Clear
set4 = {5,4,2,0}
set4.clear()
print(set4)

#Copy
set1 = {2,3,4,1}
set2 = set1.copy()
print(set2)

#pop
set1 = {2,3,1,4,5}
set1.pop() # removes random element
print(set1)

