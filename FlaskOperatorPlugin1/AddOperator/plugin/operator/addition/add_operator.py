from plugin.operator.core.services.operator import OperatorBase


class AddOperator(OperatorBase):
    def operator_name(self):
        return "Addition"

    def operator_identifier(self):
        return "AdditionOperator"

    def operation(self,number1,number2):
        return number1+number2