'''#capitalize only the first letter in each word
s = input()
print(s)
print(' '.join(i.capitalize() for i in s.split(' ')))
'''
#concatination
a="hello"
b="world"
c=a+'_'+b
print(c)
print(a, b , sep="_")
'''
#Uppercase
b=a.upper()
print(b)

#lower
a="Hello"
b=a.lower()
print(b)

#Capitalize
a='hello'
b=a.capitalize()
print(b)

#Swapcase
a="HelloWorld"
b=a.swapcase()
print(b)

#len/type
a="Hello"
print(len(a))
print(type(a))

#find/count
a= "Hello world"
print(a.count('r'))
print(a.count('z'))
print(a.count('e'))
print(a.find('l'))
print(a.find('z'))
print(a.find('e'))

#replace
a = "Hello_world"
b = a.replace("_","*")
print(b)

#* operation in string
a ="Hello"
b = a * 3
print(b)

#strip
a="_Python_"
b=a.lstrip("_")
c=a.rstrip("_")
d=a.strip("_")
print(b)
print(c)
print(d)


#first and last letter to be capital
a=input()
b=a[0].upper() + a[1:-1] +a[-1].upper()
print(b)
'''
#Get 2 string from user , concatinate both and convert middle character to upper case
a=input()
b=input()
c=a+b
print(c)
d=len(c)//2
e=c[:d] +c[d].upper() +c[d+1:]
print(e)

#Split
s = "Hello world"
val1 = s.split()
val2 = s.split("w")
val3 = s.split("ll")
print(val1)
print(val2)
print(val3)
print(type(val1))
print(type(val2))

#format
a = 10
b = 15
c = a+b
print("addition of {0} and {1} is {2}" .format(a,b,c))

