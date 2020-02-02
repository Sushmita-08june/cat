'''#List
Li1=[7,8,9,2,0,7]
print(Li1)
print(type(Li1))
print(len(Li1))
print(Li1[0])
print(Li1[-1])
Li1 = [8,9.2,3,True,"Python","a"]
print(Li1)
print(Li1[2])
print(Li1[-2])

#List with 2 string , 2 int and 2 float
Li2 = ['abc','bad',2 , 5, 2.2 , 3.4]
print(Li2)
a = Li2[0]
print(a[len(Li2[0]) // 2])
or

print(Li2[0][len(Li2[0])//2]) #EX:a[0][0] = p

#find middle character of middle string in list which has 5 strings
a = ["hello","world","fruit","string","float"]
print(a)
print(a[len(a)//2][len(a[len(a)//2])//2])
'''
#print 6,10,13,17,20,22,24,26,28,29,31,32
b = [3,4,5,6,7,[[9,10,11,12],[13,14,15],[16,17,18],[19,20,21]],[22,23,24,[25,26,27,[28,29,30],31],32]]

print(b)
print(b[3])
print(b[5][0][1])
print(b[5][1][0])
print(b[5][2][1])
print(b[5][3][1])
print(b[6][0])
print(b[6][2])
print(b[6][3][1])
print(b[6][3][3][0])
print(b[6][3][3][1])
print(b[6][3][4])
print(b[6][-1])
