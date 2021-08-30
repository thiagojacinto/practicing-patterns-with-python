#!bin/python3
# -*- coding: UTF-8 -*-

class FeeCalculator(object):
    """Calculator of fees"""
    
    def calculate(self, budget, tax_to_calculate):
        """Execute operations on a given budget"""
        calculated_fee = tax_to_calculate(budget.value)
        return calculated_fee

# introducing new fees
class NewFeeThree():
    """Fee that uses progression to handle its impact"""
    def __init__(self, budget) -> None:
        self.__budget = budget

    def calculate(self, value):
        if value > 500:
            return value * 0.1
        else:
            return value * 0.06

class NewFeeFour():
    """Fee that validate if one of the items is over some value"""
    def __init__(self, budget) -> None:
        self.__budget = budget

    def calculate(self, value):
        if value > 500 & self.has_one_item_over_100():
            return value * 0.075
        else:
            return value * 0.045
    
    def has_one_item_over_100(self):
        """Verify if one of the items of the budget has value over 100"""
        for item in self.__budget.get_itens():
            if item.value > 100: return True
        return False


if __name__ == '__main__':

    from src.budget import Budget, Item
    from src.patterns.strategy.taxes import ( calculate_tax_one, calculate_tax_two )

    my_budget = Budget()
    my_budget.add_item(Item('Item n.1', 100))
    my_budget.add_item(Item('Item n.2', 50))
    my_budget.add_item(Item('Item n.3', 150))
    my_budget.add_item(Item('Item n.4', 150))
    
    fee_calc = FeeCalculator()

    result_one = fee_calc.calculate(my_budget, calculate_tax_one)
    print(result_one)
    result_two = fee_calc.calculate(my_budget, calculate_tax_two)
    print(result_two)
    
    # applying new fees
    fee_three = NewFeeThree(my_budget)
    fee_four = NewFeeFour(my_budget)
    result_three = fee_calc.calculate(my_budget, fee_three.calculate)
    print(result_three)
    result_four = fee_calc.calculate(my_budget, fee_four.calculate)
    print(result_four)