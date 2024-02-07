# TODO Написать 3 класса с документацией и аннотацией типов
class Apple: #  класс Яблоко - аргументы: сорт - строковый тип, вес - число.
    def __init__(self, apple_kind: str, apple_weight:[int, float]):
        """
        >>> a = Apple("test", 100)
        >>> a.apple_weight, a.apple_kind
        (100, 'test')
        """
        if not isinstance(apple_kind, str):
            raise TypeError
        self.apple_kind = apple_kind
        if not isinstance(apple_weight, (int, float)):
            raise TypeError
        if apple_weight < 0:
            raise ValueError
        self.apple_weight = apple_weight
    def package(self):    # Яблоки упаковывают
        ...
    def shope(self):      # Яблоки продают
        ...
    def cooke(self):      # Из Яблок готовят десерты
        ...
class HDD:  #Класс Жёсткий диск
    def __init__(self, brend: str, country: str, weight: [int,float], volume: [int,float]):
        """
        >>> b = HDD("test",'str', 100, 5)
        >>> b.brend, b.country, b.weight, b.volume
        ('test', 'str', 100, 5)
        """
        if not isinstance(brend, str):
            raise TypeError
        self.brend = brend  # Бренда жесткого диска
        if not isinstance(country, str):
            raise TypeError
        self.country = country # Страна производства жесткого диска
        if not isinstance(weight, (int, float)):
            raise TypeError
        if weight < 0:
            raise ValueError
        self.weight = weight    # Вес жесткого диска
        if not isinstance(volume,(int, float)):
            raise TypeError
        if volume < 0:
            raise ValueError
        self.volume = volume    # Объем жесткого диска

    def order(self):    # Диск можно заказать
        ...
    def test(self):     # Диск можно проверить
        ...
    def connect(self):     # Диск можно установить
        ...
    def write_file(self):        # На диск можно записать файлы
        ...
    def reade_file(self):        # С диска можно прочитать файлы
        ...

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
