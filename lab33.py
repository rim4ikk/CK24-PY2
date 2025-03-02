class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str) -> None:
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int) -> None:
        super().__init__(name, author)
        self._pages = pages

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Число страниц {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("pages должен быть типа int")
        if new_pages <= 0:
            raise ValueError("pages должен быть больше нуля")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float) -> None:
        super().__init__(name, author)
        self._duration = duration

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: int) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("duration должен быть типа float")
        if new_duration <= 0:
            raise ValueError("duration должен быть больше нуля")
        self._duration = new_duration
