
class Fakultet(object):

    def __init__(self,*args,**kwargs):
        self.__oznaka = kwargs.pop('oznaka', None)
        self.__naziv=kwargs.pop('naziv',None)
        self.__adresa=kwargs.pop('adresa',None)

    @property
    def oznaka(self):
        return self.__oznaka

    @oznaka.setter
    def oznaka(self, vrednost):
        if isinstance(vrednost, str):
            self.__oznaka = vrednost
        else:
            raise TypeError('Mora biti tipa string')
    @property
    def naziv(self):
        return self.__naziv
    @naziv.setter
    def naziv(self,vrednost):
        if isinstance(vrednost,str):
            self.__naziv=vrednost
        else:
            raise TypeError('Mora biti tipa string')

    @property
    def adresa(self):
        return self.__adresa

    @adresa.setter
    def adresa(self, vrednost):
        if isinstance(vrednost, str):
            self.__adresa = vrednost
        else:
            raise TypeError('Mora biti tipa string')
