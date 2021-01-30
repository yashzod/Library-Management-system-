import sqlite3

def execute_database(c, conn):
    ##create table if not present else pass
    try:
        c.execute('''CREATE TABLE student_info(id,
                                            name,
                                            year,
                                            division,
                                            mo_no)''')
        c.execute('''CREATE TABLE book_info(id,
                                            title,
                                            author,
                                            publication,
                                            department,
                                            availablity)''')
        c.execute('''CREATE TABLE issue(book_id,
                                        student_id,
                                        issue_date,
                                        return_date,
                                        status
                                        )''')
        c.execute('''CREATE TABLE record(student,book,n)''')
        c.execute('''INSERT INTO record VALUES('1','1',1)''')
        conn.commit()
    except sqlite3.OperationalError:
        pass
