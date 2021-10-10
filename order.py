class Order:
    """
        A dictionary designating to keeping track of orders made to
        the store Amazon.
    """

    def __init__(self, order_num, product_id, item_type, name, prod_details):
        self._order_num = order_num
        self._product_id = product_id
        self._item_type = item_type
        self._name = name
        self._prod_details = prod_details
        self._factory = None

    @property
    def order_num(self):
        return self._order_num

    @property
    def item_type(self):
        return self._item_type

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def details(self):
        return self._prod_details

    @property
    def factory(self):
        return self._factory

    def __str__(self):
        return f"---- Order: {self._order_num} ----\n" \
               f"Item: {self._item_type}\n" \
               f"Product ID: {self._product_id}\n" \
               f"Name: {self._name}\n" \
               f"Details: {self._prod_details}\n" \
               f"Factory: {self._factory}"
