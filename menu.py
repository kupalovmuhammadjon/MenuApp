from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal
import cardView
import sys
total = 0
menu = None

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.resize(1920, 1080)
        self.setMinimumSize(1920, 1080) 
        self.setStyleSheet("""
            background-color: #FF5D5D;
        """)

        
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
            button.setFont(QFont("Montserrat", 12, weight=70))  # Choose a suitable font
            button.setStyleSheet("""
                background-color: #FF5D5D;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;       
            """)
            return button

        # National meals
        nmealsbtn = create_button(nationalMeals, "National Meals")
        
        nmhl1 = QHBoxLayout(nationalMeals)
        nmhl1.setContentsMargins(0, 0, 0, 0)
        palovCard = cardView.CardWindow("PALOV", 25000, "D:/codes/menu/palov.png")
        palovCard2 = cardView.CardWindow("PALOV", 25000, "D:/codes/menu/palov.png")
        nmhl1.addWidget(palovCard)
        nmhl1.addWidget(palovCard2)
        
        


        # Foreign meals
        fmealsbtn = create_button(foreignMeals, "Foreign Meals")

        # Desserts
        desertsbtn = create_button(deserts, "Desserts")

        # Drinks
        drinksbtn = create_button(drinks, "Drinks")

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
        
        self.show()
        

        
    def newTotal(self):
        self.totalAmout.setText(str(total))

             
        
if __name__ == "__main__":
    app = QApplication([])
    menu = Menu()
    sys.exit(app.exec_())
        
    
