import abc
from enum import Enum


class Coffee(object):

    def __init__(self,coffee_type,good_coffee):
        self.coffee_type = coffee_type
        self.good_coffee = good_coffee

    def __str__(self):
        return "Coffee{{coffe_type={0}," \
                      "good_coffee={1}}}"\
                 .format(self.coffee_type,\
                  self.good_coffee)


class CoffeeMachine(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_coffee_type(self):
        pass

    @abc.abstractmethod
    def make_coffee(self):
        pass


class CoffeeType(Enum):
    filter = 1.2
    capuccino = 3.5

    def __str__(self):
        return "CoffeeType{{name={0},price={1}}}"\
                 .format(self.name,\
                  self.value)

    def get_price(self):
        return self.value


class PaymentService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pay(self,amount):
        pass


class Shop(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_coffee_type(self):
        pass

    @abc.abstractmethod
    def buy_coffee(self,payment):
        pass