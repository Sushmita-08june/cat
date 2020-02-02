'''a= "18"
b=int(a)
print(b)

#input will accept only string values
a = input()
print(a)
print(type(a))

#adding numbers
b=input("Enter the 1st value:")
print(b)
c=input("Enter the 2nd value:")
print(c)
d=b+c
print("sum of 2 numbers:", d)

#converting to int before adding
b=int(input("Enter the 1st value:"))
print(b)
c=int(input("Enter the 2nd value:"))
print(c)
d=b+c
print("sum of 2 numbers:", d)

#Area of cone area = (1/3)*pi*(r**2)*h
pi = 3.14
r = float(input('enter r value ='))
h = float(input('enter h value ='))
area = (1/3)*pi*(r**2)*h
print('area of cone is =',area)
'''
#dividing numbers and converting type
a = int(input("Enter the 1st value:"))
b = int(input("Enter the 2nd value:"))
c = (a+b) // (a-b)
print(c)
print(type(c))
print(float(c))
print(type(c))
c = float(c)
print(type(c))
