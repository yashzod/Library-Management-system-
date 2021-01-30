from tkinter import*
import home


def book_info(root, c, conn):
    canvas=Canvas(root,bg='SlateGray2')
    canvas.place(x=0,y=0,width=900,height=500)
    canvas=Canvas(root,bg='white')
    canvas.place(x=200,y=100,width=500,height=300)
    
    txt='NEW BOOK INFORMATION'
    label= Label(root,bg='white',bd=5,text=txt,font=('',20))
    label.place(x=175,y=30,width=550)

    ##back button to home page
    button=Button(root,text='BACK',font=('',12),
                  command=lambda: home.home(root, c, conn))
    button.place(x=10,y=10)

    #######BOOK ENTRIES#######

    ##alignment
    x1,y1,x2,y2=345,50,80,85
    
    entryb1=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb2=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb3=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb4=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb5=Entry(root,bd=5,bg='white',fg='black',font=(50))
    ################
    entryb1.place(x=x1+x2,y=1*y1+y2)
    entryb2.place(x=x1+x2,y=2*y1+y2)
    entryb3.place(x=x1+x2,y=3*y1+y2)
    entryb4.place(x=x1+x2,y=4*y1+y2)
    entryb5.place(x=x1+x2,y=5*y1+y2)
    
    ##################
    ##LABELS

    ##alignment
    x1,y1,x2,y2=110,50,130,81
    
    labelb1= Label(root,bg='white',bd=5,text='Title',font=('',15))
    labelb2= Label(root,bg='white',bd=5,text='Author',font=('',15))
    labelb3= Label(root,bg='white',bd=5,text='Publication',font=('',15))
    labelb4= Label(root,bg='white',bd=5,text='Department',font=('',15))
    labelb5= Label(root,bg='white',bd=5,text='Book Id',font=('',15))
    ################
    labelb1.place(x=x1+x2,y=1*y1+y2)
    labelb2.place(x=x1+x2,y=2*y1+y2)
    labelb3.place(x=x1+x2,y=3*y1+y2)
    labelb4.place(x=x1+x2,y=4*y1+y2)
    labelb5.place(x=x1+x2,y=5*y1+y2)
    #####################
    
    ##insert data in database
    def inserts():
        name=entryb1.get()
        author=entryb2.get()
        pub=entryb3.get()
        dep=entryb4.get()

        ##get book id to be assigned from database
        for i in c.execute('SELECT * FROM record'):
            id=int(i[1])
            
        entryb5.delete(0, END)
        entryb5.insert(0,'1'+str(id))
        ui=str(int(id)+1)
        c.execute('''UPDATE record SET book=? WHERE n=1''',(str(id+1),))
        conn.commit()
        id=str(id)
        c.execute('''INSERT INTO book_info(id,title,author,publication,department,availablity)
                            VALUES(?,?,?,?,?,True)''',(id,name,author,pub,dep))
        conn.commit()
        txt='BOOK ID is 1'+str(id)
        labeln=Label(root,bg='white',bd=5,text=txt,font=('',15))
        labeln.place(x=50,y=450,width=650)
        
    def clear():
        entryb1.delete(0, END)
        entryb2.delete(0, END)
        entryb3.delete(0, END)
        entryb4.delete(0, END)
        entryb5.delete(0, END)       

    
    
    #################
    
    
    button1=Button(root,text='CLEAR',font=('',12),command=clear)
    button1.place(x=250,y=410)
    button2=Button(root,text='SUBMIT',font=('',12),command=inserts)
    button2.place(x=450,y=410)


#Code for alignment check
if __name__=="__main__":
    root=Tk()
    root.geometry("900x500")
    c,conn=None,None
    book_info(root, c, conn)



    
