#!bin/python3
# -*- coding: UTF-8 -*-

class Budget(object):

    PENDING     = 1
    APPROVED    = 2
    REPROVED    = 3
    CLOSED      = 4
  
    def __init__(self) -> None:
        # self.__value = value
        self.__itens = []
        self.current_status = 1
        self.__extra_discount = 0.0

    @property
    def value(self) -> float:
        # return self.__value
        total = 0.0
        for item in self.__itens:
            total += item.value
        
        return total - self.__extra_discount
    
    def get_itens(self):
        """Returns the itens included in the budget"""
        return tuple(self.__itens)
    
    def add_item(self, item) -> None:
        """Adds a new item to the budget"""
        self.__itens.append(item)

    def apply_extra_discount(self) -> None:
        """Applies a discount rate that varies with the current budget status"""
        if (self.current_status == Budget.PENDING):
            self.__extra_discount += self.value * 0.05
        elif (self.current_status == Budget.APPROVED):
            self.__extra_discount += self.value * 0.02
        elif (self.current_status == Budget.REPROVED):
            raise Exception('Reproved Budget do not receive extra discount.')
        elif (self.current_status == Budget.CLOSED):
            raise Exception('Closed Budget do not receive extra discount.')

class Item():

    def __init__(self, name, value) -> None:
        self.__name = name
        self.__value = value

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value
