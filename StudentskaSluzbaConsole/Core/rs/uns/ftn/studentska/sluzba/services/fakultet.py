import abc


class ServiceBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def identifier(self):
        pass

    @abc.abstractmethod
    def name(self):
        pass

class FakultetUcitatiBase(ServiceBase):

    @abc.abstractmethod
    def ucitati_fakultete(self):
        pass

class FakultetPrikazBase(ServiceBase):

    @abc.abstractmethod
    def prikazati_fakultete(self, lista_fakulteta):
        pass
