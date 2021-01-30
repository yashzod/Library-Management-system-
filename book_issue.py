from tkinter import*
from datetime import datetime, date, timedelta
import home


def book_issue(root, c, conn):
    
    canvas=Canvas(root,bg='SlateGray2')
    canvas.place(x=0,y=0,width=900,height=500)
    canvas=Canvas(root,bg='white')
    canvas.place(x=25,y=100,width=850,height=300)
    
    txt='ISSUE BOOK'
    label= Label(root,bg='white',bd=5,text=txt,font=('',20))
    label.place(x=110,y=30,width=680)

    ##back button to home page
    button=Button(root,text='BACK',font=('',12),
                  command=lambda: home.home(root, c, conn))
    button.place(x=10,y=10)
    
    txt='BOOK ISSUED'
    labelx=Label(root,bg='white',bd=5,text=txt,font=('',15))
    labelx.place(x=25,y=460,width=850)
    
    #######STUDENT ENTRIES#######

    ##alignment
    x1,y1,x2,y2=25,50,170,85
    entrys1=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys2=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys3=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys4=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys5=Entry(root,bd=5,bg='white',fg='black',font=(50))
    ################
    entrys1.place(x=x1+x2,y=1*y1+y2)
    entrys2.place(x=x1+x2,y=2*y1+y2)
    entrys3.place(x=x1+x2,y=3*y1+y2)
    entrys4.place(x=x1+x2,y=4*y1+y2)
    entrys5.place(x=x1+x2,y=5*y1+y2)
    ##################

    ##alignment
    x1,y1,x2,y2=25,50,10,81
    labels1= Label(root,bg='white',bd=5,text='Student Name',font=('',15))
    labels2= Label(root,bg='white',bd=5,text='Year',font=('',15))
    labels3= Label(root,bg='white',bd=5,text='Division',font=('',15))
    labels4= Label(root,bg='white',bd=5,text='mobile number',font=('',15))
    labels5= Label(root,bg='white',bd=5,text='Student Id',font=('',15))
    ################
    labels1.place(x=x1+x2,y=1*y1+y2)
    labels2.place(x=x1+x2,y=2*y1+y2)
    labels3.place(x=x1+x2,y=3*y1+y2)
    labels4.place(x=x1+x2,y=4*y1+y2)
    labels5.place(x=x1+x2,y=5*y1+y2)
    #######BOOK ENTRIES#######

    ##alignment
    x1,y1,x2,y2=25,50,600,85
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

    ##alignment
    x1,y1,x2,y2=25,50,450,81
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
    ############################################
    ###########################################

    ##entry for barcode reader
    entryx=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryx.place(x=25,y=410)
    entryx.focus()
    labelx=Label(root,bg='white',bd=5,text='',font=('',15))
    labelx.place(x=25,y=460,width=850)

    ##get data of id scanned by barcode reader
    def enter_data():
        txt=''
        labelx=Label(root,bg='white',bd=5,text=txt,font=('',15))
        labelx.place(x=25,y=460,width=850)
        a=entryx.get()
        entryx.delete(0,END)
        if a[0]=="0":
            entrys5.delete(0, END)
            entrys5.insert(0,a[1:])
            s5=entrys5.get()
            for i in c.execute('''SELECT * FROM student_info WHERE id=?''',(s5,)):
                entrys1.delete(0,END)
                entrys2.delete(0,END)
                entrys3.delete(0,END)
                entrys4.delete(0,END)
                entrys5.delete(0,END)
                entrys1.insert(0,i[1])
                entrys2.insert(0,i[2])
                entrys3.insert(0,i[3])
                entrys4.insert(0,i[4])
                entrys5.insert(0,'0'+s5)
        elif a[0]=='1':
            entryb5.delete(0, END)
            entryb5.insert(0,a[1:])
            b5=entryb5.get()
            for i in c.execute('''SELECT * FROM book_info WHERE id=?''',(b5,)):
                entryb1.delete(0,END)
                entryb2.delete(0,END)
                entryb3.delete(0,END)
                entryb4.delete(0,END)
                entryb5.delete(0,END)
                entryb1.insert(0,i[1])
                entryb2.insert(0,i[2])
                entryb3.insert(0,i[3])
                entryb4.insert(0,i[4])
                entryb5.insert(0,'1'+b5)
        else:
            txt='Please Enter Valid ID'
            labelx=Label(root,bg='white',bd=5,text=txt,font=('',15))
            labelx.place(x=25,y=460,width=850)
        
    entryx.bind('<Return>',(lambda event:enter_data()))

    
    def submit():

        book_id=entryb5.get()[1:]
        student_id=entrys5.get()[1:]
        issue_date=str(date.today())
        return_date=str(date.today()+timedelta(days=7))
        for i in c.execute('''SELECT * FROM book_info WHERE id=?''',(book_id,)):
            if i[5]==True:   
                status='issued'
                c.execute('''INSERT INTO issue(book_id,student_id,issue_date,return_date,status)
                                    VALUES(?,?,?,?,?)''',(book_id,student_id,issue_date,return_date,status))
                for i in c.execute('''SELECT * FROM issue'''):
                    print(i)
                c.execute('''UPDATE book_info SET availablity=False WHERE id=?''',(book_id,))
                txt='BOOK ISSUED'
                labelx=Label(root,bg='white',bd=5,text=txt,font=('',15))
                labelx.place(x=25,y=460,width=850)
            else:
                txt='BOOK NOT AVAILABLE'
                labelx=Label(root,bg='white',bd=5,text=txt,font=('',15))
                labelx.place(x=25,y=460,width=850)
                
    
    buttons=Button(root,text='SUBMIT',font=('',12),command=submit)
    buttons.place(x=700,y=410)



##Driver code to check alignment
if __name__=="__main__":
    root=Tk()
    root.geometry("900x500")
    c,conn=None,None
    book_issue(root, c, conn)

