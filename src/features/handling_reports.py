import logging
from src.budget import Budget, Item, Report

if __name__ == '__main__':

    my_other_budget = Budget()
    my_other_budget.add_item(Item('CTFL', 200.50))
    my_other_budget.add_item(Item('SaaS certification', 25.75))
    my_other_budget.add_item(Item('Another book in the shelf', 100.80))

    my_report = Report(my_other_budget)
    print(my_report)