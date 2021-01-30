from tkinter import*
import student_info
import book_info
import book_issue
import book_return


def home(root, c, conn):
    ##background canvas
    canvas=Canvas(root,bg='SlateGray2')
    canvas.place(x=0,y=0,width=900,height=500)
    
    canvas=Canvas(root,bg='white')
    canvas.place(x=200,y=100,width=500,height=300)


    txt='LIBRARY MANAGEMENT SYSTEM'
    label= Label(root,bg='white',bd=5,text=txt,font=('',30))
    label.place(x=110,y=30,width=680)

    ##button: new student information.
    button1=Button(root,text='NEW STUDENT INFORMATION',font=('',12),
                   command= lambda: student_info.student_info(root, c, conn))
    button1.place(x=300,y=140,width=300)

    ##button: new book information.
    button2=Button(root,text='NEW BOOK INFORMATION',font=('',12),
                   command= lambda: book_info.book_info(root, c, conn))
    button2.place(x=300,y=200,width=300)

    ##button: book issue.
    button3=Button(root,text='ISSUE BOOK',font=('',12),
                   command= lambda: book_issue.book_issue(root, c, conn))
    button3.place(x=300,y=260,width=300)

    ##button: book return.
    button4=Button(root,text='RETURN BOOK',font=('',12),
                   command= lambda: book_return.book_return(root, c, conn))
    button4.place(x=300,y=320,width=300)
