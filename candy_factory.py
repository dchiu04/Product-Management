import abc
from candy import Candy, PumpkinToffee, CandyCane, CremeEggs


class CandyFactory(abc.ABC):
    """
        Base candy factory that all candy factories inherit from.
    """

    @abc.abstractmethod
    def create(self, **kwargs):
        """
            Creates different items depending on which factory is asked to create the item.
        :param kwargs: all necessary arguments required to make the specific item
        :return: item
        """
        pass


class PumpkinToffeeFactory(CandyFactory):
    """
        Halloween themed candy factory that makes candy.
    """

    def create(self, variety="", **kwargs):
        """
            Creates a pumpkin toffee candy Halloween themed item.
        :param variety: variety of the candy
        :param kwargs: all other necessary arguments to create a pumpkin toffee candy
        :return: PumpkinToffee candy object
        """
        return PumpkinToffee(variety, **kwargs)


class CandyCaneFactory(CandyFactory):
    """
        Christmas themed candy factory that makes candy.
    """

    def create(self, colour="", **kwargs):
        """
            Creates a candy cane candy Christmas themed item.
        :param colour: the colour of the candy
        :param kwargs: all other necessary arguments to create a candy cane candy
        :return: CandyCane candy object
        """
        return CandyCane(colour, **kwargs)


class CremeEggsFactory(CandyFactory):
    """
        Easter themed candy factory that makes candy.
    """

    def create(self, pack_size="",**kwargs):
        """
            Creates a creme egg candy Easter themed item.
        :param pack_size: the amount of candies in one quantity
        :param kwargs: all other necessary arguments to create a creme egg candy
        :return: CremeEgg candy object
        """
        return CremeEggs(pack_size,**kwargs)
