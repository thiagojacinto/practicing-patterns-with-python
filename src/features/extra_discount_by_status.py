import logging
from src.budget import Budget, Item

if __name__ == '__main__':

    my_other_budget = Budget()
    my_other_budget.add_item(Item('Item A', 200.50))
    my_other_budget.add_item(Item('Item A', 25.75))
    my_other_budget.add_item(Item('Item A', 100.80))

    print('Value without extra discount is: {0}'.format(my_other_budget.value))
    my_other_budget.apply_extra_discount()
    print('Value with STATUS PENDING extra discount is: {0}'.format(my_other_budget.value))

    my_other_budget.current_status = Budget.APPROVED
    my_other_budget.apply_extra_discount()
    print('Value with STATUS APPROVED extra discount is: {0}'.format(my_other_budget.value))

    try:
        my_other_budget.current_status = Budget.REPROVED
        my_other_budget.apply_extra_discount()
    except Exception:
        logging.exception('Exception raised')

    try:
        my_other_budget.current_status = Budget.CLOSED
        my_other_budget.apply_extra_discount()
    except Exception:
        logging.exception('Exception raised')