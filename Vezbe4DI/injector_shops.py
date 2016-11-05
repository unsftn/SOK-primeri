from injector import Injector

from injector_modules import CommerceModule, BigName_BadCappuccino_Card_ShopModule, Library_GoodFilter_Cash_ShopModule
from abstract_types import Shop


def shop1():
    injector = Injector([CommerceModule, BigName_BadCappuccino_Card_ShopModule])
    return injector.get(Shop)


def shop2():
    injector = Injector([CommerceModule])
    #Hocemo da promenimo da se za PaymentService koristi
    #    CashPaymentService iz Library_GoodFilter_Cash_ShopModule
    # umesto
    #    CreditCardPaymentService iz CommerceModule
    child = injector.create_child_injector(Library_GoodFilter_Cash_ShopModule)
    return child.get(Shop)

if __name__ == '__main__':

    shop = shop1()

    print("At shop: {}".format(shop))

    coffee=shop.buy_coffee(10)
    print("Bought coffee: {}".format(coffee))


    print()

    shop = shop2()

    print("At shop: {}".format(shop))

    coffee = shop.buy_coffee(10)
    print("Bought coffee: {}".format(coffee))