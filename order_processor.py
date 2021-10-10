import math
import pandas as pd
from pathlib import Path
from animal_factory import ReindeerFactory, BunnyFactory, SkeletonFactory
from candy_factory import CandyCaneFactory, CremeEggsFactory, PumpkinToffeeFactory
from order import Order
from toy_factory import SantaWorkshopFactory, SpiderFactory, RobotBunnyFactory

# Used to map all factories to their corresponding item and holiday
factory_dict = {"Toy": {"Christmas": SantaWorkshopFactory, "Easter": RobotBunnyFactory, "Halloween": SpiderFactory},
                "StuffedAnimal": {"Christmas": ReindeerFactory, "Easter": BunnyFactory, "Halloween": SkeletonFactory},
                "Candy": {"Christmas": CandyCaneFactory, "Easter": CremeEggsFactory, "Halloween": PumpkinToffeeFactory}}


class OrderProcessor:
    """
        Processes the given excel file and turns the data into order objects. Also handles any potential
        input errors.
    """

    @staticmethod
    def read_file_to_orders(fn):
        """
            Reads the given excel file and converts it into a dictionary.
        :param fn: given excel file
        :return: all_orders list of dictionary
        """

        # Used to store all orders regardless of their validity
        print_orders = []

        # Used to store all valid orders
        all_orders = {}

        if Path(fn).is_file():
            orders = pd.read_excel(fn).to_dict(orient="record")

            for i in orders:
                holiday = i.get("holiday")
                item = i.get("item")

                keys = ['description',
                        'has_batteries',
                        'min_age',
                        'dimensions',
                        'num_rooms',
                        'speed',
                        'jump_height',
                        'has_glow',
                        'spider_type',
                        'num_sound',
                        'colour',
                        'has_lactose',
                        'has_nuts',
                        'variety',
                        'pack_size',
                        'stuffing',
                        'size',
                        'fabric']

                details = {x: i[x] for x in keys}

                order = Order(i.get("order_number"), i.get("product_id"), item, i.get("name"),
                              details)
                OrderProcessor.factory_mapping(order, holiday, item)

                # Only add valid orders to the store
                (message, condition) = OrderProcessor.error_handle(order, holiday)

                # Report is appended here
                # Append only valid orders to the list returned to Amazon
                if condition:
                    temp = "Order: {}, Item: {}, Product ID: {}, Name {}, Quantity: {}"
                    print_orders.append(
                        temp.format(order.order_num, order.item_type, order.product_id, order.name, i.get("quantity")))
                    all_orders[order.order_num] = [i.get('quantity'), order]
                else:
                    print_orders.append(message)

        return all_orders, print_orders

    def factory_mapping(order, holiday, item):
        """
            Maps the correct holiday to the order item.
        :param self: OrderProcessor
        :param order: current Order being processed
        :param holiday: the string designating the event
        :param item: to be mapped
        """
        factory = factory_dict.get(item).get(holiday)
        order._factory = factory

    @staticmethod
    def error_handle(order, holiday):
        """
            Handles any input errors given from the excel file.
        :param order: Order that is currently being processed
        :param holiday: the seasonal event corresponding to the items
        :return: True if there are no errors, else False
        """

        try:
            # holiday
            if holiday == 'Christmas' or holiday == 'Easter' or \
                    holiday == 'Halloween':
                pass
            else:
                return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                       "holiday can only be ""Christmas"" or ""Easter"" or ""Halloween".format(order.order_num), False
        except TypeError:
            return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                   "holiday can only be ""Christmas"" or ""Easter"" or ""Halloween".format(order.order_num), False

        try:
            # item type
            if order.item_type == 'Toy' or order.item_type == 'StuffedAnimal' or \
                    order.item_type == 'Candy':
                pass
            else:
                return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                       "item can only be ""Toy"" or ""StuffedAnimal"" or ""Candy""".format(order.order_num), False
        except TypeError:
            return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                   "item can only be ""Toy"" or ""StuffedAnimal"" or ""Candy""".format(order.order_num), False

        try:
            # has_batteries
            if order.details['has_batteries'] == 'Y' or order.details['has_batteries'] == 'N' \
                    or math.isnan(order.details['has_batteries']):
                pass
            else:
                return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                       "has_batteries can only be ""Y"" or ""N""".format(order.order_num), False
        except TypeError:
            return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                   "has_batteries can only be ""Y"" or ""N""".format(order.order_num), False

        try:
            # min_age
            if order.details['min_age'] > 0 or math.isnan(order.details['min_age']):
                pass
            else:
                return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                       "min_age can only be int greater than 0".format(order.order_num), False
        except TypeError:
            return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                   "min_age can only be int greater than 0".format(order.order_num), False

        try:
            # num_rooms
            if order.details['num_rooms'] > 0 or math.isnan(order.details['num_rooms']):
                pass
            else:
                return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                       "num_rooms can only be int greater than 0".format(order.order_num), False
        except TypeError:
            return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                   "num_rooms can only be int greater than 0".format(order.order_num), False

        try:
            # speed
            if order.details['speed'] > 0 or math.isnan(order.details['speed']):
                pass
            else:
                return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                       "speed can only be int greater than 0".format(order.order_num), False
        except TypeError:
            return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                   "speed can only be int greater than 0".format(order.order_num), False

        try:
            # jump_height
            if order.details['jump_height'] > 0 or math.isnan(order.details['jump_height']):
                pass
            else:
                return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                       "jump_height can only be int greater than 0".format(order.order_num), False
        except TypeError:
            return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                   "jump_height can only be int greater than 0".format(order.order_num), False

        try:
            # has_glow
            if order.details['has_glow'] == 'Y' or order.details['has_glow'] == 'N' \
                    or math.isnan(order.details['has_glow']):
                pass
            else:
                return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                       "has_glow can only be ""Y"" or ""N""".format(order.order_num), False
        except TypeError:
            return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                   "has_glow can only be ""Y"" or ""N""".format(order.order_num), False

        try:
            # spider_type
            if order.details['spider_type'] == 'Tarantula' or order.details['spider_type'] == 'Wolf Spider' \
                    or math.isnan(order.details['spider_type']):
                pass
            else:
                return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                       "spider_type can only be ""Tarantula"" or ""Wolf Spider""".format(order.order_num), False
        except TypeError:
            return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                   "spider_type can only be ""Tarantula"" or ""Wolf Spider""".format(order.order_num), False

        try:
            # num_sound
            if order.details['num_sound'] > 0 or math.isnan(order.details['num_sound']):
                pass
            else:
                return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                       "num_sound can only be int greater than 0".format(order.order_num), False
        except TypeError:
            return "Order: {}, Could not process order data was corrupted, InvalidDataError - " \
                   "num_sound can only be int greater than 0".format(order.order_num), False

        try:
            # Easter Toy colour
            if order.item_type == 'Toy' and holiday == 'Easter':
                if order.details['colour'] == 'Orange' or order.details['colour'] == 'Pink' or order.details[
                    'colour'] == 'Blue' \
                        or math.isnan(order.details['colour']):
                    pass
                else:
                    return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                           "toy colour can only be ""Orange"" or ""Blue"" or ""Pink""".format(order.order_num), False
        except TypeError:
            return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                   "toy colour can only be ""Orange"" or ""Blue"" or ""Pink""".format(order.order_num), False

        try:
            # Easter StuffedAnimal colour
            if order.item_type == 'StuffedAnimal' and holiday == 'Easter':
                if order.details['colour'] == 'White' or order.details['colour'] == 'Grey' or \
                        order.details['colour'] == 'Pink' or order.details['colour'] == 'Blue' \
                        or math.isnan(order.details['colour']):
                    pass
                else:
                    return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                           "stuffed animal colour can only be ""White"" or ""Grey"" or ""Blue"" or ""Pink""".format(
                        order.order_num), False
        except TypeError:
            return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                   "stuffed animal colour can only be ""White"" or ""Grey"" or ""Blue"" or ""Pink""".format(
                order.order_num), False

        try:
            # Christmas Candy colour
            if order.item_type == 'Candy' and holiday == 'Christmas':
                if order.details['colour'] == 'Red' or order.details['colour'] == 'Green' \
                        or math.isnan(order.details['colour']):
                    pass
                else:
                    return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                           "candy colour can only be ""Red"" or ""Green""".format(order.order_num), False
        except TypeError:
            return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                   "candy colour can only be ""Red"" or ""Green""".format(
                order.order_num), False

        try:
            # has_lactose
            if order.details['has_lactose'] == 'Y' or order.details['has_lactose'] == 'N' \
                    or math.isnan(order.details['has_lactose']):
                pass
            else:
                return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                       "has_lactose can only be ""Y"" or ""N""".format(
                    order.order_num), False
        except TypeError:
            return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                   "has_lactose can only be ""Y"" or ""N""".format(
                order.order_num), False

        try:
            # has_nuts
            if order.details['has_nuts'] == 'Y' or order.details['has_nuts'] == 'N' \
                    or math.isnan(order.details['has_nuts']):
                pass
            else:
                return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                       "has_nuts can only be ""Y"" or ""N""".format(
                    order.order_num), False
        except TypeError:
            return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                   "has_nuts can only be ""Y"" or ""N""".format(
                order.order_num), False

        try:
            # variety
            if order.details['variety'] == 'Sea Salt' or order.details['variety'] == 'Regular' or math.isnan(
                    order.details['variety']):
                pass
            else:
                return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                       "variety can only be ""Sea Salt"" or ""Regular""".format(
                    order.order_num), False
        except TypeError:
            return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                   "variety can only be ""Sea Salt"" or ""Regular""".format(
                order.order_num), False

        try:
            # pack_size
            if order.details['pack_size'] > 0 or math.isnan(order.details['pack_size']):
                pass
            else:
                return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                       "pack_size can only be int greater than 0".format(
                    order.order_num), False
        except TypeError:
            return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                   "pack_size can only be int greater than 0".format(
                order.order_num), False

        try:
            # stuffing
            if order.details['stuffing'] == 'Polyester Fibrefill' or order.details['stuffing'] == 'Wool' \
                    or math.isnan(order.details['stuffing']):
                pass
            else:
                return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                       "stuffing can only be ""Polyester Fibrefill"" or ""Wool""".format(
                    order.order_num), False
        except TypeError:
            return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                   "stuffing can only be ""Polyester Fibrefill"" or ""Wool""".format(
                order.order_num), False

        try:
            # size
            if order.details['size'] == 'S' or order.details['size'] == 'M' or order.details['size'] == 'L' \
                    or math.isnan(order.details['size']):
                pass
            else:
                return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                       "size can only be ""S"" or ""M"" or ""L""".format(
                    order.order_num), False
        except TypeError:
            return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                   "size can only be ""S"" or ""M"" or ""L""".format(
                order.order_num), False

        try:
            # fabric
            if order.details['fabric'] == 'Linen' or order.details['fabric'] == 'Acrylic' or \
                    order.details['fabric'] == 'Cotton' or math.isnan(order.details['fabric']):
                pass
            else:
                return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                       "fabric can only be ""Linen"" or ""Acrylic"" or ""Cotton""".format(
                    order.order_num), False
        except TypeError:
            return "Order {}, Could not process order data was corrupted, InvalidDataError - " \
                   "fabric can only be ""Linen"" or ""Acrylic"" or ""Cotton""".format(
                order.order_num), False
        return "", True
