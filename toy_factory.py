import abc

from toy import SantaWorkshop, Spider, RobotBunny


class ToyFactory(abc.ABC):
    """
        Base toy factory that all toy factories inherit from.
    """

    @abc.abstractmethod
    def create(self, **kwargs):
        """
            Creates different items depending on which factory is asked to create the item.
        :param kwargs: all necessary arguments required to make the specific item
        :return: item
        """
        pass


class SantaWorkshopFactory(ToyFactory):
    """
        Christmas themed factory to make toys.
    """

    def create(self, dimensions="", num_rooms="", **kwargs):
        """
            Creates a santa workshop toy Christmas themed item.
        :param dimensions: the width and height
        :param num_rooms: number of rooms
        :param kwargs: all other necessary arguments to create a santa workshop
        :return: SantaWorkshop toy object
        """
        return SantaWorkshop(dimensions, num_rooms, **kwargs)


class SpiderFactory(ToyFactory):
    """
        Halloween themed factory to make toys.
    """

    def create(self, speed="", jump="", glow="", species="", **kwargs):
        """
            Creates a spider toy Halloween themed item.
        :param speed: speed of the spider
        :param jump: jump height of the spider
        :param glow: whether it has glowing parts or not
        :param species: spider type
        :param kwargs: all other necessary arguments to create a spider
        :return: Spider toy object
        """

        return Spider(speed, jump, glow, species, **kwargs)


class RobotBunnyFactory(ToyFactory):
    """
        Easter themed factory to make toys.
    """

    def create(self, num_sound="", colour="", **kwargs):
        """
            Creates a robot bunny Easter themed item.
        :param num_sound: number of sounds
        :param colour: different valid colours
        :param kwargs: all other necessary arguments to create a robot bunny
        :return: RobotBunny toy object
        """

        return RobotBunny(num_sound, colour, **kwargs)
