# gui -graphical user interface

#liraries
###########
#1.tkinter
#2.pyqt
#3.turtle
import tkinter as ttk
app=ttk.Tk()

app.title('My App')

app.geometry('600x400')

ttk.Label(app,text='A simple Text Label').place(x=50,y=50)
ttk.Label(app,text='mayank agrawal').place(x=10,y=30)

def abc():
    print('wow')
ttk.Button(app,text='isko click kardo',command= abc).place(x=100,y=60)

ttk.Button(app,text='ye wala hai',command= lambda:print('wow')).place(x=100,y=120)

app.mainloop()
