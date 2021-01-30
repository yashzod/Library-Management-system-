import sqlite3
from tkinter import*
import execute_database
import home

##connect to sqlite3 database file: "lms.db"
##create database file: "lms.db", if "lms.db" not in folder
conn=sqlite3.connect('lms.db')
c=conn.cursor()

##create tables in database
execute_database.execute_database(c, conn)    

##create tkinter window
root=Tk()

##window size: width=900px, height=500px
root.geometry("900x500")

##window title
root.title("Library Management System")

##home page program
home.home(root, c, conn)

conn.commit()
root.mainloop()
