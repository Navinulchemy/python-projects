import mysql.connector
from tabulate import tabulate
link=mysql.connector.connect(host="localhost",user="root",passwd="95515",database="sys")
#if link:#to check whether the link is working
#    print("yes")
def add(name,price,color):
    conn=link.cursor()
    sql = "insert into mobiles(name,price,color) values(%s,%s,%s)"
    mobiles=(name,price,color)
    conn.execute(sql,mobiles)
    link.commit()
    print("values added")

def alter(name, price, color,mobid):
    conn = link.cursor()
    sql = "update mobiles set name=%s,price=%s,color=%s where mobid=%s"
    mobiles = (name,price,color,mobid)
    conn.execute(sql, mobiles)
    link.commit()
    print("altered successfully")
def display():
    conn=link.cursor()
    sql="select * from mobiles"
    conn.execute(sql)
    output=conn.fetchall()
    print(tabulate(output,headers=["mobid","name","price","color"]))
def remove(mobid):
    conn=link.cursor()
    sql='delete from mobiles where mobid=%s'
    mobiles=(mobid)
    conn.execute(sql,mobiles)
    link.commit()
    print("erased successfully")
note='''
1.add data
2.alter data
3.display data
4.remove data
'''

while True:
 print(note)
 c=int(input("enter your choice :"))
 if c==1:
  print("adding datas")
  name=input("enter the name :")
  price = input("enter the price :")
  color = input("enter the color :")
  add(name,price,color)
 elif c == 2:
      print('Altering table datas')
      name = input("enter the name :")
      price = input("enter the price :")
      color = input("enter the color :")
      mobid=input("enter the mobile id:")
      alter(name,price,color,mobid)
 elif c==3:
      print("displaying all records")
      display()
 elif c == 4:
    print("removing datas")
    mobid = tuple(input("enter the mobile id :"))
    remove(mobid)