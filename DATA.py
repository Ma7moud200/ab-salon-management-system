import sqlite3

#Main Data Base
db=sqlite3.connect("Data.db")
cur=db.cursor()


#Widgets Data Base
w_db=sqlite3.connect("WDB.db")
wcur=w_db.cursor()


#Main Data Tables
cur.execute('CREATE TABLE IF NOT EXISTS customers(customer_id INTEGER PRIMARY KEY AUTOINCREMENT,user_name TEXT UNIQUE NOT NULL,password TEXT,name TEXT,age INTEGER,phone TEXT,balance REAL,last_visit TEXT)')

cur.execute('CREATE TABLE IF NOT EXISTS employees(employee_id INTEGER PRIMARY KEY AUTOINCREMENT,user_name TEXT UNIQUE NOT NULL,password TEXT,name TEXT,age INTEGER,national_id TEXT,phone TEXT,slary REAL,notes TEXT)')

cur.execute('CREATE TABLE IF NOT EXISTS admin(admin_id INTEGER PRIMARY KEY AUTOINCREMENT,user_name TEXT UNIQUE NOT NULL,password TEXT,admin_password TEXT,name TEXT,age INTEGER,national_id TEXT,phone TEXT,slary REAL,notes TEXT)')

cur.execute('CREATE TABLE IF NOT EXISTS service(service_id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,price REAL,notes TEXT,type TEXT,date TEXT)')

cur.execute('CREATE TABLE IF NOT EXISTS products(product_id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,buy_price REAL,sell_price REAL,sold INTEGER,used INTEGER)')

cur.execute('CREATE TABLE IF NOT EXISTS finance(finance_id INTEGER PRIMARY KEY AUTOINCREMENT,income REAL,expenses REAL,net_profit REAL,expense_kind TEXT)')

cur.execute("CREATE TABLE IF NOT EXISTS temp(id INTEGER PRIMARY KEY AUTOINCREMENT,admin bool)")
cur.execute("CREATE TABLE IF NOT EXISTS bride_book(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,price REAL,paid REAL,rest REAL,phone TEXT,national TEXT,date TEXT,book_date TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS pro_sell(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,price REAL,type TEXT,date TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS pro_buy(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,price REAL,amount INTEGER,date TEXT)")
db.commit()
db.close()

#ًWidget Data Tables

wcur.execute("CREATE TABLE IF NOT EXISTS Hair_Service(h_id INTEGER PRIMARY KEY AUTOINCREMENT,text TEXT,price REAL,deletable bool,type TEXT)")
wcur.execute("CREATE TABLE IF NOT EXISTS Skin_Service(s_id INTEGER PRIMARY KEY AUTOINCREMENT,text TEXT,price REAL,deletable bool,type TEXT)")
wcur.execute("CREATE TABLE IF NOT EXISTS pro_cards(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,price REAL,amount INTEGER,deletable bool,type TEXT)")

w_db.commit()
w_db.close()

