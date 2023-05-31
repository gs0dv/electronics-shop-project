from src.item import Item


class MixinLanguage:
    """Класс-миксин, который хранит данные о раскладке и позволяющий её изменять"""
    # флаг для переключения языка с EN на RU
    flag = False

    def __init__(self):
        # свойство для хранения языковой раскладки
        self.__language = "EN"

    def change_lang(self):
        """Метод для переключения языка с EN на RU"""
        self.flag = False if self.flag else True
        self.__language = "RU" if self.flag else "EN"

    @property
    def language(self):
        """Геттер для свойства языки"""
        return self.__language


class Keyboard(Item, MixinLanguage):
    """Класс для представления клавиатура, который наследуется от классов Item и MixinLanguage"""

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
