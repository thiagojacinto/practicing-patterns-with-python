#!bin/python3
# -*- coding: UTF-8 -*-
from src.patterns.chain_of_responsability.discount_types import Discount_for_five_or_more_itens, Discount_for_total_more_than_400, NoDiscount

class Discount_calculator():
    """Condense discount rules and calculate"""

    def calculate(self, budget):
        """Applies discount rules"""
        
        # if len(budget.get_itens()) > 5:
        #     return budget.value * 0.1
        
        # elif budget.value > 400:
        #     return budget.value * 0.07

        # is it possible to have more rules?

        discount = Discount_for_total_more_than_400(
            next_discount = Discount_for_five_or_more_itens(next_discount = NoDiscount)
        ).calculate(budget)
        return discount

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
