class Star:
    """
    Класс описывает модель звезды на елке
    :param tree_size: размер ёлки
    """
    def __init__(self, material: str, color: str, tree_size: str):
        self.material = "plastic"
        self.color = "gold"
        self.tree_size = "average"

    def size(self, tree_size: str):
        """
        метод проверяет, что елка средняя
        >>> Star.size()
        """
        if not isinstance(tree_size, str):
            raise TypeError("Размер елки должен быть типа str")

    def star_on_the_tree(self) -> bool:
        """
        метод проверяет, есть ли на елки звезда

        """

    def put(self):
        """
        метод должен одеть звезду на елку
        """
        ...


class Gift:
    """
    класс описывает модель новогоднего подарка
    """
    def __init__(self, height: int, width: int, thickness: int):
        self.height = 20
        self.width = 30
        self.thickness = 15

    def box(self, box_height: int, box_width: int, box_thickness: int):
        """
        метод проверяет, влезает ли подарок в праздничную коробку 30 х 35 х 20
        :param box_height: высота коробки
        :param box_width: ширина коробки
        :param box_thickness: толщина коробки
        >>> Gift.box()
        """
        box_height = 30
        box_width = 35
        box_thickness = 20
        ...
        if not isinstance(box_height, int):
            raise TypeError("Высота коробки должна быть типа int")
        if not isinstance(box_width, int):
            raise TypeError("Ширина коробки должна быть типа int")
        if not isinstance(box_thickness, int):
            raise TypeError("Толщина коробки должна быть типа int")
        if box_height - self.height < 0:
            raise ValueError ("Не хватает высоты коробки")
        if box_width - self.width < 0:
            raise ValueError ("Не хватает ширины коробки")
        if box_thickness - self.thickness < 0:
            raise ValueError ("Не хватает толщины коробки")

    def pack_in_box(self):
        """
        метод должен положить подарок в коробку
        """
        ...

class Gingerbread:
    """
    класс описывает модель имбирного пряника
    >>> Gingerbread.necessary()
    """
    def __init__(self, quantity: int, size: str):
        self.quantity = 12
        self.size = "small"

    def cooking(self):
        """
        метод должен готовить пряники
        """
        ...

    def necessary(self, required_quantity: int):
        """
        проверить, что изготовлено нужное количество
        :param required_quantity: нужное количество пряников (12)
        """
        required_quantity = 12
        ...
        if not isinstance(required_quantity, int):
            raise TypeError("Нужное количество пряников должно быть типа int")
        if required_quantity > self.quantity:
            raise ValueError("Пряников не хватает, нужно сделать еще")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
