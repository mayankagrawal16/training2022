import tkinter as ttk
import pandas as pd

app = ttk.Tk()
app.title("Recommendation System")
app.geometry('400x400')

cols=['user_id','movie_id','rating','ts']
item_cols=['movie_id','title']+[str(i) for i in range(22)]
df=pd.read_csv('u.data',sep='\t',names=cols)
df1=pd.read_csv('u.item',sep='|',encoding='ISO-8859-1',names=item_cols)
movie=pd.merge(df,df1,on='movie_id')

result = ttk.Variable(app)

frame=ttk.Frame(app)
frame.place(x=10,y=10)

box = ttk.Listbox(frame,height=10,width=50)
for title in movie['title'].unique():
    box.insert(ttk.END,title)
#box.grid(row=0,column=0)
box.pack(side='left',fill='y')
#box.place(x=10,y=10)

scroll = ttk.Scrollbar(frame,orient=ttk.VERTICAL)
scroll.config(command = box.yview)
box.config(yscrollcommand=scroll.set)
scroll.pack(side='right',fill='y')


#for row,val in movie.iterrows():
   # box.insert(row+1,val['title'])

box.place(x=10,y=10)

def get_movie():
    pass
ttk.Button(app, text="Find Recommendations", font=('Arial',22),command=get_movie).place(x=200,y=50)
ttk.Label(app, textvariable=result,font=('Arial',22)).place(x=200,y=100)

app.mainloop()
