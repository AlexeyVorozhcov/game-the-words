from PyQt5.QtWidgets import QPushButton
from setting import * 


class Button:
    def __init__(self, btn : QPushButton, text=""):
        self.btn = btn
        self.btn.setText(text) 

    def connect_script(self, script):     
        self.btn.clicked.connect(script)

    def on(self):
        self.btn.setEnabled(True)

    def off(self):
        self.btn.setEnabled(False)
        
 

        