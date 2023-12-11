class star_on_the_tree:
    """
    класс описывает модель звезды на елке
    """
    def __init__(self, material: str, color: str, Christmas_tree_size: str):
        self.material = "plastic"
        self.color = "gold"
        self.Christmas_tree_size = "average"

    def size(self, Christmas_tree_size: str):
        """
        метод проверяет, елка средняя
        >>> star_on_the_tree.size()
        """
        if not isinstance(Christmas_tree_size, str):
            raise TypeError("")

    def put(self, number_of_stars_at_the_moment: int):
        """
        метод долелжен одеть звезду на елку, но чтобы на елке было не больше одной звезды

        :param number_of_stars_at_the_moment: если 0, то на елке нет звезды, если стоит n, то на елке n звезд

        >>> star_on_the_tree.put()
        """
        number_of_stars_at_the_moment = 0
        ...
        if not isinstance(number_of_stars_at_the_moment, int):
            raise TypeError("")
        if number_of_stars_at_the_moment < 0:
            raise ValueError("")
        if number_of_stars_at_the_moment + 1 >= 2:
            raise ValueError("")


class gift:
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
        >>> gift.box()
        """
        box_height = 30
        box_width = 35
        box_thickness = 20
        ...
        if not isinstance(box_height, int):
            raise TypeError("")
        if not isinstance(box_width, int):
            raise TypeError("")
        if not isinstance(box_thickness, int):
            raise TypeError("")
        if box_height - self.height < 0:
            raise ValueError
        if box_width - width < 0:
            raise ValueError
        if box_width - width < 0:
            raise ValueError

    def pack_in_box(self):
        """
        метод должен упаковать подарок в коробку
        """
        ...

class gingerbread:
    """
    класс описывает модель имбирного пряника
    >>> gingerbread.necessary()
    """
    def __init__(self, quantity: int, size: str):
        self.quantity = 12
        self.size = "small"

    def necessary(self, required_quantity: int):
        """
        проверить, что изготовлено нужное количество
        :param required_quantity: нужное количество пряников (12)
        """
        required_quantity = 12
        ...
        if not isinstance(required_quantity, int):
            raise TypeError("")
        if required_quantity > quantity:
            raise ValueError("")

    def finish_cooking(self):
        """
        если изготовлено меньше, то догодовить
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass