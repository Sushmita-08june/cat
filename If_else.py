'''#Conditional statements
a = 10
b = 8
if a + b > 15: # while checking the condition it should hv one sentence inside it otherwise it will throw error
    print("Greater than 15") # use 4 spaces instead of tab as git wont support tab option
    print("if statement")
print("Normal program execution")
print("Main program")

#if , else condition
a = 10
b = 4
if a+b > 15:
    print("Greater than 15")
    print("if statement")
else:
    print("less than 15")
    print("else statement")
print("Normal program execution")
print("Main program")

#elif
a = 10
b = 8
if a+b < 15:
    print("Greater than 15")
    print("if statement")
elif a+b==18:
    print("result is 18")
    print("elif statement")
print("Normal program execution")
print("Main program")

#check if the number is positive or negative
a = int(input())
if a < 0:
    print("number is negative")
else:
    print("number is positive")

#check odd or even
a = int(input())
if a % 2 ==0:
    print("number is even")
else:
    print("number is odd")

#check first and last character same or no
a = input()
b = list(a)
if b[0] == b[-1]:
    print("first and last characters are same")
else:
    print("first and last characters are different")

#Middle characters of 2 strings are same or no
a = input()
b = input()
c = list(a)
d = list(b)
if c[len(c)//2] == d[len(d)//2]:
    print("middle character of two strings are same")
else :
    print("middle character of 2 strings are different")
'''
#Get students, get a mark from user. 0>,>100 invalid
#90-100 = A+
#80-89 = A
#70-79 = B+
#60-69 = B
#50-59 = C
#0-49 = Fail
a = int(input())
if a >100 or a<0:
    print("invalid")
elif 90<=a and a<=100:
    print("A+")
elif 80<=a<90:
    print("A")
elif 70<=a<80:
    print("B+")
elif 60<=a<70:
    print("B")
elif 50<=a<60:
    print("C")
elif 1<=a<49:
    print("Fail")
