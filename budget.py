#!bin/python3
# -*- coding: UTF-8 -*-

class Budget(object):
  
    def __init__(self) -> None:
        # self.__value = value
        self.__itens = []

    @property
    def value(self):
        # return self.__value
        total = 0.0
        for item in self.__itens:
            total += item.value
        
        return total
    
    def get_itens(self):
        """Returns the itens included in the budget"""
        return tuple(self.__itens)

class Item():

    def __init__(self, name, value) -> None:
        self.__name = name
        self.__value == value

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value
