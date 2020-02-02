Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = "0123456789"
>>> print(a[1:5:2])
13
>>> 
>>> print(a[1:9:2])
1357
>>> print(a[1:10:4])
159
>>> b = "abcd"
>>> c = a + b
>>> print(c)
0123456789abcd
>>> print(c * 2, sep="_")
0123456789abcd0123456789abcd
>>> print(c + b * 2)
0123456789abcdabcdabcd
>>> print((c+b)*2)
0123456789abcdabcd0123456789abcdabcd
>>> 

>>> print(a[5])
5
>>> print(a[3:9])
345678
>>> print("5" in a)
True
>>> print("7" not in a)
False
>>> d = "Hi %s" ("homer")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d = "Hi %s" ("homer")
TypeError: 'str' object is not callable
>>> d = "Hi %s" % ("homer")
>>> print (a)
0123456789
>>> print (d)
Hi homer
>>> d = "Hi %c" % ("homer")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d = "Hi %c" % ("homer")
TypeError: %c requires int or char
>>> d = "Hi %c" % ("h")
>>> print(d)
Hi h
>>> d = "Hi %c" % 1
>>> print(d)
Hi 
>>> d = "Hi %c" % 3
>>> print(d)
Hi 
>>> 

>>> c= a + \t + b
SyntaxError: unexpected character after line continuation character
>>> c= a + "\t" + b
>>> print(c)
0123456789	abcd
>>> c= a + r"\t" + b
>>> print(c)
0123456789\tabcd
>>> s =('Hello '
        'world')
>>> print(s)
Hello world
>>> print("or" in s)
True
>>> print('e','w' in s)
e True
>>> print('ew' not in s)
True
>>> print (('e','w') in s)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print (('e','w') in s)
TypeError: 'in <string>' requires string as left operand, not tuple
>>> str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))
SyntaxError: multiple statements found while compiling a single statement
>>> str = 'cold'
>>> 
=========== RESTART: C:/Users/user/Desktop/workspace/str_continued.py ==========
list(enumerate(str) =  [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
len(str) =  4
>>> print(['e','w'] in s)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(['e','w'] in s)
NameError: name 's' is not defined
>>> s =('Hello '
        'world')
>>> print(['e','w'] in s)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(['e','w'] in s)
TypeError: 'in <string>' requires string as left operand, not list
>>> print("or" in [)
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> print("or" in ["or", "im"])
True
>>> b = welc
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    b = welc
NameError: name 'welc' is not defined
>>> b = ''welc
SyntaxError: invalid syntax
>>> b='welc'
>>> b.center(11,' ')
'    welc   '
>>> b.center(11,'2')
'2222welc222'
>>> 
