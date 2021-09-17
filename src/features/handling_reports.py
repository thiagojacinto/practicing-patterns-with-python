import logging
from src.budget import Budget, Item, Report
from src.patterns.observer.observers import mail_to_ceo, save_content_into_db, send_to_printer

if __name__ == '__main__':

    my_other_budget = Budget()
    my_other_budget.add_item(Item('CTFL', 200.50))
    my_other_budget.add_item(Item('SaaS certification', 25.75))
    my_other_budget.add_item(Item('Another book in the shelf', 100.80))

    my_report = Report(
        my_other_budget,
        observers=[mail_to_ceo, save_content_into_db, send_to_printer]
        )
