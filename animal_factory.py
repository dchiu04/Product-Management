import abc
from animal import Animal, Skeleton, Bunny, Reindeer


class AnimalFactory(abc.ABC):
    """
        Base factory that all animal factories inherit from.
    """

    @abc.abstractmethod
    def create(self, **kwargs):
        """
            Creates different items depending on which factory is asked to create the item.
        :param kwargs: all necessary arguments required to make the specific item
        :return: item
        """
        pass


class SkeletonFactory(AnimalFactory):
    """
        Halloween themed factory to make stuffed animals.
    """

    def create(self, has_glow="", **kwargs):
        """
            Creates a skeleton stuffed animal Halloween themed item.
        :param has_glow: whether it includes a glowing part or not
        :param kwargs: all other necessary arguments to create a skeleton
        :return: Skeleton stuffed animal object
        """
        return Skeleton(has_glow, **kwargs)


class ReindeerFactory(AnimalFactory):
    """
        Christmas themed factory to make stuffed animals.
    """

    def create(self, has_glow="", **kwargs):
        """
            Creates a reindeer stuffed animal Christmas themed item.
        :param has_glow: whether it includes a glowing part or not
        :param kwargs: all other necessary arguments to create a reindeer
        :return: Reindeer stuffed animal object
        """
        return Reindeer(has_glow, **kwargs)


class BunnyFactory(AnimalFactory):
    """
        Easter themed factory to make stuffed animals.
    """

    def create(self, colour="", **kwargs):
        """
            Creates a bunny stuffed animal Easter themed item.
        :param colour: the colour of the stuffed animal
        :param kwargs: all other necessary arguments to create a bunny
        :return: Bunny stuffed animal object
        """
        return Bunny(colour, **kwargs)
