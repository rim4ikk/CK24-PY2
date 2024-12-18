# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Cat:
    def _init_(self, ginger: int, sex: str):
        self.cats_color = ginger
        self.she_or_he = sex
        if not isinstance(ginger, int):
            raise TypeError("Процент рыжести должен быть типа int")
        if not isinstance(sex, int):
            raise TypeError("Пол должен быть типа str")
        if not (0 <= ginger <= 100):
            raise ValueError("Процент рыжести должен лежать в границах [0;100]")

    def pet(self, color_of_cat) -> bool:
        ...
    """
    Проверка насколько процентов кот рыжий 
    return Можно гладить, если кот не сильно рыжий
    raise TypeError если color_of_cat не int
    raise ValueError если не (0 <= color_of_cat <= 100)
    Пример:
    >>> cat = Cat(66, "жен")
    >>> cat.pet(42)
    """
    def name(self, pushok) -> str:
        ...
    """
    Проверка на то, подходит ли имя коту/кошке
    return Кошку нельзя назвать Пушок
    raise TypeError если pushok не str
    Пример:
    >>> cat = Cat(66, "жен")
    >>> cat.name("Маруся")
    """
class Shaverma:
    def _init_(self, inside: str, price: int):
        self.what_inside = inside
        self.which_price = price
        if not isinstance(inside, str):
            raise TypeError("Ключевой ингредиент должен быть типа str")
        if not isinstance(price, int):
            raise TypeError("Цена должна быть типа int")
    def eat(self, ingredient) -> bool:
        ...
    """
    Проверка на наличие какого-либо ингредиента (мяса, грибов и так далее)
    return Наличие ингредиента в рецепте шавермы
    raise TypeError если ingredient не str
    Пример:
    >>> mexican = Shaverma(jalapeno, 245)
    >>> mexican.eat(shrimp)
    """
    def buy(self, wallet) -> int:
        ...
    """
    Проверка на возможность купить шаверму
    return Сдача, например 
    raise ValueError если wallet - price < 0 
    Пример:
    >>> italian = Shaverma(pesto, 230)
    >>> italian.buy(250)
    """
class Hat:
    def _init_(self, hat_size: int, person_size: int, color: str):
        self.hat = hat_size
        self.person = person_size
        self.which_color = color
        if not isinstance(hat_size, int):
            raise TypeError("Размер шляпы должен быть типа int")
        if not isinstance(person_size, int):
            raise TypeError("Размер человека должен быть типа int")
        if not isinstance(color, str):
            raise TypeError("Цвет шляпы должен быть типа str")
    def wear(self) -> bool:
        ...
    """
    Функция проверяет возможность надеть шляпу
    return можно/нельзя
    Примеры:
    >>> hat = Hat(10, 9, "black")
    >>> hat.wear()
    """
    def joke(self, wanted_color) -> bool:
        ...
    """
    Функция проверяет примерку шляпы на комедию (проверка на цвет)
    return Как раз! (или нет)
    raise TypeError если wanted_color не str
    Пример:
    >>> hat = Hat(10, 9, "black")
    >>> hat.joke("black")
    """
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    "pass"
    doctest.testmod()
