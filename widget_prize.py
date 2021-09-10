from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QPushButton, QPushButton, QSizePolicy
from PyQt5.QtCore import QSize, Qt 
from PyQt5.QtGui import QIcon

BTN_WIDTH = 100
BTN_HEIGHT = 100
ICON_SIZE = QSize(90,90)
EXTENDED = QSizePolicy.Policy.Expanding
FIXED = QSizePolicy.Policy.Fixed
LABEL_BAYED = "КУПЛЕНО"

class DatasOfPrize:
    def __init__(self, image_file, name, price) -> None:
        self.image_file = image_file
        self.name = name
        self.price = price 

class Prize(QWidget):
    def __init__(self, datas_of_prize:DatasOfPrize):
        QWidget.__init__(self)
        self.vbox = QVBoxLayout()
        self.vbox.setSpacing(1) 
        self.btn = QPushButton()
        self.btn.setFixedWidth(BTN_WIDTH)
        self.btn.setFixedHeight(BTN_HEIGHT)
        # self.btn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.btn.setIcon(QIcon(datas_of_prize.image_file))
        self.btn.setIconSize(ICON_SIZE)
        self.btn.setText("")
        self.btn.setFlat(True)
                
        self.lbl = QLabel()
        self.setName(str(datas_of_prize.name))
        self.lbl.setSizePolicy (EXTENDED, EXTENDED)
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.lbl2 = QLabel()
        self.setPrice(str(datas_of_prize.price))
        self.lbl2.setSizePolicy (EXTENDED, EXTENDED)
        self.lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox.addWidget(self.btn)
        self.vbox.addWidget(self.lbl)
        self.vbox.addWidget(self.lbl2)
        self.setLayout(self.vbox)

    def off(self):
        self.btn.setEnabled(False)

    def on(self):
        self.btn.setEnabled(True) 

    def setName(self, name):
        self.lbl.setText(name)  
    
    def setPrice(self, price):
        self.lbl2.setText(price)

    def setBuyed(self):
        self.setPrice(LABEL_BAYED)    


