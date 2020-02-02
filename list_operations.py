#reverse
a1=[2,3,0,-1,4,2]
a1.reverse()
print(a1)

#sort
a1=[0,1,2,-1,-2,-3,5]
a1.sort()
print(a1)

#copy
a1=[2,3,0,-1,4,5]
a2=a1.copy()
print(a2)
a3=a1
print(a3)

#multiply
a1=[2,3,4,5,6]
a2=a1*2
print(a2)

#Max/Min/Sum
a1=[2,3,0,2,1,4,5]
print(min(a1))
print(max(a1))
print(sum(a1))

#clear
a1=[2,3,0]
a1.clear()
print(a1)

#pop
a1=[2,8,0,1,-1,3]
a1.pop(1)
print(a1)
a1.pop(3)
print(a1)

#Extend
a1=[2,3,4,5]
a2=[1,0,-1,-3]
a1.extend(a2)
print(a1)

#index
a1=[5,3,4,0,1,2]
print(a1.index(0))
print(a1.index(5))

#count
a1=[2,2,3,4,5,6,6,6]
print(a1.count(2))
print(a1.count(6))

#append
a1=[2,3,4,5,6,7]
print(a1)
a1.append(-1)
print(a1)
a1.append(8)
print(a1)

#insert
a1=[9,8,2,3,4,1]
a1.insert(2,-1)
print(a1)
a1.insert(1,-3)
print(a1)

#remove
a1=[2,3,4,0,1,2]
a1.remove(3)
print(a1)
a1.remove(0)
print(a1)

#concat
a1=[0,1,2,3,-1]
a2=[-1,-2,-2,-4]
a3=a1+a2
print(a3)
a4=[2,3] + [0,1]
print(a4)
a5=a4+[0,0]
print(a5)

#join
a1=["Hello","world","Python"]
a2="_".join(a1)
print(a2)
