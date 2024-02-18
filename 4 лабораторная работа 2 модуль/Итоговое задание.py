class ShibaInu:
    """
    Базовый класс описывает породу сиба-ину.
    :param origin: страна происхождения породы
    :param height: возможный рост собак
    :param weight: возможный вес собак
    """

    def __init__(self, origin: str, height: int, weight: int):
        self.origin = "Japan"
        self._height = height
        self._weight = weight

    @property
    def height(self):
        return self._height

    @property
    def weight(self):
        return self._weight

    @height.setter
    def height(self, height: int) -> None:
        if not isinstance(height, int):
            raise TypeError("Рост должен быть типа int")
        if height <= 0:
            raise ValueError("Рост должен быть положительным числом")
        self._height = height

    @weight.setter
    def weight(self, weight: int) -> None:
        if not isinstance(weight, int):
            raise TypeError("Вес должен быть типа int")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        self._weight = weight

    def __str__(self):
        return f"Порода сиба-ину из {self.origin}. Имеют средний размер. " \
               f"Например, рост: {self._height}; вес {self._weight}"

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"('Japan'={self.origin!r}, height={self._height!r}, weight={self._weight!r})"


class Chiin(ShibaInu):
    """
    Дочерний класс описывает сибу по личке Чиин.
    :param origin: страна происхождения породы
    :param height: возможный рост собак
    :param weight: возможный вес собак
    :param color: возможный окрас сиба-ину
    :param gender: пол собаки
    """
    def __init__(self, origin: str, height: int, weight: int, color: str, gender: str):
        super().__init__(origin)
        self._height = 42
        self._weight = 15
        self.color = "рыжий"
        self.gender = "male"

    @property
    def height(self):
        return self._height

    @property
    def weight(self):
        return self._weight

    @height.setter
    def height(self, height: int) -> None:
        if not isinstance(height, int):
            raise TypeError("Рост должен быть типа int")
        if height <= 0:
            raise ValueError("Рост должен быть положительным числом")
        self._height = 42

    @weight.setter
    def weight(self, weight: int) -> None:
        if not isinstance(weight, int):
            raise TypeError("Вес должен быть типа int")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")
        self._weight = 15

    def __str__(self):
        return f"Сиба-ину Чиин из {self.origin}. {self.gender}. " \
               f"Рост: {self._height}. Вес: {self._weight}. Окрас: {self.gender}"

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"('Japan'={self.origin!r}, height={self._height!r}, weight={self._weight!r})"
