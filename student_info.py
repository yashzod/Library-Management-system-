from tkinter import*
import home

def student_info(root, c, conn):
    canvas=Canvas(root,bg='SlateGray2')
    canvas.place(x=0,y=0,width=900,height=500)
    
    canvas=Canvas(root,bg='white')
    canvas.place(x=200,y=100,width=500,height=300)
    
    txt='NEW STUDENT INFORMATION'
    label= Label(root,bg='white',bd=5,text=txt,font=('',20))
    label.place(x=175,y=30,width=550)

    ##back button
    button=Button(root,text='BACK',font=('',12),
                  command=lambda: home.home(root, c, conn))
    button.place(x=10,y=10)
    
    #STUDENT ENTRIES
    
    ##Alignment
    x1,y1,x2,y2=345,50,80,85
    
    entrys1=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys2=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys3=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys4=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys5=Entry(root,bd=5,bg='white',fg='black',font=(50))
    #########################################################################
    entrys1.place(x=x1+x2,y=1*y1+y2)
    entrys2.place(x=x1+x2,y=2*y1+y2)
    entrys3.place(x=x1+x2,y=3*y1+y2)
    entrys4.place(x=x1+x2,y=4*y1+y2)
    entrys5.place(x=x1+x2,y=5*y1+y2)
    #########################################################################
    
    ##LABELS
    
    ##Alignment
    x1,y1,x2,y2=110,50,130,81
    
    labels1= Label(root,bg='white',bd=5,text='Student Name',font=('',15))
    labels2= Label(root,bg='white',bd=5,text='Year',font=('',15))
    labels3= Label(root,bg='white',bd=5,text='Division',font=('',15))
    labels4= Label(root,bg='white',bd=5,text='mobile number',font=('',15))
    labels5= Label(root,bg='white',bd=5,text='Student Id',font=('',15))
    #########################################################################
    labels1.place(x=x1+x2,y=1*y1+y2)
    labels2.place(x=x1+x2,y=2*y1+y2)
    labels3.place(x=x1+x2,y=3*y1+y2)
    labels4.place(x=x1+x2,y=4*y1+y2)
    labels5.place(x=x1+x2,y=5*y1+y2)
    #####################

    ##insert record
    def inserts():
        ##get values from respective entry box
        name=entrys1.get()
        year=entrys2.get()
        division=entrys3.get()
        mo_no=entrys4.get()

        ##get student id to be given from database.
        for i in c.execute('SELECT * FROM record'):
            id=int(i[0])

        ##delete any value from student id entry box
        entrys5.delete(0, END)
        entrys5.insert(0,'0'+str(id))
        
        ui=str(int(id)+1)

        ##update record
        c.execute('''UPDATE record SET student=? WHERE n=1''',(str(id+1),))
        conn.commit()
        id=str(id)
        c.execute('''INSERT INTO student_info(id,name,year,division,mo_no)
                            VALUES(?,?,?,?,?)''',(id,name,year,division,mo_no))
        conn.commit()
        txt='Your assigned ID is 0'+str(id)
        labeln=Label(root,bg='white',bd=5,text=txt,font=('',15))
        labeln.place(x=50,y=450,width=650)

    ##Clear Entry Values
    def clear():
        entrys1.delete(0, END)
        entrys2.delete(0, END)
        entrys3.delete(0, END)
        entrys4.delete(0, END)
        entrys5.delete(0, END)

    #################
    button1=Button(root,text='CLEAR',font=('',12),command=clear)
    button1.place(x=250,y=410)
    button2=Button(root,text='SUBMIT',font=('',12),command=inserts)
    button2.place(x=450,y=410)


    
