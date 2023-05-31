import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

        self.all.append(self)

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')

        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов')

        self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        path = '../src/items.csv'
        with open(path, 'r', encoding='cp1251') as file:
            datafile = csv.DictReader(file)
            for item in datafile:
                cls(name=item['name'], price=item['price'], quantity=item['quantity'])

    @staticmethod
    def string_to_number(num_str):
        return int(float(num_str))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return float(self.price * self.quantity)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"
