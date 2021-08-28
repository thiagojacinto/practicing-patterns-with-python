#!bin/python3
# -*- coding: UTF-8 -*-

class Discount_calculator():
    """Condense discount rules and calculate"""

    def calculate(self, budget):
        """Applies discount rules"""
        
        if len(budget.get_itens()) > 5:
            return budget.value * 0.1
        
        elif budget.value > 400:
            return budget.value * 0.07

        # is it possible to have more rules?

if __name__ == '__main__':
    from src.budget import Budget, Item

    my_budget = Budget()
    my_budget.add_item(Item('Item n.1', 100))
    my_budget.add_item(Item('Item n.2', 25))
    my_budget.add_item(Item('Item n.3', 500))
    my_budget.add_item(Item('Item n.4', 75))

    discount = Discount_calculator()
    result = discount.calculate(my_budget)
    print("Discount : $ {0}".format(result))
