#Create an empty list
a=[]

#add -1 at position 0
a.insert(0,-1)
print(a)

#add 3 at the end
a.append(3)
print(a)

#add [-1,-2,-3,0,1,4,5]
a1=[-1,-2,-3,0,1,4,5]
a2=a+a1
print(a2)

#find index value of 0
print(a2.index(0))

#Find the number of occurence of -1 in list
print(a2.count(-1))

#extend your list with [0,-9,9]
a3=[0,-9,9]
a2.extend(a3)
print(a2)

#find mean, median of list
print("Mean= ",(sum(a2)/len(a2)))
a2.sort()
c=len(a2)
if c%2==0:
    print("Median of a2 =",a2[c//2])
else:
    print("Median of a2 =",((a2[c//2])+(a2[(c//2)+1]))/2)

#Find Middle element in list
#Find second lowest element in list
a2.sort()
print("Second lowest element in list is ",a[1])

