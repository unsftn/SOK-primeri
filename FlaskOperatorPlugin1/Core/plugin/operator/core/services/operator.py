import abc


class OperatorBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operator_identifier(self):
        pass

    @abc.abstractmethod
    def operator_name(self):
        pass

    @abc.abstractmethod
    def operation(self,number1,number2):
        pass