class Prodavnica(object):
    def __init__(self,pib,naziv,adresa,broj_telefona):
        self.pib=pib
        self.naziv=naziv
        self.adresa=adresa
        self.broj_telefona=broj_telefona

class Artikal(object):
    def __init__(self,oznaka,naziv,opis,cena,na_akciji,kategorije,prodavnica):
        self.oznaka=oznaka
        self.naziv=naziv
        self.opis=opis
        self.cena=cena
        self.na_akciji=na_akciji
        self.kategorije=kategorije
        self.prodavnica=prodavnica

class Kategorija(object):
    def __init__(self,oznaka,naziv):
        self.oznaka=oznaka
        self.naziv=naziv

