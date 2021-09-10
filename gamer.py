from setting import *

class Gamer:
    def __init__(self, name="Новый игрок", balance_gold=BALANCE_DEFAULT, numberRound=1):
        """
        Класс для сохранения прогресса игрока
        """
        self.name = name # имя
        self.balance_gold = balance_gold # баланс золота
        self.numberRound = numberRound # до какого раунда дошел
        self.is_gaming = True
        self._script_of_animation = None
        
    def transaction_gold(self, sum_transaction):
        """
        Изменяет баланс золота у игрока
        """
        bal_old = self.balance_gold
        self.balance_gold += sum_transaction  
        self._script_of_animation(bal_old, self.balance_gold) 

    def set_script_of_animation(self, script):
        """
        Устанавливает метод, запускаемый для анимации смены баланса золота
        """
        self._script_of_animation = script



def get_gamer():
    gamer = Gamer()
    return gamer