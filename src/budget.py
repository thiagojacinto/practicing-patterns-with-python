#!bin/python3
# -*- coding: UTF-8 -*-
from src.patterns.state.budget_status import Status_pending

class Budget(object):
  
    def __init__(self) -> None:
        # self.__value = value
        self.__itens = []
        self.current_status = Status_pending()
        self.__extra_discount = 0.0

    @property
    def value(self) -> float:
        # return self.__value
        total = 0.0
        for item in self.__itens:
            total += item.value
        
        return total - self.__extra_discount
    
    def get_itens(self):
        """Returns the itens included in the budget"""
        return tuple(self.__itens)
    
    def add_item(self, item) -> None:
        """Adds a new item to the budget"""
        self.__itens.append(item)

    def apply_extra_discount(self) -> None:
        """Applies a discount rate that varies with the current budget status"""
        # if (self.current_status == Budget.PENDING):
        #     self.__extra_discount += self.value * 0.05
        # elif (self.current_status == Budget.APPROVED):
        #     self.__extra_discount += self.value * 0.02
        # elif (self.current_status == Budget.REPROVED):
        #     raise Exception('Reproved Budget do not receive extra discount.')
        # elif (self.current_status == Budget.CLOSED):
        #     raise Exception('Closed Budget do not receive extra discount.')

        self.current_status.apply_extra_discount(self)

    def add_extra_discount(self, discount) -> None:
        """Adds the input discount to the extra_discount property"""
        self.__extra_discount += discount

    def approve(self) -> None:
        """Set the status to APPROVED"""
        self.current_status.approve(self)

    def reprove(self) -> None:
        """Set the status to REPPROVED"""
        self.current_status.repprove(self)

    def close(self) -> None:
        """Set the status to CLOSED"""
        self.current_status.close(self)

class Item():

    def __init__(self, name, value) -> None:
        self.__name = name
        self.__value = value

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

class Report():
    """Explore the budget and creates a report with its items"""

    def __init__(self, budget: Budget) -> None:
        self.__budget = budget

        self.mail_to_ceo()
        self.save_content_into_db()
        self.send_to_printer()
    
    def __str__(self) -> str:
        list_items = []
        list_items.append(" ---- Budget status: {} ----\n".format(self.__budget.current_status))
        for item in self.__budget.get_itens():
            list_items.append("Item = {}, value = $ {} \n".format(item.name, item.value))

        return "".join(list_items)

    def send_to_printer(self):
        """Send content to print"""
        print('\n>>>>> SENDING THIS CONTENT TO THE PRINTER >>>>>\n')
        print(self)
        print('\n<<<<< FINISH PRINTING <<<<<\n')

    def save_content_into_db(self):
        """Save content into DB"""
        print('\n>>>>> SAVING THIS CONTENT INTO DB >>>>>\n')
        print(self)
        print('\n<<<<< FINISH SAVING <<<<<\n')

    def mail_to_ceo(self):
        """Send this content to CEO e-mail"""
        print('\n>>>>> SENDING TO CEO\'s E-MAIL >>>>>\n')
        print(self)
        print('\n<<<<< E-MAIL SENT <<<<<\n')