import sqlite3
import os.path
import pandas as pd
def main ():
    
    path = "C:/Users/anush/Desktop/Python 17.1"
    database = path + 'books.db'
    connection = sqlite3.connect(database)
    
    left_aligned_df = pd.style.set_properties(**{'text-align': 'right'})
    print ("------PART 1------")
    print("Authors' last names")
    print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection))
    print ("------PART 2------")
    print("Book titles")
    print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))
    print ("------PART 3------")
    print("INNER JOIN to select all the books")
    print(pd.read_sql("""SELECT auth.id, auth.first, auth.last,  ttl.title, ttl.copyright, ttl.isbn FROM authors AS auth INNER JOIN author_ISBN AS authISBN ON auth.id = authISBN.id INNER JOIN titles AS ttl ON authISBN.isbn = ttl.isbn WHERE first = 'Harvey'""",connection).head())
    print ("------PART 4------")
    print("Insert a new author")
    cursor = connection.cursor()
    cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Robert', 'Jackson')""")
    print(pd.read_sql('SELECT first, last FROM authors', connection))
    print ("------PART 5------")
    print("Insert a new title for an author")
    cursor = connection.cursor()
    cursor = cursor.execute("""INSERT INTO author_ISBN (id,isbn) VALUES ('10','9781305117204')""")
    cursor = cursor.execute("""INSERT INTO titles (isbn,title,edition,copyright) VALUES ('9781305117204','System Analysis and Design','7','2016')""")
    print(pd.read_sql('SELECT * FROM titles',connection))

main()
