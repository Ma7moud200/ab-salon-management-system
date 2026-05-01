from PySide6.QtWidgets import (QPushButton, QLineEdit, QGraphicsDropShadowEffect,QSizePolicy,QVBoxLayout,QHBoxLayout,QLabel,QFrame,QMdiSubWindow,QWidget,QMessageBox,QCheckBox,QGridLayout,QScrollArea)
from PySide6.QtCore import (Qt,QSize)
from PySide6.QtGui import (QColor,QIcon)
import sqlite3
import datetime
import sys
import requests

admin_id=False
db=sqlite3.connect("WDB.db")
cr=db.cursor()
def get_db2():
    db=sqlite3.connect("WDB.db")
    cr=db.cursor()
    return db,cr
def is_number(s:str):
    try:
        float(s)
        return True
    except:
        return False

class Button(QPushButton):
    def __init__(self, text,hight=0,width=0,bg_color="",hovercolor="",border="",hover_border="",text_color=""):
        super().__init__(text)
        self.setStyleSheet("""QPushButton{background-color:white;border-radius:10;color:black;border:2px solid black;min-width:250}
                           QPushButton:hover{background-color:lightgray;border-color:blue}
                           QPushButton:pressed{background-color:gray;color:blue}""")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        if hight!=0 and width!=0 and bg_color!="" and hovercolor!="" and border!="" and hover_border!="" and text_color!="":
            self.setStyleSheet(f"""QPushButton{{background-color:{bg_color};border-radius:10;color:{text_color};border:2px solid {border};width:{width};height:{hight}}}
                           QPushButton:hover{{background-color:{hovercolor};border-color:{hover_border}}}
                           QPushButton:pressed{{background-color:gray;color:blue}}""")
        elif hight!=0 and width!=0:
            self.setStyleSheet(f"""QPushButton{{background-color:white;border-radius:10;color:black;border:2px solid black;width:{width};height:{hight}}}
                           QPushButton:hover{{background-color:lightgray;border-color:blue}}
                           QPushButton:pressed{{background-color:gray;color:blue}}""")
               
        
    def enterEvent(self, event):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(25)
        self.shadow.setColor(QColor(0, 0, 0, 160))
        self.shadow.setOffset(0, 5)
        self.setGraphicsEffect(self.shadow)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setGraphicsEffect(None)
        super().leaveEvent(event)


class editline(QLineEdit):
    def __init__(self, width=500):
        super().__init__()
        # accept int (pixels) or a CSS size string like "50%" or "200px"
        if isinstance(width, int):
            width_css = f"{width}px"
        else:
            width_css = str(width)

        self.setStyleSheet(
            f"QLineEdit{{min-width:{width_css};max-width:{width_css};background-color:white;color:black;border:none;border-bottom:2px solid gray;min-height:25px}}"
            f"QLineEdit:hover{{border-bottom:2px solid blue;background-color:lightgray}}"
            f"QLineEdit:focus{{border-bottom:2px solid blue;background-color:lightgray}}"
        )
        self.setClearButtonEnabled(True)

    def focusInEvent(self, event):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(25)
        self.shadow.setColor(QColor(0, 0, 0, 160))
        self.shadow.setOffset(0, 0)
        self.setGraphicsEffect(self.shadow)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.setGraphicsEffect(None)
        super().focusOutEvent(event)


class passline(QLineEdit):
    def __init__(self, width=500):
        super().__init__()
        # accept int (pixels) or a CSS size string like "50%" or "200px"
        if isinstance(width, int):
            width_css = f"{width}px"
        else:
            width_css = str(width)

        
        self.setEchoMode(QLineEdit.EchoMode.Password)
        self.setClearButtonEnabled(True)
        self.setStyleSheet(
            f"QLineEdit{{min-width:{width_css};border:none;background-color:white;color:black;border-bottom:2px solid gray;min-height:25px}}"
            f"QLineEdit:hover{{border-color:blue;background-color:lightgray}}"
            f"QLineEdit:focus{{border-color:blue;background-color:lightgray}}"
        )

    def focusInEvent(self, event):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(25)
        self.shadow.setColor(QColor(0, 0, 0, 160))
        self.shadow.setOffset(0, 0)
        self.setGraphicsEffect(self.shadow)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.setGraphicsEffect(None)
        super().focusOutEvent(event)
        
        
class radius_Button(QPushButton):
    def __init__(self,text="",size=60,icon=""):
        super().__init__(text)
        
        
        if size%2 == 0:
            r_radius=f"{size/2}px"
        else:
            size=60
            r_radius=f"{size/2}px"
            
        self.setFixedSize(size,size)
        
        if text!="":
            self.setText(text)
        if icon!="":
            self.setIcon(QIcon(f"{icon}"))
            self.setIconSize(self.size())
        
            
            
        self.setStyleSheet(f"QPushButton{{border-radius:{r_radius};background-color:white;border:1px solid black}}"
                           f"QPushButton:hover{{background-color:lightgray;border-color:blue}}"
                           f"QPushButton:pressed{{background-color:gray;border-color:blue}}")
        
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
    def enterEvent(self, event):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(25)
        self.shadow.setColor(QColor(0, 0, 0, 160))
        self.shadow.setOffset(0, 5)
        self.setGraphicsEffect(self.shadow)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setGraphicsEffect(None)
        super().leaveEvent(event)
        


class servic_form(QFrame):
    def __init__(self,text="الخدمة",price="0",_id=None):
        super().__init__()
        
        
        vlay=QVBoxLayout()
        self.setFixedSize(210,200)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground,True)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color:#2746F5;border-radius:10;border:2px solid black")
        self.setLayout(vlay)
        
        vlay.setContentsMargins(10,10,10,10)
        
        lable=QLabel(text)
        lable.setStyleSheet("font-size:25px;font-weight:bold;color:white;max-height:30")
        hlay=QHBoxLayout()
        delet_box=QCheckBox()
        
        line=editline(width=100)
        line.setFixedWidth(70)
        line.setPlaceholderText("Price")
        line.setEnabled(False)
        line.setText(price)
        line.setClearButtonEnabled(False)
        line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        bt1=Button("Edit",hight=30,width=60)
        bt2=Button("Order",hight=30,width=60)
        
        hlay.addWidget(bt2,alignment=Qt.AlignmentFlag.AlignLeft)
        hlay.addWidget(bt1,alignment=Qt.AlignmentFlag.AlignRight)
        delet_box.setStyleSheet("border:none")
        
        # cr.execute("INSERT INTO Hair_Service(text,price) VALUES(?,?)",(
        #     lable.text(),
        #     float(line.text())
        # ))
        # db.commit()
        if _id ==None:
            _id=cr.lastrowid
        else:
            self._id=_id
    
        
        
        
        
        
        
        vlay.addWidget(lable,alignment=Qt.AlignmentFlag.AlignHCenter)
        vlay.addWidget(line,alignment=Qt.AlignmentFlag.AlignHCenter)
        vlay.addLayout(hlay)
        vlay.addWidget(delet_box,alignment=Qt.AlignmentFlag.AlignHCenter)
        vlay.setSpacing(10)
        
            
            
        def Edit():

            db1 = sqlite3.connect("Data.db")
            cr1 = db1.cursor()

            cr1.execute("SELECT admin FROM temp LIMIT 1")
            row = cr1.fetchone()
            if row is not None and row[0] == 1:
                global admin_id
                admin_id = True

            if  admin_id:
                bt1.setDisabled(False)
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
                bt3=Button("Save")
                Edit_lay.addWidget(line2,alignment=Qt.AlignmentFlag.AlignHCenter)
                Edit_lay.addWidget(line3,alignment=Qt.AlignmentFlag.AlignHCenter)
                Edit_lay.addWidget(bt3,alignment=Qt.AlignmentFlag.AlignHCenter)
                edit_window.show()
            
                
            
                    
                    
                def Save():
                    if bt3.clicked:
                        text=line2.text()
                        text2=line3.text()
                        if text!="":
                            if self._id != None:
                                try:
                                    cr.execute("UPDATE Hair_Service SET text=? WHERE h_id=?",(text,self._id))
                                    db.commit()
                                    lable.setText(text)
                                except:
                                    msg2=QMessageBox("❌Error With Data Please Try Again Later")
                                    msg2.exec()
                                    
                        if text2!="" and is_number(text2):
                            try:
                                cr.execute("UPDATE Hair_Service SET price=? WHERE h_id=?",(float(text2),self._id))
                                db.commit()
                                line.setText(f"{text2}")
                            except:
                                msg2.exec()
                        elif not is_number(text2) and text2!="":
                            msg=QMessageBox()
                            msg.setText("❌ The Price Must Be a Number ❌")
                            msg.exec()
                        edit_window.hide()
                bt3.clicked.connect(Save)
            else:
                bt1.setDisabled(True)
            
            
        bt1.clicked.connect(Edit)
        def delet():
            db1 = sqlite3.connect("Data.db")
            cr1 = db1.cursor()

            cr1.execute("SELECT admin FROM temp LIMIT 1")
            row = cr1.fetchone()
            if row is not None and row[0] == 1:
                global admin_id
                admin_id = True
            print(admin_id)
            if admin_id!=False:
                if delet_box.isChecked():
                    cr.execute("UPDATE Hair_Service SET deletable=? WHERE h_id=?",(1,self._id))
                    db.commit()
                else:
                    cr.execute("UPDATE Hair_Service SET deletable=? WHERE h_id=?",(0,self._id))
                    db.commit()
        delet_box.checkStateChanged.connect(delet)
        
        def Order():

            msg=QMessageBox(text="هل تريد الشراء؟")
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            result=msg.exec()
            if result==QMessageBox.Yes:
                if (lable.text()!="" and lable.text!= "الخدمة") and (line.text()!="0" and line.text()!="0.0"):
                    url="http://127.0.0.1:8000/services/data"
                    data={
                        "service_name":lable.text(),
                        "service_price":float(line.text()),
                        "service_kind":"Hair Service"
                    }
                    r=requests.post(url,json=data)
                    res=r.json()
                    if res["status"]=="ok":
                        pass
                    else:
                        msg3=QMessageBox(text="❌ خطا اثناء الطلب")
                        msg3.exec
                else:
                    msg2=QMessageBox(text="⚠ برجاء تعديل الاعدادات الاساسية في الكرت");msg2.exec()
        bt2.clicked.connect(Order)
            
                
        
        
        

class servic_form2(QFrame):
    def __init__(self,text="الخدمة",price="50",_id=None):
        super().__init__()
        
        
        vlay=QVBoxLayout()
        self.setFixedSize(210,200)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground,True)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color:#FF00FF;border-radius:10;border:2px solid black")
        self.setLayout(vlay)
        
        vlay.setContentsMargins(10,10,10,10)
        
        lable=QLabel(text)
        lable.setStyleSheet("font-size:25px;font-weight:bold;color:white;max-height:30")
        hlay=QHBoxLayout()
        delet_box=QCheckBox()
        
        line=editline(width=100)
        line.setFixedWidth(70)
        line.setPlaceholderText("Price")
        line.setEnabled(False)
        line.setText(price)
        line.setClearButtonEnabled(False)
        line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        bt1=Button("Edit",hight=30,width=60)
        bt2=Button("Order",hight=30,width=60)
        
        hlay.addWidget(bt2,alignment=Qt.AlignmentFlag.AlignLeft)
        hlay.addWidget(bt1,alignment=Qt.AlignmentFlag.AlignRight)
        delet_box.setStyleSheet("border:none")
        
        if _id ==None:
            _id=cr.lastrowid
        else:
            self._id=_id
    
        
        
        
        
        
        
        vlay.addWidget(lable,alignment=Qt.AlignmentFlag.AlignHCenter)
        vlay.addWidget(line,alignment=Qt.AlignmentFlag.AlignHCenter)
        vlay.addLayout(hlay)
        vlay.addWidget(delet_box,alignment=Qt.AlignmentFlag.AlignHCenter)
        vlay.setSpacing(10)
        
            
            
        def Edit():
            db1 = sqlite3.connect("Data.db")
            cr1 = db1.cursor()

            cr1.execute("SELECT admin FROM temp LIMIT 1")
            row = cr1.fetchone()
            if row is not None and row[0] == 1:
                global admin_id
                admin_id = True
            if admin_id:
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
                bt3=Button("Save")
                Edit_lay.addWidget(line2,alignment=Qt.AlignmentFlag.AlignHCenter)
                Edit_lay.addWidget(line3,alignment=Qt.AlignmentFlag.AlignHCenter)
                Edit_lay.addWidget(bt3,alignment=Qt.AlignmentFlag.AlignHCenter)
                edit_window.show()
            
                
            
                    
                    
                def Save():
                    if bt3.clicked:
                        text=line2.text()
                        text2=line3.text()
                        if text!="":
                            if self._id != None:
                                try:
                                    cr.execute("UPDATE Skin_Service SET text=? WHERE s_id=?",(text,self._id))
                                    db.commit()
                                    lable.setText(text)
                                except:
                                    msg2=QMessageBox("❌Error With Data Please Try Again Later")
                                    msg2.exec()
                                    
                        if text2!="" and is_number(text2):
                            try:
                                cr.execute("UPDATE Skin_Service SET price=? WHERE s_id=?",(float(text2),self._id))
                                db.commit()
                                line.setText(f"{text2}")
                            except:
                                msg2.exec()
                        elif not is_number(text2) and text2!="":
                            msg=QMessageBox()
                            msg.setText("❌ The Price Must Be a Number ❌")
                            msg.exec()
                        edit_window.hide()
                bt3.clicked.connect(Save)
        bt1.clicked.connect(Edit)
        def delet():
            db1 = sqlite3.connect("Data.db")
            cr1 = db1.cursor()

            cr1.execute("SELECT admin FROM temp LIMIT 1")
            row = cr1.fetchone()
            if row is not None and row[0] == 1:
                global admin_id
                admin_id = True
            if admin_id:
                if delet_box.isChecked():
                    cr.execute("UPDATE Skin_Service SET deletable=? WHERE s_id=?",(1,self._id))
                    db.commit()
                else:
                    cr.execute("UPDATE Skin_Service SET deletable=? WHERE s_id=?",(0,self._id))
                    db.commit()
        delet_box.checkStateChanged.connect(delet)
        def Order():

            msg=QMessageBox(text="هل تريد الشراء؟")
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            result=msg.exec()
            if result==QMessageBox.Yes:
                if (lable.text()!="" and lable.text!= "الخدمة") and (line.text()!="0" and line.text()!="0.0"):
                    url="http://127.0.0.1:8000/services/data"
                    data={
                        "service_name":lable.text(),
                        "service_price":float(line.text()),
                        "service_kind":"Skin Service"
                    }
                    r=requests.post(url,json=data)
                    res=r.json()
                    if res["status"]=="ok":
                        pass
                    else:
                        msg3=QMessageBox(text="❌ خطا اثناء الطلب")
                        msg3.exec
                else:
                    msg2=QMessageBox(text="⚠ برجاء تعديل الاعدادات الاساسية في الكرت");msg2.exec()
        bt2.clicked.connect(Order)
        
        
        
        
class Product_lay(QWidget):
    def __init__(self, kind,color):
        super().__init__()

        self.kind = kind
        self.color=color
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.main_lay = QVBoxLayout(self)
        self.scrol = QScrollArea()
        self.scrol.setWidgetResizable(True)
        self.scrol.setStyleSheet("""
                        QScrollArea {
                            border: none; /* شيل البوردر تماما */
                            background: transparent; /* خلي خلفيته شفافة */
                        }

                        QWidget#container {
                            background: white;
                            border-radius: 10px;
                        }

                        QScrollBar:vertical {
                            border: none;
                            background: #E0E0E0;
                            width: 10px;
                            margin: 0px;
                            border-radius: 5px;
                        }

                        QScrollBar::handle:vertical {
                            background: #0078FF;
                            min-height: 30px;
                            border-radius: 5px;
                        }

                        QScrollBar::handle:vertical:hover {
                            background: #005FCC;
                        }

                        QScrollBar::handle:vertical:pressed {
                            background: #0040A0;
                        }

                        QScrollBar::add-line,
                        QScrollBar::sub-line {
                            height: 0px;
                        }

                        QScrollBar::add-page,
                        QScrollBar::sub-page {
                            background: none;
                        }
                    """)

        self.scrol.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        

        self.serch_box = editline(500)
        self.serch_box.setPlaceholderText("Search...")
        self.main_lay.addWidget(self.serch_box, alignment=Qt.AlignmentFlag.AlignHCenter)

        # ال container اللي جواه ال grid layout
        self.container = QWidget()
        self.lay = QGridLayout(self.container)
        self.container.setLayout(self.lay)

        self.scrol.setWidget(self.container)
        self.main_lay.addWidget(self.scrol)
        self.main_lay.setStretch(0, 0)  # search
        self.main_lay.setStretch(1, 1) 
        self.serch_box.textChanged.connect(self.search)
        
        # لو حابب يحمل المنتجات مباشرة
        self.grid()

    def grid(self):
    # امسح القديم من اللاي أوت
        while self.lay.count() > 0:
            item = self.lay.takeAt(0)
            w = item.widget()
            if w is not None:
                w.setParent(None)
                w.deleteLater()

        # امسح الليست القديمة عشان مفيش تكرار
        self.cards = []

        try:
            r = requests.get(f"http://127.0.0.1:8000/products/cards/{self.kind}")
            res = r.json()
            column = 0
            row = 0
            if res:
                for c in res:
                    if column >= 5:   # نفس عدد الأعمدة اللي عندك
                        row += 1
                        column = 0

                    card = Product_card(
                        c["name"],
                        c["price"],
                        c["amount"],
                        c["id"],
                        self.kind,
                        self.color,
                        parent_lay=self
                    )
                    self.cards.append(card)
                    self.lay.addWidget(card, row, column)
                    column += 1

        except Exception as e:
            msg = QMessageBox(text=f"❌Error\n{str(e)}")
            msg.exec()
    def search(self):
        text = self.serch_box.text().strip().lower()

        # فضّي اللاي أوت (بس من غير ما تمسح الكروت)
        while self.lay.count() > 0:
            self.lay.takeAt(0)

        row = 0
        col = 0
        max_columns = 5  # زي اللي في grid

        for card in self.cards:
            name = card.lable.text().strip().lower()

            if text == "" or text in name:
                card.show()
                self.lay.addWidget(card, row, col)
                col += 1
                if col >= max_columns:
                    col = 0
                    row += 1
            else:
                card.hide()

            

        
class Product_card(QFrame):
    def __init__(self,text,price,amount,_id,kind,color="blue",parent_lay=None):
        super().__init__()
        self.text=text
        self.price=price
        self.amount=amount
        self._id=_id
        self.kind=kind
        self.parent_lay=parent_lay
        self.vlay=QVBoxLayout()
        self.setFixedSize(210,200)
        self.setStyleSheet(f"background-color:{color};border-radius:10;border:2px solid black")
        self.setLayout(self.vlay)
        self.lable=QLabel(str(self.text))
        self.lable.setStyleSheet("font-size:25px;font-weight:bold;color:white;max-height:30;border:none")
        self.price_holder=editline(width=100)
        self.price_holder.setPlaceholderText("السعر")
        self.price_holder.setText(str(self.price))
        self.price_holder.setDisabled(True)
        self.amount_holder=editline("100")
        self.amount_holder.setPlaceholderText("الكمية")
        self.amount_holder.setText(str(self.amount))
        self.amount_holder.setDisabled(True)
        self.price_holder.setClearButtonEnabled(False)
        self.price_holder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.amount_holder.setClearButtonEnabled(False)
        self.amount_holder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bt1=Button("SELL",hight=20,width=100,bg_color="red",hovercolor="darkred",border="black",hover_border="black",text_color="white")
        self.bt2=Button("EDIT",hight=20,width=100,bg_color="orange",hovercolor="darkorange",border="black",hover_border="black",text_color="white")
        self.bt3=Button("USE",hight=20,width=100,bg_color="lime",hovercolor="green",border="black",hover_border="black",text_color="white")
        self.check=QCheckBox("الحذف")
        self.hlay=QHBoxLayout()
        self.hlay.addWidget(self.bt1,alignment=Qt.AlignmentFlag.AlignLeft)
        self.hlay.addWidget(self.bt2,alignment=Qt.AlignmentFlag.AlignRight)
        self.vlay.addWidget(self.lable,alignment=Qt.AlignmentFlag.AlignHCenter)
        self.vlay.addWidget(self.price_holder,alignment=Qt.AlignmentFlag.AlignHCenter)
        self.vlay.addWidget(self.amount_holder,alignment=Qt.AlignmentFlag.AlignHCenter)
        self.vlay.addLayout(self.hlay)
        self.vlay.addWidget(self.bt3)
        self.vlay.addWidget(self.check)
        self.bt2.clicked.connect(self.edit)
        self.bt1.clicked.connect(self.sell)
        self.bt3.clicked.connect(self.use)
        
        self.check.checkStateChanged.connect(self.remove)
        self.check.setStyleSheet("border:none;color:white")
    
    def use(self):
        
        data={"id":self._id}
        try:
            r=requests.post("http://127.0.0.1:8000/products/use",json=data)
            res=r.json()
            if res["status"]=="ok":
                msg=QMessageBox(text="✅تمت العملية")
                msg.exec()
                if hasattr(self, "parent_lay") and self.parent_lay is not None:
                    self.parent_lay.grid()
            elif res["status"]=="no":
                msg=QMessageBox(text="❌No Product In Stock")
                msg.exec()
            else:
                msg=QMessageBox(text="❌حدث خطا")
                msg.exec()
        except Exception as e:
            msg=QMessageBox(text=f"❌Error\n{str(e)}")
            msg.exec()
    def sell(self):
        data={"id":self._id}
        try:
            r=requests.post("http://127.0.0.1:8000/products/sell",json=data)
            res=r.json()
            if res["status"]=="ok":
                msg=QMessageBox(text="✅تمت العملية")
                msg.exec()
                if hasattr(self, "parent_lay") and self.parent_lay is not None:
                    self.parent_lay.grid()
            elif res["status"]=="no":
                msg=QMessageBox(text="❌No Product In Stock")
                msg.exec()
            else:
                msg=QMessageBox(text="❌حدث خطا")
                msg.exec()
        except Exception as e:
            msg=QMessageBox(text=f"❌Error\n{str(e)}")
            msg.exec()
            
    def edit(self):
        db1 = sqlite3.connect("Data.db")
        cr1 = db1.cursor()

        cr1.execute("SELECT admin FROM temp LIMIT 1")
        row = cr1.fetchone()
        if row is not None and row[0] == 1:
            global admin_id
            admin_id = True
        if admin_id:
            self.bt2.setDisabled(False)
            self.edit_window=QMdiSubWindow()
            self.edit_window.setWindowTitle("Editing")
            self.edit_window.setStyleSheet("background-color:white")
            self.edit_window.setFixedSize(600,300)
            self.Edit_lay=QVBoxLayout()
            self.widget=QWidget()
            self.widget.setLayout(self.Edit_lay)
            self.edit_window.setWidget(self.widget)
            self.line2=editline(width=150)
            self.line2.setPlaceholderText("Enter Servic Name")
            self.line3=editline(width=150)
            self.line3.setPlaceholderText("Enter Price")
            self.line4=editline(width=150)
            self.line4.setPlaceholderText("Enter Amount")
            self.bt3=Button("Save")
            self.Edit_lay.addWidget(self.line2,alignment=Qt.AlignmentFlag.AlignHCenter)
            self.Edit_lay.addWidget(self.line3,alignment=Qt.AlignmentFlag.AlignHCenter)
            self.Edit_lay.addWidget(self.line4,alignment=Qt.AlignmentFlag.AlignHCenter)
            self.Edit_lay.addWidget(self.bt3,alignment=Qt.AlignmentFlag.AlignHCenter)
            self.edit_window.show()
            self.bt3.clicked.connect(self.save)
            
    def save(self):
        name = self.line2.text().strip()
        price_text = self.line3.text().strip()
        amount_text = self.line4.text().strip()

        # هنبدأ بـ id بس
        data = {
            "id": self._id,
        }

        # الاسم (لو اتكتب)
        if name != "":
            data["name"] = name

        # السعر (لو اتكتب)
        if price_text != "":
            if not is_number(price_text):
                msg = QMessageBox(text="❌ السعر لازم يكون رقم")
                msg.exec()
                return
            data["price"] = float(price_text)

        # الكمية (لو اتكتبت)
        if amount_text != "":
            if not amount_text.isdigit():
                msg = QMessageBox(text="❌ الكمية لازم تكون رقم صحيح")
                msg.exec()
                return
            data["amount"] = int(amount_text)

        # لو مفيش أي تعديل (id بس)
        if len(data) == 1:
            msg = QMessageBox(text="⚠️ مفيش أي تعديل حصل")
            msg.exec()
            return

        try:
            r = requests.post("http://127.0.0.1:8000/products/update", json=data)
            print("UPDATE response:", r.status_code, r.text)  # شوف في التيرمنال لو في مشكلة

            res = r.json()
            if res.get("status") == "ok":
                # مهم: ننادي grid على ال object مش على الكلاس
                if hasattr(self, "parent_lay") and self.parent_lay is not None:
                    self.parent_lay.grid()
                self.edit_window.hide()
            else:
                msg = QMessageBox(text="❌ Error في التعديل")
                msg.exec()
        except Exception as e:
            msg = QMessageBox(text=f"❌Error\n{str(e)}")
            msg.exec()

    def remove(self):
        boole=None
        
        if self.check.isChecked()==True:
            boole=True
            data={"id":self._id,
                  "boole":boole}
            try:
                r=requests.post("http://127.0.0.1:8000/product/remove",json=data)
                res=r.json()
                if res["status"]=="ok":
                    pass
                else:
                    msg=QMessageBox(text="❌Error")
                    msg.exec()
            except Exception as e:
                msg=QMessageBox(text=f"❌Error\n{str(e)}")
                msg.exec()
        else:
            boole=False
            data={"id":self._id,
                  "boole":boole}
            try:
                r=requests.post("http://127.0.0.1:8000/product/remove",json=data)
                res=r.json()
                if res["status"]=="ok":
                    pass
                else:
                    msg=QMessageBox(text="❌Error")
                    msg.exec()
            except Exception as e:
                msg=QMessageBox(text=f"❌Error\n{str(e)}")
                msg.exec()
            
        
    
            
            
        
        
        
class Product_lay2(QWidget):
    def __init__(self,color):
        super().__init__()

        
        self.color=color
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.main_lay = QVBoxLayout(self)
        self.scrol = QScrollArea()
        self.scrol.setWidgetResizable(True)
        self.scrol.setStyleSheet("""
                        QScrollArea {
                            border: none; /* شيل البوردر تماما */
                            background: transparent; /* خلي خلفيته شفافة */
                        }

                        QWidget#container {
                            background: white;
                            border-radius: 10px;
                        }

                        QScrollBar:vertical {
                            border: none;
                            background: #E0E0E0;
                            width: 10px;
                            margin: 0px;
                            border-radius: 5px;
                        }

                        QScrollBar::handle:vertical {
                            background: #0078FF;
                            min-height: 30px;
                            border-radius: 5px;
                        }

                        QScrollBar::handle:vertical:hover {
                            background: #005FCC;
                        }

                        QScrollBar::handle:vertical:pressed {
                            background: #0040A0;
                        }

                        QScrollBar::add-line,
                        QScrollBar::sub-line {
                            height: 0px;
                        }

                        QScrollBar::add-page,
                        QScrollBar::sub-page {
                            background: none;
                        }
                    """)

        self.scrol.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        

        self.serch_box = editline(500)
        self.serch_box.setPlaceholderText("Search...")
        self.main_lay.addWidget(self.serch_box, alignment=Qt.AlignmentFlag.AlignHCenter)

        # ال container اللي جواه ال grid layout
        self.container = QWidget()
        self.lay = QGridLayout(self.container)
        self.container.setLayout(self.lay)

        self.scrol.setWidget(self.container)
        self.main_lay.addWidget(self.scrol)
        self.main_lay.setStretch(0, 0)  # search
        self.main_lay.setStretch(1, 1) 
        self.serch_box.textChanged.connect(self.search)
        
        # لو حابب يحمل المنتجات مباشرة
        self.grid()

    def grid(self):
    # امسح القديم من اللاي أوت
        while self.lay.count() > 0:
            item = self.lay.takeAt(0)
            w = item.widget()
            if w is not None:
                w.setParent(None)
                w.deleteLater()

        # امسح الليست القديمة عشان مفيش تكرار
        self.cards = []

        try:
            r = requests.get(f"http://127.0.0.1:8000/products/cards/all/1")
            res = r.json()
            column = 0
            row = 0
            if res:
                for c in res:
                    if column >= 5:   # نفس عدد الأعمدة اللي عندك
                        row += 1
                        column = 0

                    card = Product_card2(
                        c["name"],
                        c["price"],
                        c["amount"],
                        c["id"],
                        self.color,
                        parent_lay=self
                    )
                    self.cards.append(card)
                    self.lay.addWidget(card, row, column)
                    column += 1

        except Exception as e:
            msg = QMessageBox(text=f"❌Error\n{str(e)}")
            msg.exec()
    def search(self):
        text = self.serch_box.text().strip().lower()

        # فضّي اللاي أوت (بس من غير ما تمسح الكروت)
        while self.lay.count() > 0:
            self.lay.takeAt(0)

        row = 0
        col = 0
        max_columns = 5  # زي اللي في grid

        for card in self.cards:
            name = card.lable.text().strip().lower()

            if text == "" or text in name:
                card.show()
                self.lay.addWidget(card, row, col)
                col += 1
                if col >= max_columns:
                    col = 0
                    row += 1
            else:
                card.hide()

            

        
class Product_card2(QFrame):
    def __init__(self,text,price,amount,_id,color="blue",parent_lay=None):
        super().__init__()
        self.text=text
        self.price=price
        self.amount=amount
        self._id=_id
        self.parent_lay=parent_lay
        self.vlay=QVBoxLayout()
        self.setFixedSize(210,200)
        self.setStyleSheet(f"background-color:{color};border-radius:10;border:2px solid black")
        self.setLayout(self.vlay)
        self.lable=QLabel(str(self.text))
        self.lable.setStyleSheet("font-size:25px;font-weight:bold;color:white;max-height:30;border:none")
        self.price_holder=editline(width=100)
        self.price_holder.setPlaceholderText("السعر")
        self.price_holder.setText(str(self.price))
        self.price_holder.setDisabled(True)
        self.amount_holder=editline("100")
        self.amount_holder.setPlaceholderText("الكمية")
        self.amount_holder.setText(str(self.amount))
        self.amount_holder.setDisabled(True)
        self.price_holder.setClearButtonEnabled(False)
        self.price_holder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.amount_holder.setClearButtonEnabled(False)
        self.amount_holder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bt1=Button("SELL",hight=20,width=100,bg_color="red",hovercolor="darkred",border="black",hover_border="black",text_color="white")
        self.bt2=Button("EDIT",hight=20,width=100,bg_color="lime",hovercolor="darkorange",border="black",hover_border="black",text_color="white")
        self.bt3=Button("+ BUY",hight=20,width=100,bg_color="lime",hovercolor="green",border="black",hover_border="black",text_color="white")
        self.check=QCheckBox("الحذف")
        self.hlay=QHBoxLayout()
        self.hlay.addWidget(self.bt1,alignment=Qt.AlignmentFlag.AlignLeft)
        self.hlay.addWidget(self.bt2,alignment=Qt.AlignmentFlag.AlignRight)
        self.vlay.addWidget(self.lable,alignment=Qt.AlignmentFlag.AlignHCenter)
        self.vlay.addWidget(self.price_holder,alignment=Qt.AlignmentFlag.AlignHCenter)
        self.vlay.addWidget(self.amount_holder,alignment=Qt.AlignmentFlag.AlignHCenter)
        self.vlay.addWidget(self.bt3)
        self.bt3.clicked.connect(self.edit)
        
        
    
            
    def edit(self):
        db1 = sqlite3.connect("Data.db")
        cr1 = db1.cursor()

        cr1.execute("SELECT admin FROM temp LIMIT 1")
        row = cr1.fetchone()
        if row is not None and row[0] == 1:
            global admin_id
            admin_id = True
        if admin_id:
            self.bt3.setDisabled(False)
            self.edit_window=QMdiSubWindow()
            self.edit_window.setWindowTitle("Buy")
            self.edit_window.setStyleSheet("background-color:white")
            self.edit_window.setFixedSize(600,300)
            self.Edit_lay=QVBoxLayout()
            self.widget=QWidget()
            self.widget.setLayout(self.Edit_lay)
            self.edit_window.setWidget(self.widget)
            self.line4=editline(width=150)
            self.line4.setPlaceholderText("Enter Amount")
            self.bt3=Button("Save")
            self.Edit_lay.addWidget(self.line4,alignment=Qt.AlignmentFlag.AlignHCenter)
            self.Edit_lay.addWidget(self.bt3,alignment=Qt.AlignmentFlag.AlignHCenter)
            self.edit_window.show()
            self.bt3.clicked.connect(self.save)
            
    def save(self):

        amount_text = self.line4.text().strip()

        # هنبدأ بـ id بس
        data = {
            "id": self._id,
        }

        if amount_text != "":
            if not amount_text.isdigit():
                msg = QMessageBox(text="❌ الكمية لازم تكون رقم صحيح")
                msg.exec()
                return
            data["amount"] = int(amount_text)

        # لو مفيش أي تعديل (id بس)
        if len(data) == 1:
            msg = QMessageBox(text="⚠️ مفيش أي تعديل حصل")
            msg.exec()
            return

        try:
            msg=QMessageBox(text=f"Total Price:  {float(self.price_holder.text())*int(self.line4.text())}\nهل تريد الشراء؟")
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            result=msg.exec()
            if result==QMessageBox.Yes:
                
                r = requests.post("http://127.0.0.1:8000/products/update/buy", json=data)
                print("UPDATE response:", r.status_code, r.text)  # شوف في التيرمنال لو في مشكلة

                res = r.json()
                if res.get("status") == "ok":
                    # مهم: ننادي grid على ال object مش على الكلاس
                    if hasattr(self, "parent_lay") and self.parent_lay is not None:
                        self.parent_lay.grid()
                    self.edit_window.hide()
                else:
                    msg = QMessageBox(text="❌ Error في التعديل")
                    msg.exec()
            else:
                pass
        except Exception as e:
            msg = QMessageBox(text=f"❌Error\n{str(e)}")
            msg.exec()

    