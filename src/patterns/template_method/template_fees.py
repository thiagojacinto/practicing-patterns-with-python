#!bin/python3
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from src.patterns.decorator import compound_fee
from src.patterns.decorator.add_three import additional_three

# using a template class
class FeeTemplate(compound_fee.TaxCompound, metaclass = ABCMeta):
    """Basic logic container for a new Fee"""
    
    @additional_three
    def calculate(self, value):
        """Contains the basic if-this-else-that logic to apply a fee calculation"""
        if self.condition_to_use_max_tax(value):
            return self.apply_max_tax(value) + self.next_calculate(value)
        else:
            return self.apply_min_tax(value) + self.next_calculate(value)
    
    @abstractmethod
    def condition_to_use_max_tax(self, value):
        pass
    
    @abstractmethod
    def apply_max_tax(self, value):
        pass
    
    @abstractmethod
    def apply_min_tax(self, value):
        pass

# introducing new fees
class NewFeeThree(FeeTemplate):
    """Fee that uses progression to handle its impact"""

    def condition_to_use_max_tax(self, value):
        return value > 500
    
    def apply_max_tax(self, value):
        return value * 0.1
    
    def apply_min_tax(self, value):
        return value * 0.06
    

class NewFeeFour(FeeTemplate):
    """Fee that validate if one of the items is over some value"""

    def condition_to_use_max_tax(self, value):
        return value > 500 & self.__has_one_item_over_100()
    
    def apply_max_tax(self, value):
        return value * 0.075
    
    def apply_min_tax(self, value):
        return value * 0.045
    
    def __has_one_item_over_100(self):
        """Verify if one of the items of the budget has value over 100"""
        for item in self.budget.get_itens():
            if item.value > 100: return True
        return False