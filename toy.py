import abc


class Toy(abc.ABC):
    """
        Base Toy class that all toys inherit from.
    """

    def __init__(self, battery, min_age, name, desc, product_id):
        self._battery = battery
        self._min_age = min_age
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


class SantaWorkshop(Toy):
    """
        Christmas themed toy.
    """
    def __init__(self, dimensions, num_rooms, **kwargs):
        super().__init__(
            kwargs.get("battery"),
            kwargs.get("min_age"),
            kwargs.get("name"),
            kwargs.get("desc"),
            kwargs.get("product_id")
        )
        self._dimensions = dimensions
        self._num_rooms = num_rooms


class Spider(Toy):
    """
        Halloween themed toy.
    """
    def __init__(self, speed, jump, glow, species, **kwargs):
        super().__init__(
            kwargs.get("battery"),
            kwargs.get("min_age"),
            kwargs.get("name"),
            kwargs.get("desc"),
            kwargs.get("product_id")
        )
        self._speed = speed
        self._jump = jump
        self._glow = glow
        self._species = species


class RobotBunny(Toy):
    """
        Easter themed toy.
    """
    def __init__(self, num_sound, colour, **kwargs):
        super().__init__(
            kwargs.get("battery"),
            kwargs.get("min_age"),
            kwargs.get("name"),
            kwargs.get("desc"),
            kwargs.get("product_id")
        )
        self._num_sound = num_sound
        self._colour = colour
