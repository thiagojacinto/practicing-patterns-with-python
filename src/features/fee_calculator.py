
class FeeCalculator(object):
    """Calculator of fees"""
    
    def calculate(self, budget, tax_to_calculate):
        """Execute operations on a given budget"""
        calculated_fee = tax_to_calculate(budget.value)
        return calculated_fee


if __name__ == '__main__':

    from src.budget import Budget, Item
    from src.patterns.strategy.taxes import ( calculate_tax_one, calculate_tax_two )
    from src.patterns.template_method.template_fees import ( NewFeeFour, NewFeeThree )

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

    # now, we want to compound some taxes to calculate
    compound_fee_three_and_four = NewFeeThree(my_budget, NewFeeFour(my_budget))
    result_compound = fee_calc.calculate(my_budget, compound_fee_three_and_four.calculate)
    print(result_compound)

    ultra_fee_compound = NewFeeFour(
        my_budget,
        NewFeeThree(my_budget, 
            NewFeeFour(my_budget, 
                NewFeeThree(my_budget, compound_fee_three_and_four)
                )
            )
        )
    print(fee_calc.calculate(my_budget, ultra_fee_compound.calculate))