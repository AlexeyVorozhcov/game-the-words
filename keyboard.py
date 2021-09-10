from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject
from hidden_word import preparation_letter
"""
Открытые методы:
    - создать объект
    - назначить внешний слот для сигнала clicked
    - обновить все кнопки

"""

class Keyboard(QObject):
    def __init__(self, ui):
        """
        Создается объект Клавиатура. Принимает на вход список с объектами-кнопками.
        """
        QObject.__init__(self)
        self.ui = ui
        self.buttons = self._generate_list() # список объектов-кнопок
        self.internal_slot = self._clicked # внутренний слот для кликов по кнопкам
        self._set_clicked_connects() 
        self.external_slot = None # внешний слот для кликов по кнопкам
    
    def _generate_list(self):
        """
        Возвращает сгенерированный из ui список объектов-кнопок
        """
        return self.ui.keyboard.findChildren(QtWidgets.QPushButton)

    def _set_clicked_connects(self):
        """
        Присоединяет слот к каждой кнопке
        """
        for btn in self.buttons:
            btn.clicked.connect(self.internal_slot) 

    def _clicked(self):
        """
        Внутренний слот для кликов по кнопкам
        Определяет вызвавший объект
        Запускает внешний слот, передает ему текст на вызвавшей кнопке
        """
        sender = self.sender()
        self.external_slot(sender.text())
        sender.setEnabled(False)
   
    def set_external_slot(self, command):
        """
        Устанавливает внешний слот для кликов по кнопкам
        Принимает на вход метод, который будет являться внешним слотом
        """
        self.external_slot = command    

    def update(self):
        """
        Включает все кнопки
        """
        for btn in self.buttons:
            btn.setEnabled(True)

    def all_buttons_off(self):
        """
        Выключает все кнопок
        """
        for btn in self.buttons:
            btn.setEnabled(False)

    def _find_btn_on_text(self, text):
        """
        Ищет кнопки с текстом text
        """  
        for btn in self.buttons:
            if preparation_letter(btn.text())== preparation_letter(text):
                return btn  

    def one_letter_off(self, text):
        """
        Отключает на клавиатуре одну кнопку, на которой есть text
        """
        btn = self._find_btn_on_text(text)
        if btn: btn.setEnabled(False)
        


   


