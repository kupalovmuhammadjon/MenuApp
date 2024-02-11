import pathlib
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal
import sys  
import os
is_plus = True
class CardWindow(QMainWindow):
    total_updated = pyqtSignal(int)

    def __init__(self, name, price, imageurl, total_callback):
        super().__init__()
        self.imageurl = imageurl
        self.name = name
        self.price = price
        self.is_plus = True
        self.sum = 0
        self.total_callback = total_callback
        self.setMinimumSize(155, 180)
        self.setMaximumSize(155, 180)
        self.setStyleSheet("""color: black; background-color: #D9D9D9""")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        cardlayout = QVBoxLayout(central_widget)
        cardlayout.setContentsMargins(0, 0, 0, 0)
        innerwin = QWidget()
        cardlayout.addWidget(innerwin)
        
        plvbtn = QPushButton(innerwin)
        plvbtn.setGeometry(0, 0, 155, 140)
        plvbtn.setStyleSheet(f"""
            QPushButton {{
                background-image: url({imageurl});
                border-bottom-left-radius: 5px;
                border-bottom-right-radius: 5px;
            }}
        """)

        backbtn = QPushButton(innerwin)
        backbtn.setGeometry(0, 130, 155, 40)
        backbtn.setText(f"{name} {str(price)}")
        backbtn.setFont(QFont("Montserrat", 6, weight=60))
        backbtn.setStyleSheet("""
            QPushButton {
                background-color: #FF5D5D;
                border-top-left-radius: 0px;
                border-top-right-radius: 0px;
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
                padding-left: 4px;
                text-align: left;
            }
        """)

        self.count = QLabel(innerwin)
        self.count.setGeometry(112, 140, 22, 18)
        self.count.setText("0")
        self.count.setStyleSheet("""color: black; background-color: rgba(255, 93, 93, 255)""")
        self.count.setFont(QFont("Montserrat", 7, weight=75))
        
        minusbtn = QPushButton(innerwin)
        minusbtn.setGeometry(85, 140, 20, 20)
        minusbtn.setText("-")
        minusbtn.setFont(QFont("Montserrat", 6, weight=75))
        minusbtn.setStyleSheet("""
            QPushButton {
                background-color: #47D230;
                border-radius: 10px;
                text-align: center;
            }
        """)
        minusbtn.clicked.connect(self.minus)
        
        plusbtn = QPushButton(innerwin)
        plusbtn.setGeometry(132, 140, 20, 20)
        plusbtn.setText("+")
        plusbtn.setFont(QFont("Montserrat", 6, weight=75))
        plusbtn.setStyleSheet("""
            QPushButton {
                background-color: #47D230;
                border-radius: 10px;
                text-align: center;
            }
        """)
        plusbtn.clicked.connect(self.plus)
        
        
        self.show()
        
    
    def update_total(self):
        if self.is_plus:
            self.total_callback(self.sum, self.price, self.is_plus)
        else:
            self.total_callback(-self.sum, self.price, self.is_plus)
        self.total_updated.emit(self.sum)

    def minus(self):
        if int(self.count.text()) > 0:
            self.count.setText(str(int(self.count.text()) - 1))
            self.sum = self.sum - self.price
            self.is_plus = False
            self.update_total()

    def plus(self):
        self.count.setText(str(int(self.count.text()) + 1))
        self.sum = self.sum + self.price
        self.is_plus = True
        self.update_total()


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.resize(1920, 1080)
        self.setMinimumSize(1920, 1080) 
        self.setStyleSheet("""
            background-color: #FF5D5D;
        """)
        
        self.path = str(pathlib.Path().resolve() / "/")
        print(self.path)    
        self.total = 0

        nationalMeals = QWidget(self)
        nationalMeals.setGeometry(35, 20, 900, 440)
        nationalMeals.setStyleSheet("""
            background-color: #D9D9D9;
            border-radius: 40px;
        """)

        foreignMeals = QWidget(self)
        foreignMeals.setGeometry(980, 20, 900, 440)
        foreignMeals.setStyleSheet("""
            background-color: #D9D9D9;
            border-radius: 40px;
        """)

        deserts = QWidget(self)
        deserts.setGeometry(35, 490, 900, 440)
        deserts.setStyleSheet("""
            background-color: #D9D9D9;
            border-radius: 40px;
        """)

        drinks = QWidget(self)
        drinks.setGeometry(980, 490, 900, 440)
        drinks.setStyleSheet("""
            background-color: #D9D9D9;
            border-radius: 40px;
        """)

        def create_button(parent_widget, text):
            button = QPushButton(text, parent_widget)
            button.setGeometry(300, 0, 300, 50)
            button.setFont(QFont("Montserrat", 12, weight=70))
            button.setStyleSheet("""
                background-color: #FF5D5D;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;       
            """)
            return button

        # National meals
        nmealsbtn = create_button(nationalMeals, "National Meals")
        
        winnmhl1 = QWidget(nationalMeals)
        winnmhl1.setGeometry(15, 50, 880, 200)
        nmhl1 = QHBoxLayout(winnmhl1)
        nmhl1.setContentsMargins(0, 0, 0, 0)
        palovCard = CardWindow("PALOV", 25000, f"{self.path}palov.png", self.newTotal)
        palovCard2 = CardWindow("MANTI", 35000, f"{self.path}manti.png", self.newTotal)
        palovCard3 = CardWindow("SHASHLIK\n", 12000, f"{self.path}shashlik.png", self.newTotal)
        palovCard4 = CardWindow("BARAK\n", 45000, f"{self.path}barak.png", self.newTotal)
        palovCard5 = CardWindow("Sho'rva\n", 25000, f"{self.path}shorva.png", self.newTotal)
        nmhl1.addWidget(palovCard)
        nmhl1.addWidget(palovCard2)
        nmhl1.addWidget(palovCard3)
        nmhl1.addWidget(palovCard4)
        nmhl1.addWidget(palovCard5)
        
        winnmhl2 = QWidget(nationalMeals)
        winnmhl2.setGeometry(15, 250, 880, 200)
        
        nmhl1 = QHBoxLayout(winnmhl2)
        nmhl1.setContentsMargins(0, 0, 0, 0)
        palovCard = CardWindow("PALOV", 25000, f"{self.path}palov.png", self.newTotal)
        palovCard2 = CardWindow("PALOV", 25000, f"{self.path}palov.png", self.newTotal)
        palovCard3 = CardWindow("PALOV", 25000, f"{self.path}palov.png", self.newTotal)
        palovCard4 = CardWindow("PALOV", 25000, f"{self.path}palov.png", self.newTotal)
        palovCard5 = CardWindow("PALOV", 25000, f"{self.path}palov.png", self.newTotal)
        nmhl1.addWidget(palovCard)
        nmhl1.addWidget(palovCard2)
        nmhl1.addWidget(palovCard3)
        nmhl1.addWidget(palovCard4)
        nmhl1.addWidget(palovCard5)

        # Foreign meals
        fmealsbtn = create_button(foreignMeals, "Foreign Meals")
        
        winnmhl1 = QWidget(foreignMeals)
        winnmhl1.setGeometry(15, 50, 880, 200)
        nmhl1 = QHBoxLayout(winnmhl1)
        nmhl1.setContentsMargins(0, 0, 0, 0)
        sushiCard = CardWindow("SUSHI", 54000, f"{self.path}sushi.png", self.newTotal)
        sushiCard2 = CardWindow("SUSHI", 54000, f"{self.path}sushi.png", self.newTotal)
        sushiCard3 = CardWindow("SUSHI", 54000, f"{self.path}sushi.png", self.newTotal)
        sushiCard4 = CardWindow("SUSHI", 54000, f"{self.path}sushi.png", self.newTotal)
        sushiCard5 = CardWindow("SUSHI", 54000, f"{self.path}sushi.png", self.newTotal)
        nmhl1.addWidget(sushiCard)
        nmhl1.addWidget(sushiCard2)
        nmhl1.addWidget(sushiCard3)
        nmhl1.addWidget(sushiCard4)
        nmhl1.addWidget(sushiCard5)
        
        winnmhl2 = QWidget(foreignMeals)
        winnmhl2.setGeometry(15, 250, 880, 200)
        
        nmhl1 = QHBoxLayout(winnmhl2)
        nmhl1.setContentsMargins(0, 0, 0, 0)
        sushiCard = CardWindow("SUSHI", 54000, f"{self.path}sushi.png", self.newTotal)
        sushiCard2 = CardWindow("SUSHI", 54000, f"{self.path}sushi.png", self.newTotal)
        sushiCard3 = CardWindow("SUSHI", 54000, f"{self.path}sushi.png", self.newTotal)
        sushiCard4 = CardWindow("SUSHI", 54000, f"{self.path}sushi.png", self.newTotal)
        sushiCard5 = CardWindow("SUSHI", 54000, f"{self.path}sushi.png", self.newTotal)
        nmhl1.addWidget(sushiCard)
        nmhl1.addWidget(sushiCard2)
        nmhl1.addWidget(sushiCard3)
        nmhl1.addWidget(sushiCard4)
        nmhl1.addWidget(sushiCard5)

        # Desserts
        desertsbtn = create_button(deserts, "Desserts")
        
        winnmhl1 = QWidget(deserts)
        winnmhl1.setGeometry(15, 50, 880, 200)
        nmhl1 = QHBoxLayout(winnmhl1)
        nmhl1.setContentsMargins(0, 0, 0, 0)
        pieCard = CardWindow("CHOCO \nPIE", 11000, f"{self.path}pie.png", self.newTotal)
        pieCard2 = CardWindow("CHOCO \nPIE", 11000, f"{self.path}pie.png", self.newTotal)
        pieCard3 = CardWindow("CHOCO \nPIE", 11000, f"{self.path}pie.png", self.newTotal)
        pieCard4 = CardWindow("CHOCO \nPIE", 11000, f"{self.path}pie.png", self.newTotal)
        pieCard5 = CardWindow("CHOCO \nPIE", 11000, f"{self.path}pie.png", self.newTotal)
        nmhl1.addWidget(pieCard)
        nmhl1.addWidget(pieCard2)
        nmhl1.addWidget(pieCard3)
        nmhl1.addWidget(pieCard4)
        nmhl1.addWidget(pieCard5)
        
        winnmhl2 = QWidget(deserts)
        winnmhl2.setGeometry(15, 250, 880, 200)
        
        nmhl1 = QHBoxLayout(winnmhl2)
        nmhl1.setContentsMargins(0, 0, 0, 0)
        pieCard = CardWindow("CHOCO \nPIE", 11000, f"{self.path}pie.png", self.newTotal)
        pieCard2 = CardWindow("CHOCO \nPIE", 11000, f"{self.path}pie.png", self.newTotal)
        pieCard3 = CardWindow("CHOCO \nPIE", 11000, f"{self.path}pie.png", self.newTotal)
        pieCard4 = CardWindow("CHOCO \nPIE", 11000, f"{self.path}pie.png", self.newTotal)
        pieCard5 = CardWindow("CHOCO \nPIE", 11000, f"{self.path}pie.png", self.newTotal)
        nmhl1.addWidget(pieCard)
        nmhl1.addWidget(pieCard2)
        nmhl1.addWidget(pieCard3)
        nmhl1.addWidget(pieCard4)
        nmhl1.addWidget(pieCard5)

        # Drinks
        drinksbtn = create_button(drinks, "Drinks")
        
        winnmhl1 = QWidget(drinks)
        winnmhl1.setGeometry(15, 50, 880, 200)
        nmhl1 = QHBoxLayout(winnmhl1)
        nmhl1.setContentsMargins(0, 0, 0, 0)
        chortoqCard = CardWindow("CHORTOQ\n", 9900, f"{self.path}chortoq.png", self.newTotal)
        chortoqCard2 = CardWindow("CHORTOQ\n", 9900, f"{self.path}chortoq.png", self.newTotal)
        chortoqCard3 = CardWindow("CHORTOQ\n", 9900, f"{self.path}chortoq.png", self.newTotal)
        chortoqCard4 = CardWindow("CHORTOQ\n", 9900, f"{self.path}chortoq.png", self.newTotal)
        chortoqCard5 = CardWindow("CHORTOQ\n", 9900, f"{self.path}chortoq.png", self.newTotal)
        nmhl1.addWidget(chortoqCard)
        nmhl1.addWidget(chortoqCard2)
        nmhl1.addWidget(chortoqCard3)
        nmhl1.addWidget(chortoqCard4)
        nmhl1.addWidget(chortoqCard5)
        
        winnmhl2 = QWidget(drinks)
        winnmhl2.setGeometry(15, 250, 880, 200)
        
        nmhl1 = QHBoxLayout(winnmhl2)
        nmhl1.setContentsMargins(0, 0, 0, 0)
        chortoqCard = CardWindow("CHORTOQ\n", 9900, f"{self.path}chortoq.png", self.newTotal)
        chortoqCard2 = CardWindow("CHORTOQ\n", 9900, f"{self.path}chortoq.png", self.newTotal)
        chortoqCard3 = CardWindow("CHORTOQ\n", 9900, f"{self.path}chortoq.png", self.newTotal)
        chortoqCard4 = CardWindow("CHORTOQ\n", 9900, f"{self.path}chortoq.png", self.newTotal)
        chortoqCard5 = CardWindow("CHORTOQ\n", 9900, f"{self.path}chortoq.png", self.newTotal)
        nmhl1.addWidget(chortoqCard)
        nmhl1.addWidget(chortoqCard2)
        nmhl1.addWidget(chortoqCard3)
        nmhl1.addWidget(chortoqCard4)
        nmhl1.addWidget(chortoqCard5)

        jamilbl = QLabel("Jami:", self)
        jamilbl.setGeometry(35, 942, 65, 20)
        jamilbl.setFont(QFont("Montserrat", 12, weight=70))
        
        self.totalAmout = QLabel("0", self)
        self.totalAmout.setGeometry(105, 942, 200, 20)
        self.totalAmout.setFont(QFont("Montserrat", 12, weight=70))
        
        orderbtn = QPushButton("Buyurtma qilish", self)
        orderbtn.setGeometry(1670, 942, 220, 30)
        orderbtn.setFont(QFont("Montserrat", 12, weight=70))
        orderbtn.setStyleSheet("""
                background-color: #D9D9D9;
                border-radius: 15px;       
            """) 
        
        orderbtn.clicked.connect(lambda: self.orderMessageBox())

        self.show()

    def orderMessageBox(self):
        if self.total > 0:
            mbox = QMessageBox(self)
            mbox.setIcon(QMessageBox.Information)
            mbox.setWindowTitle("Yoqimli ishtaha")
            mbox.setText("Buyurmangiz qabul qilib olindi!")
            mbox.exec_()
        else:
            mbox = QMessageBox(self)
            mbox.setIcon(QMessageBox.Warning)
            mbox.setWindowTitle("Blanck")
            mbox.setText("Hali hech narsa tanlamadingiz!")
            mbox.exec_()
            
        
    def newTotal(self, card_sum, pr, is_plus):  
        if is_plus:
            self.total -= card_sum - pr
            self.total += card_sum
        else:
            self.total -= pr
        self.totalAmout.setText(str(self.total))
        
        


if __name__ == "__main__":
    app = QApplication([])
    menu = Menu()
    sys.exit(app.exec_())
