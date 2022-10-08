Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=print('hi how are you')
hi how are you
a
a
print(a)
None
def myfun():
    print('this is first fun')

    
myfun()
this is first fun
a=myfun()
this is first fun
print(a)
None
## no input but output
def second():
    return 'abcd'

second()
'abcd'
## abcd in quotes
b=second()
b
'abcd'
##input but no output
def third(x):
    print('hello')

    
third()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    third()
TypeError: third() missing 1 required positional argument: 'x'
third('abc')
hello
def fourth(x):
    return x*10

fourth(10)
100
def fourth(x):
    print("hi")
    print("hello")
    print("mayank")
    return x*10

fourth(20)
hi
hello
mayank
200

= RESTART: C:\Users\lenovo\AppData\Local\Programs\Python\Python310\m5.py
hi

= RESTART: C:\Users\lenovo\AppData\Local\Programs\Python\Python310\m5.py
hi
def fourth(x):
    print('hi')
    return x**2
    print('hello')
    print('world')

fourth(4)
SyntaxError: invalid syntax
def fourth(x):
    print('hi')
    return x**2
    print('hello')
    print('world')

fourth(4)
KeyboardInterrupt
def fourth(x):
    print('hi')
    return x**2
    print('hello')
    print('world')

fourth(3)
hi
9
def five(x,y,z)
SyntaxError: expected ':'
def five(x,y,z):
    return x+y+z

five(4,5,1)
10
def mayank(x,y,z):
    return x+y
    return y+z

mayank(1,2,3)
3

def mayank(x,y,z):
    return (x+y,y+z)

mayank(1,2,3)
(3, 5)
def six(x,y,z)
SyntaxError: expected ':'
def six(x,y,z):
    return x+y+z

six(x=5,y=4,z=3)
12
six(2,3)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    six(2,3)
TypeError: six() missing 1 required positional argument: 'z'
def seven(x,y,z=1)
SyntaxError: expected ':'
def seven(x,y,z=1):
    return x+y+z

seven(1,2)
4
seven(1,2,4)
7
def seven(x=1,y,z=1):
    return x+y+z
SyntaxError: non-default argument follows default argument
def seven(x,y=1,z=1):
    return x+y+z

seven(1,2,3)
6
def eight(*x)
SyntaxError: expected ':'
def eight(*x):
    return x

eight()
()
eight(2)
(2,)
eight(2,3,4)
(2, 3, 4)
## kwargs
def nine(**x)
SyntaxError: expected ':'
def nine(**x):
    return x

nine()
{}
nine(name='bipul',email='bipul@gmail.com')
{'name': 'bipul', 'email': 'bipul@gmail.com'}
def name(x):
    return print("happy birthday to you (x)")

name('m')
happy birthday to you (x)
def name(x):
    return print(f"happy birthday to you (x)")name('m')
SyntaxError: invalid syntax
def name(x):
    return print("happy birthday to you (x)")

name('m')
SyntaxError: invalid syntax
def name(x):
    return print(f"happy birthday to you (x)")

name('m')
happy birthday to you (x)
def name(x):
    return print(f"happy birthday to you {x}")

name('m')
happy birthday to you m
name("mayank")
happy birthday to you mayank
def name(x):
    return print("happy birthday to you {x}",format"x")
SyntaxError: invalid syntax
def name(x):
    return print(f"happy birthday to you {x}")

name('mayank')
happy birthday to you mayank
def name(x):
    return print("happy birthday to you {x}",format{"x"})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def name(x):
    return print("happy birthday to you {x}".format{"x"})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def name(x):
    return print("happy birthday to you {}".format{"x"})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def myfun(2,4,6)
SyntaxError: invalid syntax
def myfun(2,4,6):
    
SyntaxError: invalid syntax
def myfun(x,y,z):
    return x+y+z

myfun(2,4,6)
12
myadd=lambda x,y,z:x+y+z
myadd(1,2,3)
6
math.pi
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    math.pi
NameError: name 'math' is not defined
import math
math.pi
3.141592653589793
math.sqrt(81)
9.0
math.power(2,3)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    math.power(2,3)
AttributeError: module 'math' has no attribute 'power'
math.pow(2,3)
8.0
math.factorial(5)
120
m.pi
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    m.pi
NameError: name 'm' is not defined
math.sqrt(81)
9.0
import math as m
m.pi
3.141592653589793
m.sqrt(81)
9.0
from math import sqrt
sqrt(81)
9.0
import datetime as dt
aaj _ki_date=dt.date.today()
SyntaxError: invalid syntax
aaj_ki_date=dt.date.today()
print(aaj_ki_date)
2022-09-19
import calendar
print(calendar.calendar(2022))
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

>>> print(calendar.month(2022,9))
   September 2022
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30

