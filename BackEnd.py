#Agora esqueço momentaneamente o frontend, simplesmente faço print para testar o backend

import sqlite3

def connect():
    conn=sqlite3.connect("DesktopDatabaseApp/books.db")
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insertdata(title, author, year, isnb): #Aqui são as quatro caixas do frontend
    conn=sqlite3.connect("DesktopDatabaseApp/books.db")
    cur= conn.cursor()                    #NULL cria o id automaticamente !  
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isnb))
    conn.commit()
    conn.close()

def viewdata():
    conn=sqlite3.connect("DesktopDatabaseApp/books.db")
    cur= conn.cursor()                    
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()    
    conn.close()
    return rows

def searchdata(title="", author="", year="", isbn=""): #Para que possa ter parametros sem valores, caso só procure por exemplo por author!
    conn=sqlite3.connect("DesktopDatabaseApp/books.db")
    cur= conn.cursor()                    
    cur.execute("SELECT * FROM book WHERE title=? or author=? or year=? or isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()    
    conn.close() 
    return rows

def deletedata(id): #Aqui uso o id, porque assim simplesmente seleciono a data diretamente da listbox
    conn=sqlite3.connect("DesktopDatabaseApp/books.db")
    cur= conn.cursor()                   
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def updatedata(id, title, author, year, isbn):
    conn=sqlite3.connect("DesktopDatabaseApp/books.db")
    cur= conn.cursor()                      
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author,year, isbn, id)) #Isto fica por ordem de chamada do cur.execute, primeiro chamei o title e depois o id
    conn.commit()
    conn.close()





connect()  #Aqui chamo o connect para ter a certeza que esta função é sempre executada quando abro a app.
#insertdata("book of books", "The author", 2020, 4142352871531)
#deletedata(3)
#updatedata(4, "The moon", "John Smith", 1944, 786214568715)
#print(viewdata())
#print(searchdata(author="The author"))
