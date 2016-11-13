import pkg_resources
from injector import Module, provider, Key

OperatorList=Key("OperatorList")

class GlobalFlask(Module):
    def configure(self, binder):
        binder.bind(str,to="Operator plugin")

    @provider
    def provides_plugin(self)->OperatorList:
        operators=[]
        for ep in pkg_resources.iter_entry_points(group='core.operator'):
            o = ep.load()
            print("{} {}".format(ep.name, o))
            operator=o()
            operators.append(operator)
        return operators