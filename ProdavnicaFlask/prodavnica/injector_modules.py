from injector import Key, Module, provider, singleton

from prodavnica.model import Prodavnica, Artikal, Kategorija
from prodavnica.util import pronadji_kategoriju, pronadji_prodavnicu

ListaProdavnica=Key("ListaProdavnica")
ListaArtikala=Key("ListaArtikala")
ListaKategorija=Key("ListaKategorija")
Title=Key("Title")

class GlobalFlask(Module):
    def configure(self, binder):
        binder.bind(Title,to="Evidencija prodavnica")

    @singleton
    @provider
    def provides_lista_prodavnica(self)->ListaProdavnica:
        lista_prodavnica=[]

        lista_prodavnica.append(Prodavnica("2345","Market","Adresa 1","0213333333"))
        lista_prodavnica.append(Prodavnica("1578","Megamarket","Adresa 2","02355444"))
        lista_prodavnica.append(Prodavnica("3456","Krojac","Adresa 3","01178321"))
        return lista_prodavnica

    @singleton
    @provider
    def provides_lista_artikala(self,prodavnice:ListaProdavnica,kategorije:ListaKategorija)->ListaArtikala:
        lista_artikala=[]
        lista_artikala.append(Artikal("P1","Mleko","Mleko 1L",30.2,True,
                                      [pronadji_kategoriju(kategorije,"K5")],
                                      pronadji_prodavnicu(prodavnice,"1578")))
        lista_artikala.append(Artikal("P2","Najlepse zelje cokolada","200g",70.0,False,
                                      [pronadji_kategoriju(kategorije,"K3"),pronadji_kategoriju(kategorije,"K1")]
                                      ,pronadji_prodavnicu(prodavnice,"1578")))
        lista_artikala.append(Artikal("P3", "Pantalone", "Pamucne pantalone", 70.0, False,
                                      [pronadji_kategoriju(kategorije,"K10"),
                                       pronadji_kategoriju(kategorije,"K12")],
                                      pronadji_prodavnicu(prodavnice,"3456")))
        lista_artikala.append(Artikal("P4", "Kaput", "Pamucni kaput", 7000.0, False,
                                      [pronadji_kategoriju(kategorije,"K10"),
                                       pronadji_kategoriju(kategorije,"K11")],
                                      pronadji_prodavnicu(prodavnice,"3456")))
        return lista_artikala

    @singleton
    @provider
    def provides_lista_kategorija(self) -> ListaKategorija:
        lista_kategorija = []
        lista_kategorija.append(Kategorija("K1","Slatko"))
        lista_kategorija.append(Kategorija("K2","Slano"))
        lista_kategorija.append(Kategorija("K3", "Cokolada"))
        lista_kategorija.append(Kategorija("K4", "Keks"))
        lista_kategorija.append(Kategorija("K5", "Mlecni proizvodi"))
        lista_kategorija.append(Kategorija("K6", "Voda"))
        lista_kategorija.append(Kategorija("K7", "Gazirano"))
        lista_kategorija.append(Kategorija("K8", "Negazirano"))
        lista_kategorija.append(Kategorija("K9", "Obuca"))
        lista_kategorija.append(Kategorija("K10", "Odeca"))
        lista_kategorija.append(Kategorija("K11", "Jakna"))
        lista_kategorija.append(Kategorija("K12", "Pantalone"))
        return lista_kategorija