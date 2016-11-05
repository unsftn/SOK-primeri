from injector import inject, Key

from abstract_types import CoffeeMachine, Coffee, PaymentService, Shop


class BadCoffeeMachine(CoffeeMachine):
    def __init__(self, coffee_type):
        self.coffee_type = coffee_type

    def get_coffee_type(self):
        return self.coffee_type

    def make_coffee(self):
        return Coffee(self.coffee_type,False)

    def __str__(self):
        return "BadCoffeeMachine{{coffee_type={}}}"\
                 .format(self.coffee_type)


class GoodCoffeeMachine(CoffeeMachine):
    def __init__(self, coffee_type):
        self.coffee_type = coffee_type

    def get_coffee_type(self):
        return self.coffee_type

    def make_coffee(self):
        return Coffee(self.coffee_type, True)

    def __str__(self):
        return "GoodCoffeeMachine{{coffee_type={}}}"\
                 .format(self.coffee_type)


class CashPaymentService(PaymentService):
    def pay(self, amount):
        print("Cashing {}".format(amount))

    def __str__(self):
        return "CashPaymentService{{" \
               "instance={}}}".format(self.__hash__())


class CreditCardPaymentService(PaymentService):
    def pay(self, amount):
        print("Connecting...transmitting"
              "...approved {}!".format(amount))

    def __str__(self):
        return "CreditCardPaymentService{{" \
               "instance={}}}".format(self.__hash__())

#Kreira se novi tip za anotaciju parametra
# big_ticket_payment_service
# konstruktora klase LibraryCoffeeShop
# koji ocekuje objekat koji nasledjuje
# tip PaymentService, ali ne mora da se poklapa
# sa tipom objekta koji se prosledjuje parametru
# payment_service
BigTicket=Key("BigTicket")


class LibraryCoffeeShop(Shop):

    @inject
    def __init__(self, coffee_machine: CoffeeMachine,
                    payment_service: PaymentService,
                    big_ticket_payment_service: BigTicket):
        self.coffee_machine=coffee_machine
        self.payment_service=payment_service
        self.big_ticket_payment_service=big_ticket_payment_service

    def get_coffee_type(self):
        return self.coffee_machine.get_coffee_type()

    def buy_coffee(self,payment):
        price = self.coffee_machine.get_coffee_type().get_price()
        change = payment-price
        if change <= 0 :
            raise Exception("Oops! That's {0} not enough"
                            " for a cup of coffee."
                            " It costs {1}. But it's ok,"
                            " you can pay us next week"
                            .format(payment,price))

        coffee=self.coffee_machine.make_coffee()
        self.payment_service.pay(price)
        print("Thanks for the {} tip!".format(change))
        return coffee

    def __str__(self):
        return "LibraryCoffeeShop{{" \
               "\n coffee_machine={0}" \
               "\n paymentService={1}" \
               "\n big_ticket_payment_service={2}}}"\
               .format(self.coffee_machine,
                       self.payment_service,
                       self.big_ticket_payment_service)


class BigNameCoffeeShop(Shop):

    @inject
    def __init__(self, coffee_machine: CoffeeMachine, payment_service: PaymentService):
        self.coffee_machine = coffee_machine
        self.payment_service = payment_service

    def get_coffee_type(self):
        return self.coffee_machine.get_coffee_type()

    def buy_coffee(self, payment):
        price = self.coffee_machine.get_coffee_type().get_price()
        change = payment-price
        if change <= 0:
            raise Exception("Sorry, that's {} not enough"
                            " for a cup of coffee. "
                            "It costs {}"
                            .format(payment, price))

        coffee = self.coffee_machine.make_coffee()
        self.payment_service.pay(price)
        print("Thank you....Next in line")
        return coffee

    def __str__(self):
        return "BigNameCoffeeShop{{" \
               "\n coffee_machine={0}" \
               "\n paymentService={1}}}"\
               .format(self.coffee_machine,
                       self.payment_service)