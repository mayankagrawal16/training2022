Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a='rhagiugiuwg'
b="jfwfoioaghho"
c='''rejfuagywufak
gwfvHMHjvhj
gfGWUYAEGkjss
agagagtg'''
print(c)
rejfuagywufak
gwfvHMHjvhj
gfGWUYAEGkjss
agagagtg
a='helllo world'
print(a)
helllo world
a[0]
'h'
a[6]
' '
a[10]
'l'
a[-1]
'd'
a[10]
'l'
a[11]
'd'
hello world
SyntaxError: invalid syntax
a='helllo world'
a[0:1]
'h'
h[0:2]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    h[0:2]
NameError: name 'h' is not defined
NameError: name 'h' is not defined
SyntaxError: invalid syntax
a[0:2]
'he'
a='helllo world'
a[4:6]
'lo'
a='hello world'
a[3:5]
'lo'
a[:10:2]
'hlowr'
a[-1::-1]
'dlrow olleh'
a[::-1]
'dlrow olleh'
a[-1:-11:-1]
'dlrow olle'
a[-1:-12:-1]
'dlrow olleh'
a[-7::-1]
'olleh'
a[-8:-6]
'lo'
a='hello world'
a.capatlize
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.capatlize
AttributeError: 'str' object has no attribute 'capatlize'. Did you mean: 'capitalize'?
a.capitalize()
'Hello world'
a
'hello world'
a.centre(50)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.centre(50)
AttributeError: 'str' object has no attribute 'centre'. Did you mean: 'center'?
a.center(50)
'                   hello world                    '
a.center(50,'#')
'###################hello world####################'
a.count('1')
0
a=a.centre(50)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a=a.centre(50)
AttributeError: 'str' object has no attribute 'centre'. Did you mean: 'center'?
a=a.center(50)
a
'                   hello world                    '
a.lstrip()
'hello world                    '
a.rstrip()
'                   hello world'
a.strip()
'hello world'
a=a.strip()
a
'hello world'
a.isupper()
False
a.islower
<built-in method islower of str object at 0x000001794C77B4B0>
a.islower()
True
a.upper()
'HELLO WORLD'
a.lower()
'hello world'
a=a.upper()
a
'HELLO WORLD'
a.lower()
'hello world'
a.startswith('he')
False
a
'HELLO WORLD'
a.edswith('D')
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.edswith('D')
AttributeError: 'str' object has no attribute 'edswith'. Did you mean: 'endswith'?
a.endswith('D')
True
len(a)
11
a
'HELLO WORLD'
a[0]='M'
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a[0]='M'
TypeError: 'str' object does not support item assignment
del a[0]
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    del a[0]
TypeError: 'str' object doesn't support item deletion
b='akshat123@gmail.com'
b.split('@')
['akshat123', 'gmail.com']
b=b.split('@')
b
['akshat123', 'gmail.com']
'@'.join(b)
'akshat123@gmail.com'
a.count('l')
0
a='helllo world'
a.count(l)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.count(l)
NameError: name 'l' is not defined
a.count('l')
4
m=[12,'hi',2.3,500]
m[0]
12
m[1:3]
['hi', 2.3]
'hi' in m
True
'hello' in m
False
'hello'  not in m
True
2*m
[12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500]
##repetition
m+=['new value']
m
[12, 'hi', 2.3, 500, 'new value']
m.append('abc')
m
[12, 'hi', 2.3, 500, 'new value', 'abc']
m.append('x','y')
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    m.append('x','y')
TypeError: list.append() takes exactly one argument (2 given)
m.extend(['x','y','kuch bhi'])
m
[12, 'hi', 2.3, 500, 'new value', 'abc', 'x', 'y', 'kuch bhi']
a.insert('hello',2)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.insert('hello',2)
AttributeError: 'str' object has no attribute 'insert'
m.insert('hello',2)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    m.insert('hello',2)
TypeError: 'str' object cannot be interpreted as an integer
m.insert(2,'hello')
m
[12, 'hi', 'hello', 2.3, 500, 'new value', 'abc', 'x', 'y', 'kuch bhi']
m.pop()
'kuch bhi'
mp=m.pop()
mp
'y'
m.pop(0)
12
m
['hi', 'hello', 2.3, 500, 'new value', 'abc', 'x']
m.pop('hi')
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    m.pop('hi')
TypeError: 'str' object cannot be interpreted as an integer
m.pop(1)
'hello'
m.clear()
m
[]
n=[100,32,12,45]
n.sort()
n
[12, 32, 45, 100]
n.reverse()
n
[100, 45, 32, 12]
max(n)
100
min(n)
12
m
[]
m=[12,'hi',2.3,500,'new value']
m..index[''hi]
SyntaxError: invalid syntax
m.index['hi']
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    m.index['hi']
TypeError: 'builtin_function_or_method' object is not subscriptable
m=[12,'hi',2.3,500,'new value']
m.index('hi')
1
m[1][0]
'h'
t=52,23,'abc'
type(t)
<class 'tuple'>
len(t)
3
t.index('abc')
2
t[0]
52
t[:2]
(52, 23)
t[0]=23
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    t[0]=23
TypeError: 'tuple' object does not support item assignment
t
(52, 23, 'abc')
k=(52,23,85,(5,'abc',5.5),100)
type(t)
<class 'tuple'>
type(k)
<class 'tuple'>
k[3]
(5, 'abc', 5.5)
k[3[0]]
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    k[3[0]]
TypeError: 'int' object is not subscriptable
k[3][1]
'abc'
k[3][1][1]
'b'
## HW-to add value in an tupple
s={1,1,2,2,3,4,4,3}
type(s)
<class 'set'>
print(s)
{1, 2, 3, 4}
s[0]
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s[0:2]
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    s[0:2]
TypeError: 'set' object is not subscriptable
s
{1, 2, 3, 4}
s2={23,3,41,4}
s.intersetion(s2)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    s.intersetion(s2)
AttributeError: 'set' object has no attribute 'intersetion'. Did you mean: 'intersection'?
>>> s.intersection(s2)
{3, 4}
>>> s.union(s2)
{1, 2, 3, 4, 41, 23}
>>> s.add(100)
>>> s
{1, 2, 3, 100, 4}
>>> ##unordered
>>> s.discard(100)
>>> s
{1, 2, 3, 4}
>>> s.remove(3)
>>> s
{1, 2, 4}
>>> pop(s)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    pop(s)
NameError: name 'pop' is not defined. Did you mean: 'pow'?
>>> pop(1)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    pop(1)
NameError: name 'pop' is not defined. Did you mean: 'pow'?
>>> s.pop(0)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    s.pop(0)
TypeError: set.pop() takes no arguments (1 given)
>>> s1={44,22,33}
>>> s.update(s1)
>>> s
{1, 2, 33, 4, 44, 22}
>>> s.clear()
>>> s
set()
>>> #max,min,len
