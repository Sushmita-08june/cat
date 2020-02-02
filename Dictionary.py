'''val1 = {1:"maths",2:"statistics",3:"game theory",4:"DBMS"}
print(val1)
#print(val1[0]) # throws error because key 0 does not exist 
print(val1[1])

#add/replace
print(type(val1))
print(len(val1))
print(val1.keys())
print(val1.values())
print(val1.items())
val1[5] = "os"
val1[6] = "okay"
print(val1)
val1[4] = "Mining"
print(val1)
print(val1.get(3))

#Update
val2 = {9:"graphics",10:"java"}
val1.update(val2)
print(val1)

#pop/popitem
print(val1)
val1.pop(6)
print(val1)
val1.popitem()
print(val1)

#clear/copy
val3 = val1.copy()
print(val3)
val3.clear()
print(val3)
'''

A = {1 : {"papers" : ["c" , "c++" , "DS1"], "Arr" : ["DS1", "c"], "Top score" : ["c++"] },
     2 : {"Lab" : ["DS2"] , "others" : ["EG" , "oops"]}, 3 : {"seminars" : ("DBMS" , "Mining")},
     4 : {"projects" : { "project1" : "game theory" , "project2" : "ML"},
      "papers" : ("AI", "Industry paper")}}

#print(A)

#print(A[1])
print(A[1]["papers"][1])
print(A[1]["Arr"][0])
print(A[1]["Top score"][0])
print(A[2].keys()) # print keys
print(A[3]["seminars"][1])
print(A[4].keys())
print(A[4]["projects"]["project1"])
print(A[4]["projects"]["project2"])
print(A[4]["papers"])
print(A[4]["papers"][0])
print(A[4]["papers"][1])
