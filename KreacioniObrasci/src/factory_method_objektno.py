
import abc

class Product(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def who(self):
        pass

class Creator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def factory_method(self):
        pass

class ConcreteProductA(Product):

    def who(self):
        return "Product A"

class ConcreteProductB(Product):

    def who(self):
        return "Product B"

class ConcreteCreatorA(Creator):

    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):

    def factory_method(self):
        return ConcreteProductB()


def test(factory):
    print(factory.factory_method().who())

if __name__=="__main__":
    test(ConcreteCreatorA())
    test(ConcreteCreatorB())