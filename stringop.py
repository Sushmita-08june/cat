print("hello","abs",sep='45')
print('value','str',end='e')
print("world")

print('value','str',end='\t')
print('sush')
print("hello","abs",sep='\t')

#Slicing
a = 'whirlpool'
print(a[1:5:1])
print(a[5:1:-1])
print(a[len(a):0:-1])

# enumerate()
str = 'cold'
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))

a = 'Python world!!'
a.replace("!!" , "$")
print(a)

#concatination
b = 'Hi'
c = 'Dear'
print (b + c)

#Repeatation
print (b*3)

#memberhip
print ("o" in a)
print ("h" not in a)

#suppressing escape sequence
print ("ab" + "\t" + "cd")
print ("ab" + r"\t" + "cd")
