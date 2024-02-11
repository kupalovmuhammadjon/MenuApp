from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import menu 

class CardWindow(QMainWindow):
    def __init__(self, name, price, imageurl):
        super().__init__()
        self.imageurl = imageurl
        self.name = name
        self.price = price
        self.sum = 0
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
        
       
    def minus(self):
        if int(self.count.text()) > 0:
            self.count.setText(str(int(self.count.text()) - 1))
        self.sum = int(self.count.text()) * self.price
        menu.total = self.sum
        menu.changeTotal()
        
        
    def plus(self):
        self.count.setText(str(int(self.count.text()) + 1))
        self.sum = int(self.count.text()) * self.price
        menu.total = self.sum
        menu.changeTotal()
        
        


