from os.path import abspath, curdir, join

# Папка запущенной программы
BASE_PATH = abspath(curdir)

# папка, где хранятся звуковые файлы
FOLDER_SOUND_FILES = join(BASE_PATH,"SOUND FILES")

# папка, где хранятся иконки
FOLDER_ICONS = join(BASE_PATH,"ICONS FILES")


PRICE_SHOW_DEFINITION = -100
PRICE_PUSH_LETTER = -10
PRICE_OPEN_LETTER = 20
PRICE_ONE_RANDOM_LETTER = -PRICE_OPEN_LETTER - 10
PRICE_FIRST_AND_LAST_LETTER = -100
PRICE_OPEN_ALL_VOWELS = - 150
BALANCE_DEFAULT = 100
SPEED_ANIMATION_GOLD = 1

TEXTBUTTON_SHOW_DEFINITION = f" Показать определение слова {PRICE_SHOW_DEFINITION}"
TEXTBUTTON_FIRST_AND_LAST_LETTER = f" Открыть первую и последнюю буквы {PRICE_FIRST_AND_LAST_LETTER}"
TEXTBUTTON_ONE_RANDOM_LETTER = f" Открыть случайную букву {PRICE_ONE_RANDOM_LETTER}"
TEXTBUTTON_OPEN_ALL_VOWELS = f" Открыть все гласные {PRICE_OPEN_ALL_VOWELS}"

