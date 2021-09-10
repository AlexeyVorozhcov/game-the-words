from words import get_word_and_definition
from random import choice

SIMBOL_HIDDEN = "*"
MAX_LEN = 17
MAX_LEN_DEFINITION = 180
ABC = "ёйцукенгшщзхъэждлорпавыфячсмитьбю"
VOWELS = "уеёэоаыяию"
WORDSFILTER = [" к сущ.", "То же, что", "по знач.", "То же, что", "см. ", "секс", "полов", "порно", "влагалище" ]

class HiddenWord:
    def __init__(self):
        """
        При создании объекта создаются данные:
        _WORD - загаданное слово,
        _DEFINITION - определение слова (для подсказки)
         """
        while True:
            self._WORD, self._DEFINITION = get_word_and_definition()
            if self._is_len_ok() and self._is_len_definition_ok() and self._is_matches_the_filter(): break
        self._played_letters = []

    def _is_len_ok(self):
        """
        Возвращает True, если длина слова меньше или равна максимальной длине MAX_LEN
        """
        if len(self._WORD)<=MAX_LEN: return True
        else: return False
    
    def _is_len_definition_ok(self):
        """
        Возвращает True, если длина определения меньше или равна максимальной длине MAX_LEN_DEFINITION
        """
        if len(self._DEFINITION)<=MAX_LEN_DEFINITION: return True
        else: return False

    def _is_matches_the_filter(self):
        """
        Если в слове или определении нет фрагментов из фильтра, возвращает True
        В противном случае возвращает False
        """
        for word_from_filter in WORDSFILTER:
            if self._WORD.count(word_from_filter)>0 or self._DEFINITION.count(word_from_filter)>0:
                return False
        return True        

    def get(self):
        """
        Возвращает слово со скрытыми буквами
        """
        return ''.join(self._get_as_list())
    
    def is_letter_here(self, string):
        """
        Есть эта буква?
        Если входящий параметр string не корректный, возвращает -2
        Если буква уже есть в списке сыгранных букв - возвращает -1
        Если такой буквы нет в слове - возвращает 0
        Если буква есть в слове - возвращает количество этих букв в слове
        Также добавляет в список сыгранных букв
        """
        letter = preparation_letter(string)
        if letter is None: return -2
        if letter in self._played_letters: return -1
        found = self._WORD.count(letter)
        self._played_letters.append(letter)
        return found

    def is_solved(self):
        """
        Возвращает True, если количество скрытых букв в слове = 0 
        """
        if self.get().count(SIMBOL_HIDDEN) == 0:
            return True
        else:
            return False  

    def get_definition(self):
        """
        Возвращает определение слова
        """
        return self._DEFINITION          

    def _get_as_list(self):
        """
        Возвращает список, состоящий из букв слова self.WORD, 
        при этом если буквы нет в списке self.played_letters, то вместо нее SIMBOL_HIDDEN
        """
        result = []
        for letter in self._WORD:
            if letter in self._played_letters:
                result.append(letter)
            else:
                result.append(SIMBOL_HIDDEN)
        return result

    def get_one_random_letter(self):
        """
        Возвращает одну случайную неоткрыую букву в слове
        """
        result = None
        while True:
            result = preparation_letter(choice(self._WORD))
            if result not in self._played_letters: break
        return result

    def get_first_letter(self):
        """
        Возвращает первую букву в слове
        """
        return self._WORD[0]    

    def get_last_letter(self):
        """
        Возвращает последнюю букву в слове
        """
        return self._WORD[-1] 

    def get_allVowels(self):
        """
        Возвращает список гласных букв в слове
        """
        list = []
        for letter in self._WORD:
            try:
                if preparation_letter(letter) in VOWELS: list.append(letter)
            except Exception as e:
                pass    
        return list    

def preparation_letter(letter):
    """
    Подготавливает букву к обработке, возвращает полготовленную букву
    Возвращает None, если на входе не русская буква 
    """
    if len(letter)==0: return None
    result = letter[0].lower()
    if result in ABC:
        return result
    else:
        return None


if __name__=="__main__":
    test = HiddenWord()
    print(test._WORD)
    # test._DEFINITION = "м. разг. 1) Уменьш. к сущ.: навес. 2) Ласк. к сущ.: навес."
    print(test._DEFINITION)
    print(test._is_matches_the_filter()) 

