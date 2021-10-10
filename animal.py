class Animal:
    """
        Base Animal class that all animals inherit from.
    """
    def __init__(self, stuffing, size, fabric, name, desc, product_id):
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric
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


class Skeleton(Animal):
    """
        Halloween themed stuffed animal.
    """
    def __init__(self, has_glow, **kwargs):
        super().__init__(
            kwargs.get("stuffing"),
            kwargs.get("size"),
            kwargs.get("fabric"),
            kwargs.get("name"),
            kwargs.get("desc"),
            kwargs.get("product_id")
        )
        self._has_glow = has_glow


class Reindeer(Animal):
    """
        Christmas themed stuffed animal.
    """
    def __init__(self, has_glow, **kwargs):
        super().__init__(
            kwargs.get("stuffing"),
            kwargs.get("size"),
            kwargs.get("fabric"),
            kwargs.get("name"),
            kwargs.get("desc"),
            kwargs.get("product_id")
        )
        self._has_glow = has_glow


class Bunny(Animal):
    """
        Easter themed stuffed animal.
    """
    def __init__(self, colour, **kwargs):
        super().__init__(
            kwargs.get("stuffing"),
            kwargs.get("size"),
            kwargs.get("fabric"),
            kwargs.get("name"),
            kwargs.get("desc"),
            kwargs.get("product_id")
        )
        self._colour = colour
