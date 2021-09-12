from abc import ABCMeta, abstractmethod


class Budget_status():
    """Represents a status of the budget"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def apply_extra_discount(self, budget):
        pass

    @abstractmethod
    def approve(self, budget) -> None:
        pass

    @abstractmethod
    def repprove(self, budget) -> None:
        pass

    @abstractmethod
    def close(self, budget) -> None:
        pass


class Status_pending(Budget_status):
    """Budget status as PENDING"""

    def apply_extra_discount(self, budget):
        budget.add_extra_discount(budget.value * 0.05)

    def approve(self, budget) -> None:
        budget.current_status = Status_approved()

    def repprove(self, budget) -> None:
        budget.current_status = Status_repproved()

    def close(self, budget) -> None:
        budget.current_status = Status_closed()


class Status_approved(Budget_status):
    """Budget status as APPROVED"""

    def apply_extra_discount(self, budget):
        return budget.add_extra_discount(budget.value * 0.02)

    def approve(self, budget) -> None:
        raise Exception('Budget status is already APPROVED')

    def repprove(self, budget) -> None:
        raise Exception(
            'Budget status is already APPROVED, cannot be repproved')

    def close(self, budget) -> None:
        budget.current_status = Status_closed()


class Status_repproved(Budget_status):
    """Budget status as REPPROVED"""

    def apply_extra_discount(self, budget):
        raise Exception('Reproved Budget do not receive extra discount.')

    def approve(self, budget) -> None:
        raise Exception(
            'Budget status is already REPPROVED, cannot be approved')

    def repprove(self, budget) -> None:
        raise Exception('Budget status is already REPPROVED')

    def close(self, budget) -> None:
        budget.current_status = Status_closed()


class Status_closed(Budget_status):
    """Budget status as closed"""

    def apply_extra_discount(self, budget):
        raise Exception('Closed Budget do not receive extra discount.')

    def approve(self, budget) -> None:
        raise Exception('Budget status is already CLOSED, cannot be approved')

    def repprove(self, budget) -> None:
        raise Exception('Budget status is already CLOSED, cannot be repproved')

    def close(self, budget) -> None:
        raise Exception('Budget status is already CLOSED')
