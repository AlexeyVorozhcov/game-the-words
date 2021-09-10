from setting import TEXTBUTTON_FIRST_AND_LAST_LETTER, TEXTBUTTON_ONE_RANDOM_LETTER, TEXTBUTTON_OPEN_ALL_VOWELS, TEXTBUTTON_SHOW_DEFINITION
from PyQt5 import QtWidgets
import win
import tablo
import keyboard
import buttons
import my_animation
from setting import SPEED_ANIMATION_GOLD
from widget_prize import Prize, DatasOfPrize

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() # инициализация главного окна
        self.ui = win.Ui_MainWindow() # объект с интерфейсом
        self.ui.setupUi(self) # инициализация интерфейса
        self.keyboard = keyboard.Keyboard(self.ui)
        self.tablo = tablo.Tablo(self.ui)
        self.btn_showDefinition = buttons.Button(self.ui.pushButton_show_definition, TEXTBUTTON_SHOW_DEFINITION)
        self.btn_nextWord = buttons.Button(self.ui.pushButton_next_word)
        self.btn_oneRandomLetter = buttons.Button(self.ui.pushButton_help1, TEXTBUTTON_ONE_RANDOM_LETTER)
        self.btn_firstAndLastLetter = buttons.Button(self.ui.pushButton_help2, TEXTBUTTON_FIRST_AND_LAST_LETTER)
        self.btn_openAllVowels = buttons.Button(self.ui.pushButton_help3, TEXTBUTTON_OPEN_ALL_VOWELS)

        list = []
        num = 0
        for i in range(3):
            for j in range(8):
                list.append(Prize(DatasOfPrize("glasn.png", "Умная сова", 1000*i)))
                self.ui.gridLayout_prizes.addWidget(list[num], i, j)
                num +=1



    def connect_with_btn_showDefinition(self, script):
        """
        Присоединяет скрипт к кнопке "Показать определение"
        """
        self.btn_showDefinition.connect_script(script)

    def connect_with_btn_nextWord(self, script):
        """
        Присоединяет скрипт к кнопке "Next"
        """
        self.btn_nextWord.connect_script(script)    

    def connect_with_btn_oneRandomLetter(self, script):
        """
        Присоединяет скрипт к кнопке "Открыть одну случайную букву"
        """
        self.btn_oneRandomLetter.connect_script(script)    
    
    def connect_with_btn_firstAndLastLetter(self, script):
        """
        Присоединяет скрипт к кнопке "Открыть первую и последнюю буквы"
        """
        self.btn_firstAndLastLetter.connect_script(script)     

    def connect_with_btn_openAllVowels(self, script):
        """
        Присоединяет скрипт к кнопке "Открыть все"
        """
        self.btn_openAllVowels.connect_script(script)              

    def connect_with_btns_keyboard(self, command):
        """
        Присоединяет скрипт к буквенным кнопкам
        """
        self.keyboard.set_external_slot(command)

    def show_definition(self, definition):
        """
        Помещает текст в поле textEdit_definition (опредедение слова)
        """
        self.ui.label_definition.setVisible(True)
        self.ui.label_definition.setText(definition)  

    def hide_definition(self):
        """
        Очищает поле textEdit_definition (опредедение слова)
        """
        self.ui.label_definition.setVisible(False)
        self.ui.label_definition.setText("")

    def set_round_goal(self, goal):
        """
        Помещает текст в поле label_round_goal (цель раунда)
        """        
        pass

    def set_name_gamer(self, name):
        """
        Помещает текст в поле label_name_gamer (имя игрока)
        """        
        self.ui.label_name_gamer.setText(str(name))
        self.ui.tabWidget.setTabText(0, name)           

    def set_text_in_dialog(self, text):
        """
        Вставляет текст в поле Диалог
        """        
        self.ui.label_dialog.setText(text)  

    def set_balance_gold(self, balance):
        """
        Вставляет текст в поле Баланс золота
        """    
        self.ui.label_balance_gold.setText(str(balance))

    def animation_balance_gold(self, bal_old, bal_new):
        """
        Запускает анимацию изменения значения в поле Баланс золота
        """            
        step = 0
        if bal_old<bal_new: step = 1
        else:step = -1
        self.a = my_animation.Animation(range(bal_old, bal_new+step, step), self.set_balance_gold, SPEED_ANIMATION_GOLD)  

    def restart(self):
        """
        Очищает все поля для новой игры
        """    
        self.keyboard.update()
        self.hide_definition()    
        self.btn_nextWord.off()
        self.btn_showDefinition.on()  
        self.btn_oneRandomLetter.on() 
        self.btn_firstAndLastLetter.on()
        self.btn_openAllVowels.on()
        
    def all_buttons_off(self):
        """
        Делает все кнопки неактивными (кроме Next)
        """
        self.btn_showDefinition.off()  
        self.btn_oneRandomLetter.off() 
        self.btn_firstAndLastLetter.off()
        self.btn_openAllVowels.off()
        self.keyboard.all_buttons_off()





def test_print(letter):
    print(letter)

def print_repeat_letter():
    print("Такую букву уже называли!")

def print_letter_not_found():
    print("Такой буквы в этом слове нет...")  

def print_starting_game():
    print(f"Я загадал слово из ... букв:")

def input_letter():
    return input("Введите букву: ")

def print_letter_is_found():
    print("-"*10)
    print("Есть такая буква!")

def print_letter_is_many():
    print("Таких букв тут несколько! Круто!")    

def print_hidden_word(word):
    print(word)
    print("-"*10)

def print_win():
    print ("ПОБЕДА!!!")

def print_error_letter():
    print("Введена некорректная буква.")    

def print_massage(mode):
    if mode==-2: print_error_letter()
    if mode==-1: print_repeat_letter()
    elif mode==0: print_letter_not_found()
    elif mode==1: print_letter_is_found()
    elif mode>1: print_letter_is_many()

