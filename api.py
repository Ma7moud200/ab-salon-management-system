from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import os
import uvicorn
import bcrypt
import datetime
salt=bcrypt.gensalt()
app=FastAPI()
def is_number(s:str):
    try:
        float(s)
        return True
    except:
        return False

def get_db():
    db=sqlite3.connect("Data.db")
    return db,db.cursor()
def get_db2():
    db=sqlite3.connect("WDB.db")
    return db,db.cursor()

class users(BaseModel):
    Name:str
    User_Name:str
    Age:int
    Phone:str
    Role:str
class LoginModel(BaseModel):
    user_name:str
    password:str
    role:str
    admin_password:str | None=None
class products(BaseModel):
    product_name:str
    product_amount:int
    product_price:float
    product_sold:int
    product_buy_price:float
    product_id:int
class services(BaseModel):
    service_name:str
    service_kind:str
    service_price:float
class services_bride(BaseModel):
    id:int
    service_name:str
    service_kind:str
    service_price:float
class SignUpModel(BaseModel):
    name:str
    user_name:str
    password:str
    age:int
    phone:str
    national_id:str | None = None
    admin_password:str | None = None
    role:str
class hair_services_butoons(BaseModel):
    text:str
    price:float
    service_id:int
class skin_services_butoons(BaseModel):
    
    text:str
    price:float
    service_id:int

class bride_book(BaseModel):
    name:str
    price:float
    paid:float
    phone:str
    national:str
    date:str
class BookingUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    paid: float | None = None
    phone: str | None = None
    national: str | None = None
    date: str | None = None
class DeleteByFlag(BaseModel):
    boole: bool

class new_product(BaseModel):
    name:str
    price:float
    amount:int
    kind:str
class RemoveProduct(BaseModel):
    id: int
    boole: bool    
class update_product(BaseModel):
    id:int
    name:str | None=None
    price:float |None=None
    amount:int |None=None
class sell(BaseModel):
    id:int
class buy(BaseModel):
    id:int
    amount:int

@app.post("/login")
async def login(data: LoginModel):
    user_name = data.user_name      # أو data.user_name لو الاسم كده في الموديل
    password = data.password
    admin_password = data.admin_password
    role = data.role

    password_bytes = password.encode('utf-8')

    db, cr = get_db()

    try:
        if role == "Customer":
            cr.execute(
                "SELECT password,customer_id FROM customers WHERE user_name=?",
                (user_name,)
            )
            row = cr.fetchone()

            if row is None:
                return {"Status": "Error", "msg": "User Not Found"}

            stored_hash = row[0]
            customer_id=row[1]
            if isinstance(stored_hash, str):
                stored_hash = stored_hash.encode('utf-8')

            if bcrypt.checkpw(password_bytes, stored_hash):
                return {"Status": "Ok", "msg": "Login Successful","customer_id":customer_id}
            else:
                return {"Status": "error", "msg": "Wrong Password"}

        elif role == "Employee":
            cr.execute(
                "SELECT password,employee_id FROM employees WHERE user_name=?",
                (user_name,)
            )
            row = cr.fetchone()

            if row is None:
                return {"Status": "Error", "msg": "User Not Found"}

            stored_hash = row[0]
            employee_id=row[1]
            if isinstance(stored_hash, str):
                stored_hash = stored_hash.encode('utf-8')

            if bcrypt.checkpw(password_bytes, stored_hash):
                return {"Status": "Ok", "msg": "Login Successful","employee_id":employee_id}
            else:
                return {"Status": "error", "msg": "Wrong Password"}

        elif role == "Admin":
            admin_bytes = admin_password.encode('utf-8')

            cr.execute(
                "SELECT password, admin_password,admin_id FROM admin WHERE user_name=?",
                (user_name,)
            )
            row = cr.fetchone()

            if row is None:
                return {"Status": "Error", "msg": "User Not Found"}

            stored_hash = row[0]
            admin_stored = row[1]
            admin_id=row[2]

            if isinstance(stored_hash, str):
                stored_hash = stored_hash.encode('utf-8')
            if isinstance(admin_stored, str):
                admin_stored = admin_stored.encode('utf-8')

            if bcrypt.checkpw(password_bytes, stored_hash) and bcrypt.checkpw(admin_bytes, admin_stored):
                cr.execute("INSERT INTO temp (admin) VALUES (?)", (1,))
                db.commit()
                return {"Status": "Ok", "msg": "Login Successful","admin_id":admin_id}
            else:
                return {"Status": "error", "msg": "Wrong Password"}

        else:
            return {"Status": "error", "msg": "Invalid role"}

    finally:
        db.close()

        
    
   
   

@app.post("/signup")
async def SignUp(data: SignUpModel):
    user_name=data.user_name
    password=data.password.encode()
    age=data.age
    name=data.name
    phone=data.phone
    national_id=data.national_id
    role=data.role
    hashed=bcrypt.hashpw(password,salt)
    
    db,cr=get_db()
    try:
        if role=="Customer":
            cr.execute("SELECT user_name FROM customers WHERE user_name = ?", (data.user_name,))
            exists = cr.fetchone()

            if exists is not None:
                db.close()
                return {"Status": "Error: username exixts", "msg": "Username already exists"}
            else:
                get_db()
                cr.execute("INSERT INTO customers(user_name,password,name,age,phone) VALUES(?,?,?,?,?)",(user_name,hashed,name,age,phone))
                db.commit()
                db.close()
                return{"Status":"Ok","msg":"You SignedUp as Customer"}
            
            
        if role=="Employee":
            cr.execute("SELECT user_name FROM employees WHERE user_name = ?", (data.user_name,))
            exists = cr.fetchone()

            if exists is not None:
                db.close()
                return {"Status": "Error: username exixts", "msg": "Username already exists"}
            else:
                get_db()
                cr.execute("INSERT INTO employees(user_name,password,name,age,phone,national_id) VALUES(?,?,?,?,?,?)",(user_name,hashed,name,age,phone,national_id))
                db.commit()
                db.close()
                return{"Status":"Ok","msg":"Welcom To Our Community"}
            
            
        if role=="Admin":
            admin_password=data.admin_password.encode()
            hashed_admin=bcrypt.hashpw(admin_password,salt)
            cr.execute("SELECT user_name FROM admin WHERE user_name = ?", (data.user_name,))
            exists = cr.fetchone()

            if exists is not None:
                db.close()
                return {"Status": "Error: username exixts", "msg": "Username already exists"}
            else:
                get_db()
                cr.execute("INSERT INTO admin(user_name,password,name,age,phone,national_id,admin_password) VALUES(?,?,?,?,?,?,?)",(user_name,hashed,name,age,phone,national_id,hashed_admin))
                db.commit()
                db.close()
                return{"Status":"Ok","msg":"Welcom To Our Community"}
    except Exception as e:
        return{"Status":"Error","msg":"Field To SignUp","desc":str(e)}
    
    
@app.get("/services/hair")
async def HairButton():
    db, cr = get_db2()
    
    cr.execute("SELECT * FROM Hair_Service")
    rows = cr.fetchall()
    
    if rows:
        buttons = []
        for row in rows:
            button_informations = {
                "service_id": row[0],
                "text": row[1],
                "price": row[2]
            }
            buttons.append(button_informations)
        
        db.close()
        return {"status": "ok", "buttons": buttons}
    
    else:
        db.close()
        return {"status": "error", "msg": "No Buttons"}
    
@app.get("/services/skin")
async def HairButton():
    db, cr = get_db2()
    
    cr.execute("SELECT * FROM Skin_Service")
    rows = cr.fetchall()
    
    if rows:
        buttons = []
        for row in rows:
            button_informations = {
                "service_id": row[0],
                "text": row[1],
                "price": row[2]
            }
            buttons.append(button_informations)
        
        db.close()
        return {"status": "ok", "buttons": buttons}
    
    else:
        db.close()
        return {"status": "error", "msg": "No Buttons"}


@app.post("/services/data")
async def services_data(data:services):
    service_name=data.service_name
    service_kind=data.service_kind
    service_price=data.service_price
    
    try:
        db,cr=get_db()
        cr.execute("INSERT INTO service(name,price,type,date) VALUES(?,?,?,?)",(
            service_name,
            service_price,
            service_kind,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))
        db.commit()
        return {"status":"ok","msg":"Order Added"}
    except:
        return{"status":"error","msg":"There Is Something Wrong"}
    
@app.post("/services/bride")
async def services_data(data:services_bride):
    id=data.id
    service_name=data.service_name
    service_kind=data.service_kind
    service_price=data.service_price
    
    try:
        db,cr=get_db()
        cr.execute("DELETE FROM bride_book WHERE id=?",(id,))
        cr.execute("INSERT INTO service(name,price,type,date) VALUES(?,?,?,?)",(
            service_name,
            service_price,
            service_kind,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))
        db.commit()
        return {"status":"ok","msg":"Order Added"}
    except Exception as e:
        print(str(e))
        return{"status":"error","msg":"There Is Something Wrong"}
    
    

@app.post("/bride/book")
async def bride_book(data:bride_book):
    
    name=data.name
    price=data.price
    phone=data.phone
    national=data.national
    date=data.date
    paid=data.paid
    db,cr=get_db()
    try:
        cr.execute("INSERT INTO bride_book(name,price,paid,rest,phone,national,date,book_date)VALUES(?,?,?,?,?,?,?,?)",(name,price,paid,price-paid,phone,national,date,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        db.commit()
        return{"status":"ok","msg":"Booked"}
    except Exception as e:
        return{"status":"error","msg":str(e)}
        
@app.get("/books/data")
async def get_books_data():
    db,cr=get_db()
    cr.execute("SELECT * FROM bride_book ORDER BY date")
    rows=cr.fetchall()
    result=[]
    for r in rows:
        date=datetime.datetime.fromisoformat(r[7]).strftime("%I:%M %p %d-%m-%Y")
        book_date=datetime.datetime.fromisoformat(r[8]).strftime("%I:%M %p %d-%m-%Y")
        result.append({"id":r[0],
                      "name":r[1],
                      "price":r[2],
                      "paid":r[3],
                      "rest":r[4],
                      "phone":r[5],
                      "national":r[6],
                      "date":date,
                      "book_date":book_date
                      
                      })
    return result
@app.delete("/books/delete/{booking_id}")
async def delete(booking_id:int):
    db,cr=get_db()
    cr.execute("DELETE FROM bride_book WHERE id=?",(booking_id,))
    db.commit()
    db.close()
    return{"status":"ok"}

@app.patch("/books/update/{booking_id}")
def update_booking(booking_id: int, data: BookingUpdate):
    # بنجيب بس الحقول اللي اتبعتت فعلاً
    fields = data.model_dump(exclude_unset=True)

    if not fields:
        return {"status": "no_data", "msg": "No fields to update"}

    # بنبني جملة الـ SQL ديناميكياً
    set_clause = ", ".join(f"{col} = ?" for col in fields.keys())
    values = list(fields.values())
    values.append(booking_id)

    conn = sqlite3.connect("Data.db")
    cr = conn.cursor()
    cr.execute(f"UPDATE bride_book SET {set_clause} WHERE id = ?", values)
    cr.execute("SELECT price,paid FROM bride_book WHERE id=?", (booking_id,))
    row=cr.fetchone()
    cr.execute("UPDATE bride_book SET rest=? WHERE id=?",(row[0]-row[1],booking_id))
    conn.commit()
    conn.close()

    return {"status": "ok"}

@app.get("/products/cards/{kind}")
async def pro_cards(kind:str):
    cards=[]
    db,cr=get_db2()
    cr.execute("SELECT * From pro_cards WHERE type=?",(kind,))
    r=cr.fetchall()
    if r is not None:
        for row in r:
            card={"id":row[0],
                  "name":row[1],
                  "price":row[2],
                  "amount":row[3]
            }
            cards.append(card)
    return cards
                  
                  
                  
@app.post("/products/add")
async def add_product(data:new_product):
    name=data.name
    price=data.price
    amount=data.amount
    kind=data.kind
    try:
        db,cr=get_db2()
        cr.execute("INSERT INTO pro_cards(name,price,amount,type)VALUES(?,?,?,?)",(name,price,amount,kind))
        db.commit()
        return{"status":"ok"}
    except:
        return{"status":"Error"}
    
@app.post("/products/update")
async def update_pro(data: update_product):
    db, cr = get_db2()

    try:
        # name
        if data.name is not None and data.name != "":
            cr.execute("UPDATE pro_cards SET name=? WHERE id=?", (data.name, data.id))

        # price
        if data.price is not None:
            cr.execute("UPDATE pro_cards SET price=? WHERE id=?", (data.price, data.id))

        # amount
        if data.amount is not None:
            cr.execute("UPDATE pro_cards SET amount=? WHERE id=?", (data.amount, data.id))

        db.commit()
        return {"status": "ok"}
    except Exception as e:
        db.rollback()
        return {"status": "error", "detail": str(e)}
    finally:
        db.close()


@app.post("/product/remove")
async def remove(data: RemoveProduct):
    db, cr = get_db2()
    id = data.id
    boole = data.boole

    try:
        if boole:
            cr.execute("UPDATE pro_cards SET deletable=? WHERE id=?", (1, id))
        else:
            cr.execute("UPDATE pro_cards SET deletable=? WHERE id=?", (0, id))

        db.commit()
        return {"status": "ok"}
    except:
        return {"status": "Error"}


@app.post("/products/delete")
async def delete(data: DeleteByFlag):
    boole = data.boole
    if boole:
        db, cr = get_db2()
        try:
            cr.execute("DELETE FROM pro_cards WHERE deletable=?", (1,))  # 👈 متنساش FROM
            db.commit()
            return {"status": "ok"}
        except Exception as e:
            db.rollback()
            return {"status": "Error", "detail": str(e)}
        finally:
            db.close()
    else:
        return {"status": "no_action"}
    
@app.post("/products/sell")
async def pro_sell(data:sell):
    id=data.id
    db,cr=get_db()
    db2,cr2=get_db2()
    try:
        cr2.execute("SELECT name,price,type,amount FROM pro_cards WHERE id=?",(id,))
        r=cr2.fetchone()
        if r is not None:
            name=r[0]
            price=r[1]
            kind=r[2]
            amount=r[3]
            date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if amount>0:
                cr.execute("INSERT INTO pro_sell (name,price,type,date)VALUES(?,?,?,?)",(name,price,kind,date))
                db.commit()
                cr2.execute("UPDATE pro_cards SET amount=? WHERE id=?",(amount-1,id))
                db2.commit()
                return{"status":"ok"}
            else:
                return{"status":"no","msg":"No product In Stock"}
    except Exception as e:
        print(str(e))
        return{"status":"error"}
    
    finally:
        db.close()
        db2.close()

@app.post("/products/use")   
async def pro_use(data:sell):
    try:
        id=data.id
        db,cr=get_db2()
        cr.execute("SELECT amount FROM pro_cards WHERE id=?",(id,))
        r=cr.fetchone()
        if r is not None:
            if r[0]>0:
                cr.execute("UPDATE pro_cards SET amount=? WHERE id=?",(r[0]-1,id))
                db.commit()
                return{"status":"ok"}
            else:
                return{"status":"no"}
    except Exception as e:
        print(str(e))
        return{"status":"error"}
            

@app.get("/products/cards/all/1")
async def pro_cards():
    cards=[]
    db,cr=get_db2()
    cr.execute("SELECT * From pro_cards")
    r=cr.fetchall()
    if r is not None:
        for row in r:
            card={"id":row[0],
                  "name":row[1],
                  "price":row[2],
                  "amount":row[3]
            }
            cards.append(card)
    return cards
@app.post("/products/update/buy")
async def buy(data:buy):
    db,cr=get_db()
    db2,cr2=get_db2()
    try:
        id=data.id
        amount=data.amount
        date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cr2.execute("SELECT name,amount,price FROM pro_cards WHERE id=?",(id,))
        r=cr2.fetchone()
        price=r[2]*amount
        cr.execute("INSERT INTO pro_buy (name,price,amount,date) VALUES(?,?,?,?)",(r[0],price,amount,date))
        cr2.execute("UPDATE pro_cards SET amount=? WHERE id=?",(r[1]+amount,id))
        db.commit()
        db2.commit()
        return{"status":"ok"}
    except Exception as e:
        return{"status":"error","msg":f"{str(e)}"}
    finally:
        db.close()
        db2.close()
        
        





 
if __name__=="__main__":
    import uvicorn
    uvicorn.run("api:app",host="0.0.0.0",port=8000,reload=True)