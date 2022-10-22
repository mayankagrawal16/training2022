from tkinter import *
app=Tk()
app.title('mayank window')

app.geometry('500x500')

app.iconbitmap('palm-tree-icon.png')
app.maxsize(width=600,height=300)
app.minsize(width=600,height=300)

# label
lb1=Label(app,text='enter your weight',bg='red')
lb1.place(x=10,y=10)

# entry
ent=Entry(app, bg='red',fg='black',bd=5)
ent.place(x=150,y=10)

# button
btn=Button(app,text='submit').place(x=10,y=80)
app.mainloop()