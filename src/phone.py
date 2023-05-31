from src.item import Item


class Phone(Item):
    """Класс для представления телефонов"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        # Метод базового класса
        super().__init__(name, price, quantity)
        # Количество поддерживаемых сим
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """Возвращает количество поддерживаемых сим"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, count_sim):
        """Устанавливает количество поддерживаемых сим, если их число больше нуля, иначе вызов исключения"""
        if count_sim <= 0 or count_sim % 2 != 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

        self.__number_of_sim = count_sim

    def __str__(self):
        """'iPhone 14'"""
        return self.name

    def __repr__(self):
        """Phone('iPhone 14', 120000, 5, 2)"""
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
