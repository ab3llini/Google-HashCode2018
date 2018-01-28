from abc import ABCMeta, abstractmethod


class Element:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_value(self):
        """
        :return: a relative value for an element;
                 an element with the lower value will be selected first
        """
        raise NotImplementedError

    @abstractmethod
    def clone(self):
        raise NotImplementedError
