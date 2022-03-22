
from tkinter import *
from PIL import ImageTk,Image
t=Tk()
t.geometry('900x700')

p=Image.open("C:\\Users\\Muhammed kamil hm\\Desktop\\Tkinter_sample3\\bg.jpg")
p=p.resize((900,700))
p=ImageTk.PhotoImage(p)
pic=Label(t,image=p)
pic.place(x=0,y=0)

import pymysql
x=pymysql.connect(host='localhost',user='root',password='kamil@avodha',db='company')
cur=x.cursor()


Label(text='employee',fg='black',font=('times new roman',30,'bold')).place(x=100,y=5)


Label(text='Name : ',bg='yellow',font='italic').place(x=10,y=80)
nm=Entry(width=50)
nm.place(x=95,y=80)


Label(text='age : ',bg='yellow',font='italic').place(x=10,y=140)
ag=Entry(width=50)
ag.place(x=85,y=140)

Label(text='job : ',bg='yellow',font='italic').place(x=10,y=200)
dp=Entry(width=50)
dp.place(x=100,y=200)


Label(text='salary : ',bg='yellow',font='italic').place(x=10,y=260)
sx=Entry(width=50)
sx.place(x=95,y=260)



def abcd():
    import pymysql
    x=pymysql.connect(host='localhost',user='root',password='kamil@avodha',db='company')
    cur=x.cursor()
    n=nm.get()
    
    a=ag.get()
    d=dp.get()
    s=sx.get()
    cur.execute('insert into worker values(%s,%s,%s,%s)',(n,a,d,s))
    x.commit()
    




Button(text='submit',bg='silver',font='italic',command=abcd).place(x=40,y=300)



Label(text='UPDATE',fg='black',font=('times new roman',30,'bold')).place(x=90,y=370)




Label(text='Name : ',bg='yellow',font='italic').place(x=10,y=450)
un=Entry(width=50)
un.place(x=95,y=450)


Label(text='age : ',bg='yellow',font='italic').place(x=10,y=500)
ua=Entry(width=50)
ua.place(x=75,y=500)


Label(text='job : ',bg='yellow',font='italic').place(x=10,y=550)
ud=Entry(width=50)
ud.place(x=100,y=550)



Label(text='salary : ',bg='yellow',font='italic').place(x=10,y=600)
us=Entry(width=50)
us.place(x=95,y=600)



def upd():
    import pymysql
    x=pymysql.connect(host='localhost',user='root',password='kamil@avodha',db='company')
    cur=x.cursor()
    unw=un.get()
    uaw=ua.get()
    udw=ud.get()
    usw=us.get()
    cur.execute('update worker set age=%s where name=%s',(uaw,unw))
    cur.execute('update worker set sex=%s where department=%s',(usw,udw)) 
    x.commit()
    
    



Button(text='apply',bg='red',font='italic',command=upd).place(x=40,y=650)



sc=Scrollbar()
sc.pack(side=RIGHT,fill=Y)
tx=Text(height=20,width=30)
sc.config(command=tx.yview)
tx.place(x=600,y=10)
tx.insert(INSERT,('click on view data button\nto see \navailable\ndata sets'))



def view():
    import pymysql
    x=pymysql.connect(host='localhost',user='root',password='kamil@avodha',db='company')
    cur=x.cursor()
    cur.execute('select * from worker')
    v=cur.fetchall()
    vn=[','.join(map(str,xd))for xd in v]   
    
    tx.delete('1.0',END)
    tx.insert(INSERT,('DARTA SETS ARE\n'))
    for i in vn:
        tx.insert(INSERT,('%s\n\n'%i))




Button(text='View Data',bg='indigo',font='white',command=view).place(x=550,y=400)





    

t.mainloop()












