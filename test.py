import unittest
from hidden_word import HiddenWord

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.hiddenword = HiddenWord()
        self.hiddenword.word = "слово"
        self.hiddenword.played_letters = ["с", "л", "о", "в", "о"]

    def test_count_symbols_in_string(self):
        self.assertEqual(self.hiddenword.is_win(), True)



if __name__ == '__main__':
    list = range(100,105)
    print(list) 
    print (len(list)) 
    print(list[0])   
    print(list[1]) 
    print(list[2]) 
    print(list[3])   