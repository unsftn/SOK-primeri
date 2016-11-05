from injector import Module, provider

from implementation import BigNameCoffeeShop, BadCoffeeMachine, CreditCardPaymentService, CashPaymentService, \
    LibraryCoffeeShop, GoodCoffeeMachine, BigTicket
from abstract_types import Shop, CoffeeMachine, CoffeeType, PaymentService


class BigName_BadCappuccino_Card_ShopModule(Module):
    def configure(self, binder):
        binder.bind(Shop,to=BigNameCoffeeShop)

    @provider
    def provides_coffee_machine(self)->CoffeeMachine:
        return BadCoffeeMachine(CoffeeType.capuccino)


class CommerceModule(Module):
    def configure(self, binder):
        binder.bind(PaymentService, to=CreditCardPaymentService)


class Library_GoodFilter_Cash_ShopModule(Module):
    def configure(self, binder):
        binder.bind(PaymentService, to=CashPaymentService)
        binder.bind(BigTicket, to=CreditCardPaymentService)
        binder.bind(Shop, to=LibraryCoffeeShop)

    @provider
    def provides_coffee_machine(self)->CoffeeMachine:
        return GoodCoffeeMachine(CoffeeType.filter)