#!bin/python3
# -*- coding: UTF-8 -*-

class FeeCalculator(object):
    """Calculator of fees"""
    
    def calculate(self, budget):
        """Execute operations on a given budget"""
        calculated_fee = budget.value * 0.015
        return calculated_fee

if __name__ == '__main__':

    from budget import Budget

    my_budget = Budget(450)
    fee_calc = FeeCalculator()

    result = fee_calc.calculate(my_budget)
    print(result)