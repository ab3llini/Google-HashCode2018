from abc import ABCMeta, abstractmethod
from element import Element
from collections import Iterable, Iterator


class ElementList(Iterable):
    """
    This class implement a list for the greedy algorithm over a list of elements.
    This class extends Iterable so it can be iterate with a foreach loop
    """
    __metaclass__ = ABCMeta
    # This should be a list of type Element
    __elements = []

    def __init__(self, elements):
        """
        Create a list of elements of type Element
        :param elements: a list of object of type Element
        :raise TypeError if elements is not a list of Element
        """
        if type(elements) is not list:
            raise TypeError
        if issubclass(elements[0], Element):
            print("elements are of type", type(elements[0]))
            raise TypeError

        self.__elements = elements
        self.__sorted = False
        self.__iter_index = 0

    def get_elements(self):
        return self.__elements

    @abstractmethod
    def ind(self, element):
        """
        :param element: an element that could be included in the solution
        :return: true if the element can be included, false otherwise
        """
        raise NotImplementedError

    @abstractmethod
    def clone(self):
        raise NotImplementedError

    def is_empty(self):
        return len(self.__elements) == 0

    def best(self):
        """
        If the list is not sorted, this method will sort it and then
        :return: the best Element according to the value returned from get_value()
        """
        if not self.__sorted:
            self.sort()
        e = self.__elements[0]
        self.__elements = self.__elements[1:]
        return e

    def sort(self):
        """
        If the elements are not sorted this will sort them with complexity O(n * log(n))
        :return: nothing
        """
        if not self.__sorted:
            self.__elements.sort(key=lambda element: element.get_value())
        self.__sorted = True

    def insert(self, element, mode='RECURSIVE'):
        """
        This method will add the element to the list, if the list is sorted
        the element will be added to the correct position, otherwise it will be
        added at the end of the list
        :param element: is the element to add
        :param mode: is the function type, 'RECURSIVE' for search complexity of O(log(n))
                     'ITERATIVE' for search complexity of O(n)
        """
        if issubclass(element, Element):
            print("element type is", type(element))
            raise TypeError
        if not self.__sorted:
            self.__elements.append(element)
        elif mode is 'RECURSIVE':
            self.__recursive_insert_in_order__(element)
        elif mode is 'ITERATIVE':
            self.__insert_in_order__(element)
        else:
            print("Error, the mode is incorrect")

    def remove(self, index):
        return self.__elements.pop(index)

    def __recursive_insert_in_order__(self, element, min_elem=0, max_elem=None):
        """
        This method will find the position for the new element with complexity of
        O(n * log(n)), for the remaining shifts the complexity still be O(n)
        :param element: is the element to add
        :param min_elem: is the minimum position, by default is 0
        :param max_elem: is the maximum position, by default is the length of the list
        """
        if max_elem is None:
            max_elem = len(self.__elements)

        if max_elem - min_elem <= 1:
            self.__elements.insert(max_elem, element)
            return

        index = (max_elem + min_elem) // 2
        if element.get_value() < self.__elements[index].get_value():
            self.__recursive_insert_in_order__(element, min_elem=min_elem, max_elem=index)
        else:
            self.__recursive_insert_in_order__(element, min_elem=index, max_elem=max_elem)

    def __insert_in_order__(self, element):
        """
        This method will find the position for the new element with complexity of
        O(n), for the remaining shifts the complexity still be O(n)
        :param element: is the element to add
        """
        index = 0
        while self.__elements[index].get_value() < element.get_value():
            index = index + 1
        self.__elements.insert(index, element)

    # Method for iterate into the list

    def __iter__(self):
        self.__iter_index = 0
        return self

    def next(self):
        if self.__has_next():
            self.__iter_index = self.__iter_index + 1
            return self.__elements[self.__iter_index - 1]
        else:
            raise StopIteration

    def __has_next(self):
        return self.__iter_index < len(self.__elements)
