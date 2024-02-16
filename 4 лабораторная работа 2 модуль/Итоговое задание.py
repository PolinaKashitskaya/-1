if __name__ == "__main__":

    # Write your solution here
    class Dog:
        """
        Базовый класс собаки.
        :param kingdom: царство, к которому относятся собаки
        :param size: возможный размер собак
        """

        def __init__(self, kingdom: str, size: str):
            self.kingdom = "животные"
            self.size = "большой, средний, маленький"

        @property
        def kingdom(self):
            """
            Геттер должен вернуть kingdom
            """
            return self.kingdom

        def __str__(self):
            return f"Собаки относятся к царству {self.kingdom}. " \
                   f"и имеют больший диапазон размеров, чем любые другие млекопитающие. " \
                   f"Основное деление по размеру: {self.size}"


        def __repr__(self):
            return f"{self.__class__.__name__}" \
                   f"('животные'={self.kingdom!r}, 'большой, средний, маленький'={self.size!r})"


    class ShibaInu(Dog):
        """
        Дочерний класс сиба-ину.
        :param kingdom: царство, к которому относятся собаки, в том числе и сиба-ину
        :param size: размер сиба-ину
        :param color: возможный окрас сиба-ину
        """
        def __init__(self, kingdom: str, size: str, color: str):
            super().__init__(kingdom)
            self._size = "средний"
            self.color = "черный, рыжий, зонарный"

        @property
        def kingdom(self):
            """
            Геттер должен вернуть kingdom
            """
            return self.kingdom

        def size(self):
            """
            Геттер должен вернуть size
            """
            return self._size

        def color(self):
            """
            Геттер должен вернуть color
            """
            return self.color

        def __str__(self):
            return f"Собаки относятся к царству {self.kingdom}. " \
                   f"Сиба-ину - порода охотничьих собак. " \
                   f"Их размер: {self._size}." \
                   f"Стандарт допускает три основных типа окраса сиба-ину: {self.color}" \
                   f"Также бывают белые сиба-ину, но они не являются стандартом породы"

        def __repr__(self):
            return f"{self.__class__.__name__}" \
                   f"('животные'={self.kingdom!r}, 'средний'={self._size!r}, 'черный, рыжий, зонарный'={self.color!r})"

        @size.setter
        def size(self, value):
            self._size = value


    pass