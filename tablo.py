from math import floor

"""
Открытые методы:
    - Создать табло
    - Отобразить слово
    - Очистить табло
"""
MAX_LEN = 17
CENTER_POS = 9

class Tablo:
    def __init__(self, ui):
        self.ui = ui
        self.letters = []
        self._generate_list()
        self.clear()

    def _generate_list(self):
        """
        Добавляет в список объекты табло
        """
        self.letters.append(self.ui.w1)
        self.letters.append(self.ui.w2)
        self.letters.append(self.ui.w3)
        self.letters.append(self.ui.w4)
        self.letters.append(self.ui.w5)
        self.letters.append(self.ui.w6)
        self.letters.append(self.ui.w7)
        self.letters.append(self.ui.w8)
        self.letters.append(self.ui.w9)
        self.letters.append(self.ui.w10)
        self.letters.append(self.ui.w11)
        self.letters.append(self.ui.w12)
        self.letters.append(self.ui.w13)
        self.letters.append(self.ui.w14)
        self.letters.append(self.ui.w15)
        self.letters.append(self.ui.w16)
        self.letters.append(self.ui.w17)

    def clear(self):
        """
        Очищает табло
        """
        for letter in self.letters:
            letter.setVisible(False)
            letter.setText("")    

    def show_word(self, word):
        """
        Отображает слово в табло
        """
        len_word = len(word)
        if len_word>0:
            start_pos = CENTER_POS - floor(len_word/2)
            end_pos = start_pos + len_word -1
            number_of_letter = 0
            for i in range(start_pos-1, end_pos):
                self.letters[i].setVisible(True)
                self.letters[i].setText(word[number_of_letter])
                number_of_letter += 1        