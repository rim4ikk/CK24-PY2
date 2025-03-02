import doctest


class Computer:
    """
    Класс описывает компьютер, без привязки к типу устройства - ноутбук или десктоп
    """

    def __init__(self, brand: str, system: str, gpu: str) -> None:
        """
        Иницализация экземпляра класса

        Все методы непубличны, для того, чтобы их можно было менять только через соответствующие свойства

        :param brand: производитель ПК, read-only, т.к. производителя поменять нельзя
        :param system: ОС ПК
        :param gpu: установленная видеокарта

        Пример:
        >>> comp = Computer("msi", "windows", "gtx-2354") # инициализация экземпляра класса
        """
        self._brand = brand
        self._system = system
        self._gpu = gpu

    def __str__(self) -> str:
        """
        Вывод информации о компьютере

        :return: строка информации о ПК
        """
        return f"Информация о компьютере: производитель: {self._brand}, " \
               f"ОС: {self._system}, " \
               f"видеокарта: {self._gpu}"

    def __repr__(self) -> str:
        """
        Вывод информации об экзепляре класса

        :return: строка информации об объекте Computer
        """
        return f"{self.__class__.__name__}({self._brand!r}, " \
               f"{self._system!r}, " \
               f"{self._gpu!r})"

    @property
    def brand(self) -> str:
        """getter для brand, setter отсутствует, т.к. производителя нельзя поменять """
        return self.brand

    @property
    def system(self) -> str:
        """getter для system"""
        return self._system

    @system.setter
    def system(self, new_system: str) -> None:
        """setter для system, проверяющий значение system"""
        if not isinstance(new_system, str):
            raise TypeError("Название новой системы должно быть строкой")
        self._system = new_system

    @property
    def gpu(self) -> str:
        """Getter для gpu"""
        return self._gpu

    @gpu.setter
    def gpu(self, new_gpu: str) -> None:
        """setter для gpu с проверкой"""
        if not isinstance(new_gpu, str):
            raise TypeError("Название видеокарты должно быть строкой")
        self._gpu = new_gpu

    def stress_test(self) -> bool:
        """
        Проводит стресс-тест компьютера

        :return: True, если тест пройден, False, если нет

        Пример:
        >>> comp = Computer("msi", "windows", "gtx-2354")
        >>> comp.stress_test()
        """
        ...


class Laptop(Computer):
    def __init__(self, brand: str, system: str, gpu: str, diagonal: float) -> None:
        """
        Инициализация экземпляра класса дочернего Laptop, с новым атрибутом diagonal

        :param diagonal: диагональ ноутбука
        """
        super().__init__(brand, system, gpu)
        self._diagonal = diagonal

    def __str__(self) -> str:
        """
        __str__ как у Computer с добавлением параметра diagonal в выводе

        :return: строка информации о ноутбуке
        """
        return f"Информация о компьютере: производитель: {self._brand}, " \
               f"ОС: {self._system}, " \
               f"видеокарта: {self._gpu}, " \
               f"диагональ ноутбука: {self._diagonal}"

    def __repr__(self) -> str:
        """
        __repr__ как у Computer с добавлением параметра diagonal в выводе

        :return: строка информации об объекте Laptop
        """
        return f"{self.__class__.__name__}({self._brand!r}, " \
               f"{self._system!r}, " \
               f"{self._gpu!r}, " \
               f"{self._diagonal})"

    @property
    def diagonal(self) -> float:
        """getter для diagonal, setter отсутствует, диагональ нельзя поменять"""
        return self._diagonal


class Desktop(Computer):
    def __init__(self, brand: str, system: str, gpu: str, location: int, can_be_watered: bool) -> None:
        """
        Инициализация экземпляра класса дочернего Laptop, с новыми атрибутами location, can_be_watered

        :param location: код расположения десктопа на предприятии
        :param can_be_watered: возможность установления водяной системы охлаждения
        """
        super().__init__(brand, system, gpu)
        self._location = location
        self._can_be_watered = can_be_watered

    def __str__(self) -> str:
        """
        __str__ как у Computer с добавлением параметров diagonal и can_be_watered в выводе

        :return: строка информации о десктопе
        """
        return f"Информация о компьютере: производитель: {self._brand!r}, " \
               f"ОС: {self._system!r}, " \
               f"видеокарта: {self._gpu!r}, " \
               f"номер точки расположения: {self._location}, " \
               f"есть слот для водяного охлаждения: {self._can_be_watered}"

    def __repr__(self) -> str:
        """
        __repr__ как у Computer с добавлением параметров diagonal и can_be_watered в выводе

        :return: строка информации об объекте Desktop
        """
        return f"{self.__class__.__name__}(" \
               f"{self._brand}, " \
               f"{self._system}, " \
               f"{self._gpu}, " \
               f"{self._location}, " \
               f"{self._can_be_watered})"

    @property
    def location(self) -> int:
        """getter для location"""
        return self._location

    @location.setter
    def location(self, new_location: int) -> None:
        """setter с проверкой для location"""
        if not isinstance(new_location, int):
            raise TypeError("Код расположения десктопа должен быть типа int")
        if new_location < 0:
            raise ValueError("Код расположения десктопа должен быть положительным числом")
        self._location = new_location

    @property
    def can_be_watered(self) -> bool:
        """getter для can_be_watered, setter отсутствует: этот параметр нельзя менять"""
        return self._can_be_watered

    def stress_test(self) -> bool:
        """
        Унаследованный метод stress_test. Перегружен для работы с десктопами с возможностью водяного охлаждения.
        Если такая возможность есть - происходит особый стресс-тест, иначе обычный стресс-тест

        :return: True, если тест пройден, False, если нет

        Пример:
        >>> desk = Desktop("msi", "windows", "gtx-1499", 234, True)
        >>> desk.stress_test()
        """
        if self._can_be_watered:
            ...
        else:
            super().stress_test()
            ...


if __name__ == "__main__":
    # Write your solution here
    doctest.testmod()
    pass
