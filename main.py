from PyQt5 import QtGui
from hidden_word import HiddenWord
import interface
from setting import * 
from gamer import Gamer, get_gamer 
from PyQt5.QtMultimedia import QSound

app = interface.QtWidgets.QApplication([])
win = interface.MainWindow()
win.show()

sound = QSound(join(FOLDER_SOUND_FILES,"test.wav"))

class Game:
    def __init__(self, gamer : Gamer):
        """
        Создание игорового процесса
        """
        self.gamer = gamer
        self.hidden_word = None
        self.word_off = None
        self.round_off = None
        self.start_new_round()
  
    def start_new_round(self):
        """
        Запуск нового раунда
        """
        self.round_off = False
        round = self.gamer.numberRound
        win.set_round_goal(500)
        win.set_name_gamer(self.gamer.name)
        self.start_new_word()

    def start_new_word(self):
        """
        Запуск нового слова
        """
        self.word_off = False 
        win.set_text_in_dialog("Отгадай слово")
        self.hidden_word = HiddenWord()
        win.tablo.clear()
        win.tablo.show_word(self.hidden_word.get())
        win.set_balance_gold(self.gamer.balance_gold)
        win.restart() 
     
    def turn(self, letter):
        """
        Метод-слот для кликов по буквенным кнопкам в игре
        Обработка кликов по кнопкам с буквам, один клик - это один ход игры
        На вход получает букву
        """
        if self.word_off: # слово уже разгадано, дальше ничего делать не нужно   
            return None 
        result_of_turn = self.hidden_word.is_letter_here(letter) # есть такая буква в слове?
        sound.play()
        if result_of_turn==0:  # буквы в слове нет
            self.gamer.transaction_gold(PRICE_PUSH_LETTER, ) # расплата за ошибку
        if result_of_turn>0:  # буква в слове есть
            self.gamer.transaction_gold(PRICE_OPEN_LETTER*result_of_turn) # награда, умноженная на количество букв
        win.tablo.show_word(self.hidden_word.get())
        interface.print_massage(result_of_turn)
        if self.hidden_word.is_solved(): # слово разгадано?
            self.word_off = True
            win.all_buttons_off()
            win.set_text_in_dialog("Отлично! Давай дальше!")
            win.btn_nextWord.on()

    def click_to_showDefinition(self):
        """
        Клик по кнопке "Показать определение"
        """
        win.show_definition(self.hidden_word.get_definition())
        self.gamer.transaction_gold(PRICE_SHOW_DEFINITION) 
        win.btn_showDefinition.off()

    def click_to_nextWord(self):
        """
        Клик по кнопке "Next"
        """
        self.start_new_word() 

    def click_to_open_random_letter(self):
        """
        Клик по кнопке "Открыть одну случайную букву"
        """
        letter = self.hidden_word.get_one_random_letter()
        self.turn(letter)
        win.keyboard.one_letter_off(letter) 
        self.gamer.transaction_gold(PRICE_ONE_RANDOM_LETTER)
        win.btn_oneRandomLetter.off()     

    def click_to_open_first_and_last_letter(self):
        """
        Клик по кнопке "Открыть первую и последнюю буквы"
        """
        letter = self.hidden_word.get_first_letter()
        self.turn(letter)
        win.keyboard.one_letter_off(letter)
        letter = self.hidden_word.get_last_letter()
        self.turn(letter)
        win.keyboard.one_letter_off(letter)
        self.gamer.transaction_gold(PRICE_FIRST_AND_LAST_LETTER)
        win.btn_firstAndLastLetter.off()

    def click_to_openAllVowels(self):
        """
        Клик по кнопке "Открыть все гласные"
        """
        self.gamer.transaction_gold(PRICE_OPEN_ALL_VOWELS)
        list_of_vowels = self.hidden_word.get_allVowels()
        for letter in list_of_vowels:
            self.turn(letter)
            win.keyboard.one_letter_off(letter)
        win.btn_openAllVowels.off()
        



gamer = get_gamer()
gamer.set_script_of_animation(win.animation_balance_gold)
current_round = gamer.numberRound
game = Game(gamer)
win.connect_with_btn_showDefinition(game.click_to_showDefinition)
win.connect_with_btn_nextWord(game.click_to_nextWord)
win.connect_with_btn_oneRandomLetter(game.click_to_open_random_letter)
win.connect_with_btn_firstAndLastLetter(game.click_to_open_first_and_last_letter)
win.connect_with_btn_openAllVowels(game.click_to_openAllVowels)
win.connect_with_btns_keyboard(game.turn)



exit(app.exec())    
    





  
