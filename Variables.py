'''variable creation rules
1.A variable name must start with a letter or the underscore character.
2.A variable name cannot start with number
3.A variable name can only contain alpha-numeric characters and uderscores(A-z,0-9,and_)
4.Variable names are case-sensitive(age,Age and AGE are 3 different variables)
'''

#printing variables and their type
a = 7
b = 8
print(a)
print(b)
print(type(a))
print(type(b))

#Adding 2 numbers
a = 7
b = 8
c = a+b
print(c)

#calculating area of circle, area = pi * (r ** 2)
pi = 3.14
r = 9
area = pi * (r ** 2)
print("area of circle is", area)
print(type(area))

#Calculating circumference of circle circum = 2 * pi * r
pi = 3.14
r = 8
circum = 2 * pi * r
print("circumference of circle is",circum)

#Area of cone area = (1/3)*pi*(r**2)*h
pi = 3.14
r = 9
h = 6
area = (1/3)*pi*(r**2)*h
print('area of cone is',area)

#checking type of variable after conversion
a = 7
b = 8.9
c = int(b)
d = float(a)
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
