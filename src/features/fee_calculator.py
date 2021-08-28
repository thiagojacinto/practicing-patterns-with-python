#!bin/python3
# -*- coding: UTF-8 -*-

class FeeCalculator(object):
    """Calculator of fees"""
    
    def calculate(self, budget, tax_to_calculate):
        """Execute operations on a given budget"""
        calculated_fee = tax_to_calculate(budget.value)
        return calculated_fee

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