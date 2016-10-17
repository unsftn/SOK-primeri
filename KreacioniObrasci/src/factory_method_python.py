class ConcreteProductA():

    def who(self):
        return "Product A"

class ConcreteProductB():

    def who(self):
        return "Product B"

class ConcreteCreatorA():

    @classmethod
    def factory_method(cls):
        return ConcreteProductA()

class ConcreteCreatorB():

    @classmethod
    def factory_method(cls):
        return ConcreteProductB()


def test(factory):
    print(factory.factory_method().who())

if __name__=="__main__":
    test(ConcreteCreatorA)
    test(ConcreteCreatorB)