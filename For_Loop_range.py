'''#print first and last letters of each word in list
s=""
list1 = ["Python","Java","DBMS","SQL"]
for i in list1:
  s = s + i[0] + i[-1]  
print(s)

#print middle letters of all words
a = ""
list1 = ["Python","Java","DBMS","SQL"]
for i in list1:
    a = a + i[len(i)//2]
print(a)

#find the number of vowels present in given string
b = input()
num=0
for i in b:
    if i == 'a':
        num = num+1
    if i == 'e':
        num = num+1
    if i == 'i':
        num = num+1
    if i == 'o':
        num = num+1
    if i == 'u':
        num = num+1
print(num)

#even count and odd count
even_count = 0
odd_count = 0
list1 = ["Python","Java","DBMS","SQL"]
for i in list1:
    if len(i)%2==0:
        even_count = even_count+1
    else :
        odd_count = odd_count+1
print("Even lenth words in list are",even_count)
print("Odd lenth words in list are",odd_count)

#reverse and concat the words in list
list1=["Python","Java","DBMS","SQL"]
s=""
for i in list1:
    s = s+i[::-1]
print(s)

#Range function
for i in range(5):
    print(i)
for i in range(6,11):
    print(i)
for i in range(10,50,6):
    print(i)
for i in range(10,0,-1):
    print(i)

#reverse and concat words in list and list itself

list1=["Python","Java","DBMS","SQL"]
s=""
list2=list1[::-1]
for i in list2:
    s = s+i[::-1]
print(s)

#reverse and concat words in list and list itself using range function
list1=["Python","Java","DBMS","SQL"]
n = len(list1)
s=""
for i in range(n-1,-1,-1):
    s=s+list1[i][::-1]
print(s)

#print 100,92,84,76,68
for i in range(100,60,-8):
  print(i)

#task
#take input from user for how many lines of code you want to execute,
#then execute only those number of lines

a = int(input())
b=[]
for i in range(0,a):
  c=input()
  b.append(c)
print(b)

#task Imp
#take input from user
#1-n print all numbers
#divisible by 3 -> Fizz
#divisible by 5 -> Buzz
#divisible by 3 & 5 -> Fizz Buzz
#others -> NA
#O/p
#1 NA
#2 NA
#3 Fizz
a = int(input())
for i in range(1,a+1):
  print(i, end="  ")
  if (i % 3 == 0) and (i % 5 == 0):
    print("Fizz Buzz")
  elif (i % 3 == 0):
    print("Fizz")
  elif (i % 5 == 0):
    print("Buzz")
  else:
    print("NA")
'''
