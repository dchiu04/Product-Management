class Candy:
    """
        Base Candy class that all candies inherit from.
    """
    def __init__(self, nuts, lactose, name, desc, product_id):
        self._nuts = nuts
        self._lactose = lactose
        self._name = name
        self._desc = desc
        self._product_id = product_id

    @property
    def name(self):
        return self._name

    @property
    def product_id(self):
        return self._product_id

    @property
    def desc(self):
        return self._desc

    def __str__(self):
        return f"Name: {self._name} ----\n" \
               f"Product ID: {self._product_id}\n" \
               f"Description: {self._desc}\n"


class PumpkinToffee(Candy):
    """
        Halloween themed candy. Requires variety.
    """
    def __init__(self, variety, **kwargs):
        super().__init__(
                         kwargs.get("nuts"),
                         kwargs.get("lactose"),
                         kwargs.get("name"),
                         kwargs.get("desc"),
                         kwargs.get("product_id")
                         )
        self._variety = variety


class CandyCane(Candy):
    """
        Christmas themed candy. Requires colour.
    """
    def __init__(self, colour, **kwargs):
        super().__init__(
                         kwargs.get("nuts"),
                         kwargs.get("lactose"),
                         kwargs.get("name"),
                         kwargs.get("desc"),
                         kwargs.get("product_id")
                         )
        self._colour = colour


class CremeEggs(Candy):
    """
        Easter themed candy. Requires pack size.
    """
    def __init__(self, pack_size, **kwargs):
        super().__init__(
                         kwargs.get("nuts"),
                         kwargs.get("lactose"),
                         kwargs.get("name"),
                         kwargs.get("desc"),
                         kwargs.get("product_id")
                         )
        self._pack_size = pack_size
