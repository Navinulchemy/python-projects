import mysql.connector
from tabulate import tabulate
connection=mysql.connector.connect(host="localhost",user="navin",password="95515",database="library")
#if connection:
    #print ("yes");
def insert(BOOKNAME,COST,AUTHOR,RATINGS):
    bridge=connection.cursor()
    sql="insert into books (BOOKNAME,COST,AUTHOR,RATINGS) values (%s,%s,%s,%s)"
    books=(BOOKNAME,COST,AUTHOR,RATINGS)
    bridge.execute(sql,books)
    connection.commit()
    print("inserted successfully")


def update(BOOKNAME, COST, AUTHOR, RATINGS,BOOK_ID):
    bridge = connection.cursor()
    sql = "update books set BOOKNAME=%s,COST=%s,AUTHOR=%s,RATINGS=%s where BOOK_ID=%s"
    books = (BOOKNAME, COST, AUTHOR, RATINGS,BOOK_ID)
    bridge.execute(sql, books)
    connection.commit()
    print("updated successfully")


def display():
 bridge=connection.cursor()
 sql="select * from books"
 bridge.execute(sql)
 result=bridge.fetchall()
 print(tabulate(result,headers=["BOOK_ID","BOOKNAME","COST","AUTHOR","RATINGS"]))

def delete(BOOK_ID):
    bridge = connection.cursor()
    sql = "delete from books where BOOK_ID=%s"
    books =(BOOK_ID)
    bridge.execute(sql, books)
    connection.commit()
    print("deleted successfully")



msg=('''
1.insert
2.update
3.display
4.delete
''')
while True:
    print(msg)
    choice = (int(input("Enter your choice :")))
    if choice==1:
        print("Insertion is in process")
        BOOKNAME=input("enter the book name :")
        COST = input("enter the cost :")
        AUTHOR = input("enter the author :")
        RATINGS = input("enter the ratings :")
        insert(BOOKNAME,COST,AUTHOR,RATINGS)
    elif choice==2:
        print("updation is in process")
        BOOKNAME = input("enter the book name :")
        COST = input("enter the cost :")
        AUTHOR = input("enter the author :")
        RATINGS = input("enter the ratings :")
        BOOK_ID = input("enter the book id :")
        update(BOOKNAME, COST, AUTHOR, RATINGS,BOOK_ID)

    elif choice==3:
        print("display the entire table")
        display()

    elif choice==4:
        print("deletion is in process")
        BOOK_ID = tuple(input("enter the book id :"))
        delete(BOOK_ID)
    else:
        print("entered a wrong choice")
        quit()

