#!bin/python3
# -*- coding: UTF-8 -*-

class NoDiscount():
    """Last item of discount chain. Returns zero discount"""
    
    def calculate(self, budget):
        return 0

class Discount_for_five_or_more_itens():
    """Discount when have 5 or more itens in a Budget"""
    def __init__(self, discount_rate = 0.1, next_discount = None) -> None:
        self.__discount_rate = discount_rate
        self.__next_discount = next_discount

    def calculate(self, budget):
        if len(budget.get_itens()) > 5:
            return budget.value * self.__discount_rate
        else:
            return self.__next_discount.calculate(budget)

class Discount_for_total_more_than_400():
    """Discount when have 400 or more of Budget value"""
    def __init__(self, discount_rate = 0.07, next_discount = None) -> None:
        self.__discount_rate = discount_rate
        self.__next_discount = next_discount

    def calculate(self, budget):
        if budget.value >= 400:
            return budget.value * self.__discount_rate
        else:
            return self.__next_discount.calculate(budget)