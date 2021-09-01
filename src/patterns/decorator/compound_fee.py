# encoding=utf8
from abc import ABCMeta, abstractmethod

class TaxCompound():
    """
    Class that implements a decorator to compound taxes
    """

    __metaclass__ = ABCMeta

    def __init__(self, budget, next_tax = None) -> None:
        self.__next_tax = next_tax
        self.__budget = budget
    
    @property
    def budget(self):
        return self.__budget

    def next_calculate(self, value):
        if self.__next_tax is None:
            return 0
        else:
            return self.__next_tax.calculate(value)
    
    @abstractmethod
    def calculate(self, value):
        pass