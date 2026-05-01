from PySide6.QtWidgets import (QApplication,QWidget,QCheckBox,QHBoxLayout,QVBoxLayout,QLineEdit,QMainWindow,QLabel,QPushButton,QAbstractItemView,QHeaderView,
                               QFormLayout,QMessageBox,QComboBox,QGraphicsDropShadowEffect,QTabWidget,QTabBar,QFrame,QTextBrowser,QGridLayout,QDateEdit,QMdiSubWindow,QDataWidgetMapper,QCalendarWidget,QDateTimeEdit,QTableWidgetItem,QTableWidget)
from PySide6 import QtWidgets
from PySide6.QtCore import Qt,QSize,QMargins,QDate,QDateTime,QTime
from PySide6.QtGui import QColor,QKeyEvent
import sys
from Custom_Edits1 import (Button,editline,passline,radius_Button,servic_form,servic_form2,Product_lay,Product_card,Product_lay2)
import sqlite3
import requests
import time
api="http://127.0.0.1:8000"
def is_number(s:str):
    try:
        float(s)
        return True
    except:
        return False

db= sqlite3.connect("Data.db")
cr=db.cursor()
wd=sqlite3.connect("WDB.db")
wr=wd.cursor()
employee_id=None
customer_id=None
admin_id=None
cr.execute("DELETE FROM temp")
db.commit()
def com():
    db.commit()



class Login_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:white")
        self.setFixedSize(800,600)
        widget=QWidget(self)
        self.setCentralWidget(widget)
        
        
        
        Vlay=QtWidgets.QVBoxLayout()
        widget.setLayout(Vlay)
        
        lable1=QLabel("AB|System")
        lable2=QLabel("Choose Your Role")
        
        form=QFormLayout()
        Hlay=QHBoxLayout()
        
        
        combo= QComboBox()
        combo.addItems(["Customer","Employee","Admin"])
        
        
        user_input=editline(500)
        user_input.setPlaceholderText("UserName")
    
        
        bt1=Button("Login")
        bt2=Button("Create Account")
        
        
            
        
        
        pass_input=passline(500)
        pass_input.setPlaceholderText("Password")
        pass_input.setMaximumWidth(500)
        
        
        admin_input=passline(500)
        admin_input.setPlaceholderText("Admin Password")  
        

        
        
        
              
        Vlay.addWidget(lable1,alignment=Qt.AlignmentFlag.AlignHCenter)
        Vlay.addWidget(user_input,alignment=Qt.AlignmentFlag.AlignHCenter)
        Vlay.addWidget(pass_input,alignment=Qt.AlignmentFlag.AlignHCenter)
        Vlay.addWidget(admin_input,alignment=Qt.AlignmentFlag.AlignHCenter)
        Vlay.addLayout(Hlay)
        Vlay.addWidget(lable2,alignment=Qt.AlignmentFlag.AlignHCenter)
        Vlay.addWidget(combo,alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.setWindowTitle("AB|SYS")
        
        
        
        Hlay.addWidget(bt1,alignment=Qt.AlignmentFlag.AlignHCenter)
        Hlay.addWidget(bt2,alignment=Qt.AlignmentFlag.AlignHCenter)
        
       
        combo.setStyleSheet("QComboBox{background-color:white;border-radius:12px;border:2px solid black;color:black;;min-width:175;min-height:20;margin:10px}QComboBox:hover{background-color:lightgray;border-color:blue}")
        combo.setCursor(Qt.CursorShape.PointingHandCursor)
        
        
        lable1.setStyleSheet("font-size:40px;font-weight:bold;color:red;max-height:40")
        lable2.setStyleSheet("font-size:25px;max-height:30")
        admin_input.hide()
            
        def admin_show():    
            text=combo.currentText()
            if text =='Admin':
                admin_input.show()
            else:
                admin_input.hide()
            
        def Create_account_page(self):
            user_input.clear()
            pass_input.clear()
            admin_input.clear()
            l_window.hide()
            s_window.show()
        
        def login_page(self):
            text=combo.currentText()
            username,password,admin_password=user_input.text(),pass_input.text(),admin_input.text()
            lgoin_url="http://127.0.0.1:8000/login"
            msg=QMessageBox()
            if text=="Employee":
                if username==""or password=="":
                    msg.setText("⚠ Please Enter User Name And Passowrd")
                    msg.exec()
                else:
                    try:
                        data={"user_name":username,
                              "password":password,
                              "role":text
                        }
                        r=requests.post(lgoin_url,json=data)
                        res=r.json()
                        if res["msg"]=="User Not Found":
                            msg.setText("❌Wrong User Name")
                            msg.exec()
                        elif res["msg"]=="Wrong Password":
                            msg.setText("❌Wrong Password")
                            msg.exec()
                        elif res["Status"]=="Ok":
                            global employee_id
                            employee_id=res["employee_id"]
                            l_window.hide()
                            user_input.clear()
                            pass_input.clear()
                            admin_input.clear()
                            m_window.showMaximized()
                            
                        
                    except Exception as e:
                        msg.setText(f"❌ There is proplem with server\n  ({str(e)})")
                        msg.exec()

                        
            
            elif text=="Customer":
                msg=QMessageBox()
                if username==""or password=="":
                    msg.setText("⚠ Please Enter User Name And Passowrd")
                    msg.exec()
                else:
                    try:
                        data={"user_name":username,
                              "password":password,
                              "role":text
                        }
                        r=requests.post(lgoin_url,json=data)
                        res=r.json()
                        if res["msg"]=="User Not Found":
                            msg.setText("❌Wrong User Name")
                            msg.exec()
                        elif res["msg"]=="Wrong Password":
                            msg.setText("❌Wrong Password")
                            msg.exec()
                        elif res["Status"]=="Ok":
                            global customer_id
                            customer_id=res["customer_id"]
                            l_window.hide()
                            user_input.clear()
                            pass_input.clear()
                            admin_input.clear()
                            m_window.showMaximized()
                            
                        
                    except Exception as e:
                        msg.setText(f"❌ There is proplem with server\n  ({str(e)})")
                        msg.exec()
            
            
            elif text=="Admin":
                msg=QMessageBox()
                if username==""or password=="" or admin_password=="":
                    msg.setText("⚠ Please Enter User Name And Passowrd")
                    msg.exec()
                else:
                    try:
                        data={"user_name":username,
                              "password":password,
                              "admin_password":admin_password,
                              "role":text
                        }
                        r=requests.post(lgoin_url,json=data)
                        res=r.json()
                        if res["msg"]=="User Not Found":
                            msg.setText("❌Wrong User Name")
                            msg.exec()
                        elif res["msg"]=="Wrong Password":
                            msg.setText("❌ Wrong Password")
                            msg.exec()
                        elif res["Status"]=="Ok":
                            global admin_id
                            admin_id=res["admin_id"]
                            l_window.hide()
                            user_input.clear()
                            pass_input.clear()
                            admin_input.clear()
                            m_window.showMaximized()
                            
                            
                        
                    except Exception as e:
                        msg.setText(f"❌ There is proplem with server\n  ({str(e)})")
                        msg.exec()
                        
            
        combo.currentTextChanged.connect(admin_show)
        bt2.clicked.connect(Create_account_page)
        bt1.clicked.connect(login_page)
        
        
        
#Signup Window------------------------------------------------------------------------------------------------------------------------------------------


class Signup_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:white")
        self.resize(800,600)
        widget=QWidget(self)
        self.setCentralWidget(widget)
        Vlay=QtWidgets.QVBoxLayout()
        widget.setLayout(Vlay)
        lable1=QLabel("AB|System")
        lable2=QLabel("Choose Your Role")
        form=QFormLayout()
        Hlay=QHBoxLayout()
        Hlay2=QHBoxLayout()
        
        
        combo= QComboBox()
        combo.addItems(["Customer","Employee","Admin"])
        combo.setStyleSheet("")
        
        
        user_input=editline(500)
        user_input.setPlaceholderText("UserName")
        
        
        name=editline(200)
        name.setPlaceholderText("Enter Name")
        
        
        age=editline(200)
        age.setPlaceholderText("Enter Age")
        
        
        Phone=editline(200)
        Phone.setPlaceholderText("Enter Phone Number")
        
        
        national_id=editline(200)
        national_id.setPlaceholderText("Enter Nationaal ID")
        
        Hlay2.addWidget(name)
        Hlay2.addWidget(age)
        Hlay2.addWidget(Phone)
        Hlay2.addWidget(national_id)
        
        
        national_id.hide()
        
        
        
        
        pass_input=passline()
        pass_input.setPlaceholderText("Password")
        
        
        admin_input=passline()
        admin_input.setPlaceholderText("Admin Password") 
        
               
        Vlay.addWidget(lable1,alignment=Qt.AlignmentFlag.AlignHCenter)
        Vlay.addWidget(user_input,alignment=Qt.AlignmentFlag.AlignHCenter)
        Vlay.addWidget(pass_input,alignment=Qt.AlignmentFlag.AlignHCenter)
        Vlay.addWidget(admin_input,alignment=Qt.AlignmentFlag.AlignHCenter)
        Vlay.addLayout(Hlay2)
        Vlay.addLayout(Hlay)
        Vlay.addWidget(lable2,alignment=Qt.AlignmentFlag.AlignHCenter)
        Vlay.addWidget(combo,alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.setWindowTitle("AB|SYS")
        
        bt1=Button("Login")
        bt2=Button("Signup")
        
        Hlay.addWidget(bt1,alignment=Qt.AlignmentFlag.AlignHCenter)
        Hlay.addWidget(bt2,alignment=Qt.AlignmentFlag.AlignHCenter)
        
        
        combo.setStyleSheet("background-color:white;border-radius:11px;color:black;border:2px solid black;min-width:175;min-height:20;margin:10px")
        
        lable1.setStyleSheet("font-size:40px;font-weight:bold;color:red;max-height:40")
        lable2.setStyleSheet("font-size:25px;max-height:30")
        

        
        admin_input.hide()
        def admin_show():    
            text=combo.currentText()
            
            if text =='Admin':
                admin_input.show()
                national_id.show()
            elif text=="Employee":
                admin_input.hide()
                national_id.show()
            else:
                admin_input.hide()
                national_id.hide()
            
        combo.currentTextChanged.connect(admin_show)
        def sign_up_button():
            msg = QMessageBox()
            role = combo.currentText()
            sign_url = "http://127.0.0.1:8000/signup"

            # ناخد القيم مرة واحدة
            username    = user_input.text().strip()
            password    = pass_input.text().strip()
            full_name   = name.text().strip()
            age_text    = age.text().strip()
            phone_text  = Phone.text().strip()
            national_id_text = national_id.text().strip()
            admin_pass  = admin_input.text().strip()

            # 1) تحقق أساسي
            if len(username) < 3 or len(password) < 8:
                msg.setText("Min length for username is 3\nand password is 8 characters")
                msg.exec()
                return

            # 2) تحقق من الحقول الفاضية حسب الـ role
            if not full_name or not age_text or not phone_text:
                msg.setText("Warning⚠\nYou need to fill all fields")
                msg.exec()
                return

            if role in ("Employee", "Admin") and not national_id_text:
                msg.setText("Warning⚠\nNational ID is required")
                msg.exec()
                return

            if role == "Admin" and len(admin_pass) < 8:
                msg.setText("Warning⚠\nAdmin password must be at least 8 characters")
                msg.exec()
                return

            # 3) تأكد إن الأرقام فعلاً أرقام
            if not age_text.isdigit() or not phone_text.isdigit() or (
                role in ("Employee", "Admin") and not national_id_text.isdigit()
            ):
                msg.setText("Warning⚠\nPhone, National ID and Age must be digits")
                msg.exec()
                return

            # 4) نبني الـ JSON اللي هنبعته للـ API
            data = {
                "user_name": username,
                "password": password,
                "name": full_name,
                "age": int(age_text),
                "phone": phone_text,
                "role": role
            }

            if role in ("Employee", "Admin"):
                data["national_id"] = national_id_text

            if role == "Admin":
                data["admin_password"] = admin_pass

            # 5) نبعت الريكوست
            try:
                r = requests.post(sign_url, json=data)
                res = r.json()
            except Exception as e:
                msg.setText(f"Error❌\n{e}")
                msg.exec()
                return

            # 6) نتعامل مع الرد
            if res["Status"] == "Ok":
                msg.setText("Signed Up Successfully✅")
            elif res["Status"]=="Error: username exixts":
                msg.setText("❌ User Name Already Exist")
            else:
                msg.setText("There Is Something Wrong❌")
            msg.exec()

                    
            
            
                
                
                   
                
                
                    
        def back_to_login(self):
            user_input.clear()
            pass_input.clear()
            admin_input.clear()
            name.clear()
            age.clear()
            Phone.clear()
            national_id.clear()
            s_window.close()
            l_window.show()
        bt1.clicked.connect(back_to_login)
        bt2.clicked.connect(sign_up_button)
        
class main_widow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        main_tabs=QTabWidget()
        
        servic_tabs=QTabWidget()
        servic_tab=QWidget()
        
        self.setCentralWidget(main_tabs)
        self.setWindowTitle("AB|Main")
        
        servic_lay=QVBoxLayout()
        servic_tab.setLayout(servic_lay)
        main_tabs.addTab(servic_tab,"Services💈")
        
            
            
        
        
        # Tabs
        b1=Button("Remove",hight=20,width=100,bg_color="red",hovercolor="darkred",border="black",hover_border="black",text_color="white")
        
        b2=Button("+ Add",hight=20,width=100,bg_color="lime",hovercolor="green",border="black",hover_border="black",text_color="white")
        temp_lay=QHBoxLayout()
        temp_lay.addWidget(QLabel(""))
        hlay2=QHBoxLayout()
        hlay2.addStretch(1)
        hlay2.addWidget(b2,alignment=Qt.AlignmentFlag.AlignRight)
        hlay2.addLayout(temp_lay)
        hlay2.addWidget(b1,alignment=Qt.AlignmentFlag.AlignRight)
        servic_lay.addLayout(hlay2)
        servic_tab2=QTabWidget()
        servic_lay.addWidget(servic_tab2)
        tab1=QWidget()
        tab2=QWidget()
        tab3=QWidget()
        servic_tab2.addTab(tab1,"Hair Services 👩")
        servic_tab2.addTab(tab2,"Skin Services 💅")
        servic_tab2.addTab(tab3,"Bride Services 👰")
        product_tabs=QWidget()
        product_main_lay=QVBoxLayout()
        main_tabs.addTab(product_tabs,"المنتجات🛒")
        product_tabs.setLayout(product_main_lay)
        
        
        #Services Tab
        lay1=QVBoxLayout()
        lay2=QVBoxLayout()
        
        
        lable=QLabel("AB|System")
        lable2=QLabel("AB|System")
        
        lable.setStyleSheet("font-size:40px;font-weight:bold;color:red;max-height:40")
        lable2.setStyleSheet("font-size:40px;font-weight:bold;color:red;max-height:40")
        
        
        
        tab1.setLayout(lay1)
        tab2.setLayout(lay2)
        hlay=QGridLayout()
        hlay.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        lay1.addWidget(lable,alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignHCenter)
        lay1.addLayout(hlay)
        lay1.addStretch(1)
        lay1.setContentsMargins(20,10,20,10)
        hlay2=QGridLayout()
        hlay2.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        lay2.addWidget(lable2,alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignHCenter)
        lay2.addLayout(hlay2)
        lay2.addStretch(1)
        lay2.setContentsMargins(20,10,20,10)
        
        #Products Tab
        add_bt=Button("+ Add",hight=20,width=100,bg_color="lime",hovercolor="green",border="black",hover_border="black",text_color="white")
        remove_bt=Button("Remove",hight=20,width=100,bg_color="red",hovercolor="darkred",border="black",hover_border="black",text_color="white")
        h=QHBoxLayout()
        t=QHBoxLayout()
        products_sub_tab=QTabWidget()
        hair_products=QWidget()
        skin_products=QWidget()
        tint_products=QWidget()
        all_pro=QWidget()
        h.addStretch(1)
        h.addWidget(add_bt,alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignRight)
        h.addLayout(t)
        h.addWidget(remove_bt,alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignRight)
        product_main_lay.addLayout(h)
        product_main_lay.addWidget(products_sub_tab)
        product_main_lay.setStretch(0, 0)
        product_main_lay.setStretch(1, 1)
        # product_main_lay.addStretch(1)
        products_sub_tab.addTab(hair_products,"منتجات الشعر💇‍♀️")
        products_sub_tab.addTab(skin_products,"منتجات البشرة💄")
        products_sub_tab.addTab(tint_products,"الصبغات🎨")
        products_sub_tab.addTab(all_pro,"شراء بضاعة")
        lay11=QVBoxLayout(hair_products)
        lay12=QVBoxLayout(skin_products)
        lay13=QVBoxLayout(tint_products)
        lay14=QVBoxLayout(all_pro)
        
        # lay11.addStretch(1)
        pro=Product_lay("Hair","blue")
        pro2=Product_lay("Skin","red")
        pro3=Product_lay("Tint","purple")
        all_p=Product_lay2("#000080")
        self.product=pro
        self.product2=pro2
        self.product3=pro3
        self.pro=all_p
        lay11.addWidget(self.product)
        lay12.addWidget(self.product2)
        lay13.addWidget(self.product3)
        lay14.addWidget(self.pro)
        
        
        #Buttons Fanctions
        def Hair__Form():
            while hlay.count()>0:
                item=hlay.takeAt(0)
                widget=item.widget()
                if widget is not None:
                    widget.setParent(None)
                    widget.deleteLater()
            wr.execute("SELECT * FROM Hair_Service")
            rows= wr.fetchall()
            line_column=0
            line_row=0
            for n_row in rows:
                if not rows:
                    print("No Rows From DB")
                if line_column>=6 and line_row>=3:
                    msg=QMessageBox(text="❌ This Widget Takex Just 18 Items")
                    msg.exec()
                    break
                    
                if line_column>=6 and line_row<=3:
                    line_column=0  
                    line_row+=1
                
                n_id=n_row[0]
                n_text=n_row[1]
                n_price=n_row[2]
                
                hlay.addWidget(servic_form(_id=n_id,text=n_text,price=str(n_price)),line_row,line_column)
                line_column+=1
            wr.execute("UPDATE Hair_Service SET deletable=?",(0,))
            wd.commit()
            
            
            
        def Skin__Form():
            while hlay2.count()>0:
                item=hlay2.takeAt(0)
                widget=item.widget()
                if widget is not None:
                    widget.setParent(None)
                    widget.deleteLater()
            wr.execute("SELECT * FROM Skin_Service")
            rows= wr.fetchall()
            line_column=0
            line_row=0
            for n_row in rows:
                if not rows:
                    print("No Rows From DB")
                if line_column>=6 and line_row>=3:
                    msg=QMessageBox(text="❌ This Widget Takex Just 18 Items")
                    msg.exec()
                    break
                    
                if line_column>=6 and line_row<=3:
                    line_column=0  
                    line_row+=1
                
                n_id=n_row[0]
                n_text=n_row[1]
                n_price=n_row[2]
                
                hlay2.addWidget(servic_form2(_id=n_id,text=n_text,price=str(n_price)),line_row,line_column)
                line_column+=1
            wr.execute("UPDATE Hair_Service SET deletable=?",(0,))
            wd.commit()
        Skin__Form()
        Hair__Form()
        
        
        windows=[] 
        
        
        def add_form(self):
            if not admin_id and servic_tab2.currentWidget()!=tab3:
                b1.setDisabled(True)
                b2.setDisabled(True)
            else:
                b1.setDisabled(False)
                b2.setDisabled(False)
                if servic_tab2.currentWidget()==tab1:
                    wr.execute("SELECT * FROM Hair_Service")
                    row=wr.fetchall()
                    count=len(row)
                    if count>=18:
                        msg=QMessageBox(text="⚠ Sorry This Widget Takes Only 18 Card")
                        msg.exec()
                    elif count<18:
                        wr.execute("INSERT INTO Hair_Service(text,price,deletable,type) VALUES (?,?,?,?)",("الخدمة",0,False,"Hair_Service"))
                        wd.commit()
                        Hair__Form()
                elif servic_tab2.currentWidget()==tab2:
                     wr.execute("SELECT * FROM Skin_Service")
                     row=wr.fetchall()
                     count=len(row)
                     if count>=18:
                        msg=QMessageBox(text="⚠ Sorry This Widget Takes Only 18 Card")
                        msg.exec()
                     elif count<18:
                        wr.execute("INSERT INTO Skin_Service(text,price,deletable,type) VALUES (?,?,?,?)",("الخدمة",0,False,"Skin_Service"))
                        wd.commit()
                        Skin__Form()
                elif servic_tab2.currentWidget()==tab3:
                    book_window=QMdiSubWindow()
                    book_window.setWindowTitle("Booking Window 📝")
                    book_window.setStyleSheet("background-color:white")
                    book_window.setFixedSize(800,400)
                    widget=QWidget()
                    grid=QGridLayout()
                    widget.setLayout(grid)
                    book_window.setWidget(widget)
                    name=editline(width=150)
                    name.setPlaceholderText("الاسم")
                    phone=editline(width=150)
                    phone.setPlaceholderText("رقم الهاتف")
                    national=editline(width=150)
                    national.setPlaceholderText("الرقم القومي")
                    price=editline(width=150)
                    price.setPlaceholderText("السعر")
                    paid=editline(width=150)
                    paid.setPlaceholderText("المدفوع")
                    date=QDateTimeEdit()
                    date.setDate(QDate.currentDate())
                    btn=Button("Save")
                    grid.addWidget(name,0,0)
                    grid.addWidget(phone,0,1)
                    grid.addWidget(national,0,2)
                    grid.addWidget(price,1,0)
                    grid.addWidget(paid,1,2)
                    grid.addWidget(date,2,1)
                    grid.addWidget(btn,3,1)
                    windows.append(book_window)
                    book_window.show()
                    
                    def Save():
                        if btn.clicked:
                            name1=name.text()
                            price1=price.text()
                            paid1=paid.text()
                            phone1=phone.text()
                            national1=national.text()
                            date1=date.dateTime().toString("yyyy-MM-dd HH:mm:ss")
                            try:
                                url="http://127.0.0.1:8000/bride/book"
                                data={
                                    "name":name1,
                                    "price":float(price1),
                                    "paid":float(paid1),
                                    "phone":phone1,
                                    "national":national1,
                                    "date":date1
                                }
                                if name1!="" and (price1!="" and is_number(price1))and(paid1!=""and is_number(paid1))and (phone1!="" and phone1.isdigit())and (national1!=""and national1.isdigit())and date1!="":
                                    r=requests.post(url,json=data)
                                    res=r.json()
                                    if res["status"]=="ok":
                                        msg2=QMessageBox(text="✅تم الحجز")
                                        msg2.exec()
                                        windows.append(msg2)
                                    else:
                                        msg2=QMessageBox(text="❌ حدث خطا في السيرفر")
                                        msg2.exec()
                                        windows.append(msg2)
                                else:
                                    msg2=QMessageBox(text="⚠ برجاء ملئ جميع الخانات بالطريفة الصحيحة")
                                    msg2.exec()
                                    windows.append(msg2)
                            except Exception as e:
                                ex=str(e)
                                msg2=QMessageBox(text=f"❌ خطا في السيرفر\n{e}")
                                msg2.exec()
                            finally:
                                name.clear()
                                phone.clear()
                                national.clear()
                                price.clear()
                                paid.clear()
                                book_window.hide()
                                load_bookings()
                    btn.clicked.connect(Save)
                            
        table=QTableWidget()
        
        b2.clicked.connect(add_form)
        def add_product():
            if not admin_id:
                add_bt.setDisabled(True)
            else:
                if products_sub_tab.currentWidget()==hair_products:
                    self.product.grid()
                    edit_window=QMdiSubWindow()
                    edit_window.setWindowTitle("Editing")
                    edit_window.setStyleSheet("background-color:white")
                    edit_window.setFixedSize(600,300)
                    Edit_lay=QVBoxLayout()
                    widget=QWidget()
                    widget.setLayout(Edit_lay)
                    edit_window.setWidget(widget)
                    line2=editline(width=150)
                    line2.setPlaceholderText("Enter Servic Name")
                    line3=editline(width=150)
                    line3.setPlaceholderText("Enter Price")
                    line4=editline(width=150)
                    line4.setPlaceholderText("Enter Amount")
                    bt3=Button("Save")
                    Edit_lay.addWidget(line2,alignment=Qt.AlignmentFlag.AlignHCenter)
                    Edit_lay.addWidget(line3,alignment=Qt.AlignmentFlag.AlignHCenter)
                    Edit_lay.addWidget(line4,alignment=Qt.AlignmentFlag.AlignHCenter)
                    Edit_lay.addWidget(bt3,alignment=Qt.AlignmentFlag.AlignHCenter)
                    windows.append(edit_window)
                    edit_window.show()
                    
                    def save():
                        name=line2.text()
                        price=line3.text()
                        amount=line4.text()
                        if is_number(price)and amount.isdigit() and name!="":
                            try:
                                data={"name":name,
                                      "price":float(price),
                                      "amount":int(amount),
                                      "kind":"Hair"}
                                r=requests.post("http://127.0.0.1:8000/products/add",json=data)
                                res=r.json()
                                if res["status"]=="ok":
                                    edit_window.hide()
                                    self.product.grid()
                                else:
                                    msg=QMessageBox(text="❌Error")
                                    msg.exec()
                            except Exception as e:
                                msg=QMessageBox(text=f"❌Error\n{str(e)}")
                                msg.exec()
                        else:
                            msg=QMessageBox(text="❌Enter All Values Right")
                            msg.exec()
                    bt3.clicked.connect(save)
                elif products_sub_tab.currentWidget()==skin_products:
                    self.product2.grid()
                    edit_window=QMdiSubWindow()
                    edit_window.setWindowTitle("Editing")
                    edit_window.setStyleSheet("background-color:white")
                    edit_window.setFixedSize(600,300)
                    Edit_lay=QVBoxLayout()
                    widget=QWidget()
                    widget.setLayout(Edit_lay)
                    edit_window.setWidget(widget)
                    line2=editline(width=150)
                    line2.setPlaceholderText("Enter Servic Name")
                    line3=editline(width=150)
                    line3.setPlaceholderText("Enter Price")
                    line4=editline(width=150)
                    line4.setPlaceholderText("Enter Amount")
                    bt3=Button("Save")
                    Edit_lay.addWidget(line2,alignment=Qt.AlignmentFlag.AlignHCenter)
                    Edit_lay.addWidget(line3,alignment=Qt.AlignmentFlag.AlignHCenter)
                    Edit_lay.addWidget(line4,alignment=Qt.AlignmentFlag.AlignHCenter)
                    Edit_lay.addWidget(bt3,alignment=Qt.AlignmentFlag.AlignHCenter)
                    windows.append(edit_window)
                    edit_window.show()
                    
                    def save():
                        name=line2.text()
                        price=line3.text()
                        amount=line4.text()
                        if is_number(price)and amount.isdigit() and name!="":
                            try:
                                data={"name":name,
                                      "price":float(price),
                                      "amount":int(amount),
                                      "kind":"Skin"}
                                r=requests.post("http://127.0.0.1:8000/products/add",json=data)
                                res=r.json()
                                if res["status"]=="ok":
                                    edit_window.hide()
                                    self.product2.grid()
                                else:
                                    msg=QMessageBox(text="❌Error")
                                    msg.exec()
                            except Exception as e:
                                msg=QMessageBox(text=f"❌Error\n{str(e)}")
                                msg.exec()
                        else:
                            msg=QMessageBox(text="❌Enter All Values Right")
                            msg.exec()
                    bt3.clicked.connect(save)
                    
                elif products_sub_tab.currentWidget()==tint_products:
                    self.product3.grid()
                    edit_window=QMdiSubWindow()
                    edit_window.setWindowTitle("Editing")
                    edit_window.setStyleSheet("background-color:white")
                    edit_window.setFixedSize(600,300)
                    Edit_lay=QVBoxLayout()
                    widget=QWidget()
                    widget.setLayout(Edit_lay)
                    edit_window.setWidget(widget)
                    line2=editline(width=150)
                    line2.setPlaceholderText("Enter Servic Name")
                    line3=editline(width=150)
                    line3.setPlaceholderText("Enter Price")
                    line4=editline(width=150)
                    line4.setPlaceholderText("Enter Amount")
                    bt3=Button("Save")
                    Edit_lay.addWidget(line2,alignment=Qt.AlignmentFlag.AlignHCenter)
                    Edit_lay.addWidget(line3,alignment=Qt.AlignmentFlag.AlignHCenter)
                    Edit_lay.addWidget(line4,alignment=Qt.AlignmentFlag.AlignHCenter)
                    Edit_lay.addWidget(bt3,alignment=Qt.AlignmentFlag.AlignHCenter)
                    windows.append(edit_window)
                    edit_window.show()
                    
                    def save():
                        name=line2.text()
                        price=line3.text()
                        amount=line4.text()
                        if is_number(price)and amount.isdigit() and name!="":
                            try:
                                data={"name":name,
                                      "price":float(price),
                                      "amount":int(amount),
                                      "kind":"Tint"}
                                r=requests.post("http://127.0.0.1:8000/products/add",json=data)
                                res=r.json()
                                if res["status"]=="ok":
                                    edit_window.hide()
                                    self.product3.grid()
                                else:
                                    msg=QMessageBox(text="❌Error")
                                    msg.exec()
                            except Exception as e:
                                msg=QMessageBox(text=f"❌Error\n{str(e)}")
                                msg.exec()
                        else:
                            msg=QMessageBox(text="❌Enter All Values Right")
                            msg.exec()
                    bt3.clicked.connect(save)
                elif   products_sub_tab.currentWidget()==all_pro:
                    self.pro.grid()
                         
        add_bt.clicked.connect(add_product)
        
        def update_pro():
            
            if products_sub_tab.currentWidget()==hair_products:
                self.product.grid()
            elif products_sub_tab.currentWidget()==skin_products:
                self.product2.grid()
            elif products_sub_tab.currentWidget()==tint_products:
                self.product3.grid()
            elif products_sub_tab.currentWidget()==all_pro:
                self.pro.grid()
            
        products_sub_tab.currentChanged.connect(update_pro)   
                
        def load_bookings():
            try:
                r=requests.get(f"{api}/books/data")
                res=r.json()
                table.clear()
                table.setRowCount(len(res))
                table.setColumnCount(11)
                table.setHorizontalHeaderLabels(["الاسم","السعر","المدفوع","الباقي","التلغون","الرفم القومي","تاريخ الخروج","تاريخ الححز","اتمام الحجز","التعديل","الفاء الحجز"])
                header=table.horizontalHeader()
                header.setSectionResizeMode(QHeaderView.Stretch)
                for row,b in enumerate (res):
                    booking_id=b["id"]
                    name=b["name"]
                    price=b["price"]
                    bid=booking_id
                    table.setItem(row,0,QTableWidgetItem(b["name"]))
                    table.setItem(row,1,QTableWidgetItem(str(b["price"])))
                    table.setItem(row,2,QTableWidgetItem(str(b["paid"])))
                    table.setItem(row,3,QTableWidgetItem(str(b["rest"])))
                    table.setItem(row,4,QTableWidgetItem(b["phone"]))
                    table.setItem(row,5,QTableWidgetItem(b["national"]))
                    table.setItem(row,6,QTableWidgetItem(b["date"]))
                    table.setItem(row,7,QTableWidgetItem(b["book_date"]))
                    
                    done_btn = Button("Done",hight=10,width=80,bg_color="lime",hovercolor="green",border="black",hover_border="black",text_color="white")
                    table.setCellWidget(row, 8, done_btn)
                    done_btn.clicked.connect(lambda _, bid=bid,name=name,price=price,kind="Bride Booking": book_done(bid,name,price,kind))
                    
                    edit_btn = Button("Edit",hight=10,width=80,bg_color="orange",hovercolor="darkorange",border="black",hover_border="black",text_color="white")
                    edit_btn.clicked.connect(lambda _, bid=bid: edit_booking(bid))
                    
                    table.setCellWidget(row, 9, edit_btn)

                    # زرار Cancel
                    cancel_btn = Button("Cancel",hight=10,width=80,bg_color="red",hovercolor="darkred",border="black",hover_border="black",text_color="white")
                    cancel_btn.clicked.connect(lambda _, bid=bid: cancel_booking(bid))
                    table.setCellWidget(row, 10, cancel_btn)
            except Exception as e:
                msg=QMessageBox(text=f"❌Error\n{str(e)}")
                msg.exec()
        def book_done(booking_id,name,price,kind):
            msg=QMessageBox(text="هل تريد اتمام الحجز؟")
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            result=msg.exec()
            if result==QMessageBox.Yes:
                
                try:
                    data={"id":booking_id,
                        "service_name":name,
                        "service_price":price,
                        "service_kind":kind}
                    r=requests.post(f"{api}/services/bride",json=data)
                    res=r.json()
                    if res["status"]=="ok":
                        load_bookings()
                    else:
                        msg2=QMessageBox(text="❌Error with Server")
                        msg2.exec()
                except Exception as e:
                    msg2=QMessageBox(text=f"❌Error\n{str(e)}")
                    msg2.exec()
            else:
                pass
                        
                    
                
            
        
        def edit_booking(booking_id):
            edit_page = QMdiSubWindow()
            edit_page.setWindowTitle("صفحة التعديل")
            edit_page.setStyleSheet("background-color:white")
            edit_page.setFixedSize(800, 400)

            widget = QWidget()
            grid = QGridLayout()
            widget.setLayout(grid)
            edit_page.setWidget(widget)

            name = editline(width=150)
            name.setPlaceholderText("الاسم")

            phone = editline(width=150)
            phone.setPlaceholderText("رقم الهاتف")

            national = editline(width=150)
            national.setPlaceholderText("الرقم القومي")

            price = editline(width=150)
            price.setPlaceholderText("السعر")

            paid = editline(width=150)
            paid.setPlaceholderText("المدفوع")

            date = QDateTimeEdit()
            date.setDate(QDate.currentDate())

            # ✅ تشيك بوكس علشان نعرف إذا اليوزر عايز يغيّر التاريخ ولا لأ
            change_date = QCheckBox("تعديل التاريخ")

            btn = Button("Save")

            grid.addWidget(name,     0, 0)
            grid.addWidget(phone,    0, 1)
            grid.addWidget(national, 0, 2)
            grid.addWidget(price,    1, 0)
            grid.addWidget(paid,     1, 2)
            grid.addWidget(date,     2, 1)
            grid.addWidget(change_date, 2, 2)  # 👈 التشيك بوكس جنب التاريخ
            grid.addWidget(btn,      3, 1)

            windows.append(edit_page)
            edit_page.show()

            def Save():
                if btn.clicked:
                    name1     = name.text()
                    price1    = price.text()
                    paid1     = paid.text()
                    phone1    = phone.text()
                    national1 = national.text()

                    try:
                        url = f"http://127.0.0.1:8000/books/update/{booking_id}"
                        data = {}

                        if name1:
                            data["name"] = name1
                        if price1 and is_number(price1):
                            data["price"] = float(price1)
                        if paid1 and is_number(paid1):
                            data["paid"] = float(paid1)
                        if phone1 and phone1.isdigit():
                            data["phone"] = phone1
                        if national1 and national1.isdigit():
                            data["national"] = national1

                        # ✅ التاريخ مش هيتبعت غير لو التشيك بوكس متعلم
                        if change_date.isChecked():
                            date1 = date.dateTime().toString("yyyy-MM-dd HH:mm:ss")
                            if date1:
                                data["date"] = date1

                        if not data:
                            msg2 = QMessageBox(text="⚠ مفيش حاجة اتعدّلت")
                            msg2.exec()
                            windows.append(msg2)
                            return

                        r = requests.patch(url, json=data)
                        res = r.json()

                        if res["status"] == "ok":
                            load_bookings()
                            msg2 = QMessageBox(text="تم التعديل✅")
                            msg2.exec()
                            windows.append(msg2)
                        else:
                            msg2 = QMessageBox(text="❌ حدث خطا في السيرفر")
                            msg2.exec()
                            windows.append(msg2)

                    except Exception as e:
                        ex = str(e)
                        msg2 = QMessageBox(text=f"❌ خطا في السيرفر\n{ex}")
                        msg2.exec()
                    finally:
                        name.clear()
                        phone.clear()
                        national.clear()
                        price.clear()
                        paid.clear()
                        edit_page.hide()

            btn.clicked.connect(Save)

        
        
        
        def cancel_booking(booking_id):
                try:
                    r = requests.delete(f"http://127.0.0.1:8000/books/delete/{booking_id}")
                    res = r.json()

                    if res.get("status") == "ok":
                        load_bookings()   # refresh
                    else:
                        print("Failed delete:", res)

                except Exception as e:
                    print("Delete Error:", e)
        
                
                
                



        vlay=QVBoxLayout()
        vlay.addWidget(table)
        tab3.setLayout(vlay)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        load_bookings()
                    
                    
                    
                    
                    
                    
                    
            
        
        def Tab3():
            if servic_tab2.currentWidget()==tab3:
                b2.setDisabled(False)
        servic_tab2.currentChanged.connect(Tab3)
        
        
        
        
        
        
        def remove_button():
            msg=QMessageBox(text="⚠ هل انت تريد حذف الكروت المختارة؟")
            msg.setWindowTitle("🗑 تاكيد الحذف")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            result=msg.exec()
            if result==QMessageBox.Yes:
                wr.execute("DELETE FROM Hair_Service WHERE deletable=?",(1,))
                wd.commit()
                wr.execute("DELETE FROM Skin_Service WHERE deletable=?",(1,))
                wd.commit()
                Hair__Form()
                Skin__Form()
                
            else:
                pass
                
        b1.clicked.connect(remove_button)
        def remove_pro():
            if not admin_id:
                remove_bt.setDisabled(True)
            else:
                msg=QMessageBox(text="⚠ هل انت متاكد من حذف المنتجات المختارة؟")
                msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
                result=msg.exec()
                if result==QMessageBox.Yes:
                    try:
                        data={"boole":True}
                        r=requests.post(f"{api}/products/delete",json=data)
                        res=r.json()
                        if res["status"]=="ok":
                            pro.grid()
                        else:
                            msg2=QMessageBox(text="❌Error")
                            msg2.exec()
                    except Exception as e:
                            msg2=QMessageBox(text=f"❌Error\n{str(e)}")
                            msg2.exec() 
                else:
                    pass
        remove_bt.clicked.connect(remove_pro)
        def un_delet():
            wr.execute("UPDATE pro_cards SET deletable=?",(0,))
            wd.commit()
        un_delet()
        

            
            
            
        

        
        
        
        
        
          
        
        
        
        
        
        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    l_window=Login_Window()
    
    l_window.show()
    s_window=Signup_Window()
    m_window=main_widow()
    
    sys.exit(app.exec())      
        
        
        
        
        
