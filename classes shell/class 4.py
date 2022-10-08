Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d1={'name':['akash','akshat','sunny'],'age':[25,20,22],}
type(d1)
<class 'dict'>
len(d1)
2
d1[name]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d1[name]
NameError: name 'name' is not defined
d1['name']
['akash', 'akshat', 'sunny']
d1['age']
[25, 20, 22]
d1.keys()
dict_keys(['name', 'age'])
d1.values()
dict_values([['akash', 'akshat', 'sunny'], [25, 20, 22]])
d1.items()
dict_items([('name', ['akash', 'akshat', 'sunny']), ('age', [25, 20, 22])])
print(d1)
{'name': ['akash', 'akshat', 'sunny'], 'age': [25, 20, 22]}
d1['ph_no']=[2223355,219872892,8927080349]
d1
{'name': ['akash', 'akshat', 'sunny'], 'age': [25, 20, 22], 'ph_no': [2223355, 219872892, 8927080349]}
d1['name[0]']
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d1['name[0]']
KeyError: 'name[0]'
d1('name[0]')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d1('name[0]')
TypeError: 'dict' object is not callable
d1('name')[0]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d1('name')[0]
TypeError: 'dict' object is not callable
d1['name'][0]
'akash'
d1['name'][0][:-1]
'akas'
d1['name'][0][::-1]
'hsaka'
d1['name'][0]='mayank'
d1
{'name': ['mayank', 'akshat', 'sunny'], 'age': [25, 20, 22], 'ph_no': [2223355, 219872892, 8927080349]}
d1['name'][3]='dcskjck'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d1['name'][3]='dcskjck'
IndexError: list assignment index out of range
del d1['ph_no']
d1
{'name': ['mayank', 'akshat', 'sunny'], 'age': [25, 20, 22]}
d1['name'].append('gfg')
d1
{'name': ['mayank', 'akshat', 'sunny', 'gfg'], 'age': [25, 20, 22]}
d1['age'].append('7854')
d1
{'name': ['mayank', 'akshat', 'sunny', 'gfg'], 'age': [25, 20, 22, '7854']}
d1.get('name')
['mayank', 'akshat', 'sunny', 'gfg']
a=20
b='ml'
print(a,b)
20 ml
print(a,b,sep='      ')
20      ml
print(a,b,sep='@')
20@ml
print(a)
20
print(b)
ml

======================= RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python310/python class/m1.py =======================
20###ml


======================= RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python310/python class/m1.py =======================
20###ml

======================= RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python310/python class/m1.py =======================
20
ml
a=input('enter your name:')
enter your name:mayank
a
'mayank'
input(a)
mayank
''
input(c)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    input(c)
NameError: name 'c' is not defined
b=input(first no:)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
b=input('first no:')
first no:23
b=input('second no:')
second no:34
input(a+b)
mayank34
''
input(b=input('first no:')
      b=input('first no:')
      
SyntaxError: '(' was never closed
b=input('first no:')
      
first no:23
b=input('second no:')
      
second no:4b=input('second no:')
c=input('second no:')
      
second no:34
input(b+c)
      
4b=input('second no:')34
''
a=int(input('enter your first number'))
      
enter your first number34
b=int(input('enter your second number'))
      
enter your second number43
a+b
      
77

============================== RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python310/m3.py =============================
Traceback (most recent call last):
  File "C:/Users/lenovo/AppData/Local/Programs/Python/Python310/m3.py", line 1, in <module>
    if age<18:
NameError: name 'age' is not defined

============================== RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python310/m3.py =============================
Traceback (most recent call last):
  File "C:/Users/lenovo/AppData/Local/Programs/Python/Python310/m3.py", line 1, in <module>
    input(age)
NameError: name 'age' is not defined

============================== RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python310/m3.py =============================
enter age23
a gift
a task
koi gift nahi h

============================== RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python310/m3.py =============================
enter age18
a gift
a task

============================== RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python310/m3.py =============================
enter age23
koi gift nahi h
>>> 
============================== RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python310/m3.py =============================
enter age18
a gift
a task
>>> 
======================= RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python310/python class/m2.py =======================
enter age34
koi gift nahi h
>>> 
================= RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python310/python class/nested if else.py =================
enter the day=saturday
enter the condition=sick
half day work
>>> 
>>> 
================== RESTART: C:/Users/lenovo/AppData/Local/Programs/Python/Python310/python class/max of three.py ==================
 23
 27
 56
c is the largest
>>> 
>>> range(0,8)
...       
range(0, 8)
>>> list(range(0,11))
...       
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(11))
...       
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(2,101,2))
...       
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
