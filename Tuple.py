#Tuple
tuple1 = (7,8,2,3,4,"Python","Hi")
print(tuple1)
print(type(tuple1))
print(len(tuple1))
tuple2 = (8.0,7.23,False,True,9)
print(tuple2)
print(tuple2[2])
print(tuple1[-1])

#Concat
tuple3 = tuple1 + tuple2
print(tuple3)
tuple4 = tuple3 + (7,8,9)
print(tuple4)
tuple5 = (2,0,1) + (3,2,4)
print(tuple5)

#Multiply
tuple6 = tuple5 * 3
print(tuple6)

#Slicing/indexing
tuple7 = tuple6[-8:]
print(tuple7)
tuple8 = tuple7[2:5] + tuple2[1:]
print(tuple8)

#Replace element in list
Li1=[7,8,2,4,3]
Li1[-3] = 9
print(Li1)
'''tuple1 = (7,8,2,4,3)
tuple1[-3] = 9 # Throws error as it is immutable
print(tuple1)'''

#Tuple to list
val1 = (9,2,3,4)
print(val1)
print(type(val1))
val1 = list(val1)
print(val1)
print(type(val1))

#Conversion
#List to tuple
Val1=[7,8,9,-1]
print(Val1)
print(type(val1))
val1=tuple(val1)
print(val1)
print(type(val1))
