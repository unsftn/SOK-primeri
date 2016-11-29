from flask.globals import request
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect

from prodavnica import app
from prodavnica.injector_modules import Title, ListaArtikala, ListaProdavnica, ListaKategorija
from prodavnica.model import Artikal
from prodavnica.util import pronadji_artikal, convert_to_float, convert_to_boolean, pronadji_prodavnicu, \
    pronadji_kategoriju


@app.route("/artikli")
def lista_artikala(title:Title,artikli:ListaArtikala):
    return render_template("lista_artikala.html",title=title,artikli=artikli)

@app.route("/brisanje/artikla/<oznaka>")
def brisanje_artikla(artikli:ListaArtikala,oznaka):
    a=pronadji_artikal(artikli,oznaka)
    if a is not None:
        artikli.remove(a)
    return redirect(url_for('lista_artikala'))

@app.route("/unos/artikla",methods=['GET','POST'])
def unos_artikla(title:Title,artikli:ListaArtikala,prodavnice:ListaProdavnica,lista_kategorija:ListaKategorija):
    if request.method=='GET':
        stara_oznaka=request.args.get('oznaka')
        a=pronadji_artikal(artikli,stara_oznaka)
        if a is None:
            return render_template("unos_artikla.html",title=title,prodavnice=prodavnice,lista_kategorija=lista_kategorija)
        else:
            return render_template("unos_artikla.html",title=title,stara_oznaka=stara_oznaka,oznaka=a.oznaka,
                               naziv=a.naziv,opis=a.opis,cena=a.cena,na_akciji=a.na_akciji,kategorije=a.kategorije,
                               prodavnica=a.prodavnica,prodavnice=prodavnice,lista_kategorija=lista_kategorija)
    else:
        greska_oznaka=None
        greska_naziv=None
        greska_opis=None
        greska_cena=None
        greska_na_akciji = None
        greska_kategorije = None
        greska_prodavnica = None
        oznaka = request.form['oznaka']
        naziv = request.form['naziv']
        opis = request.form['opis']
        cena, cena_converted = convert_to_float(request.form['cena'])
        try:
            na_akciji, na_akciji_converted = convert_to_boolean(request.form['na_akciji'])
        except:
            na_akciji=False

        kategorije_lista = request.form.getlist('kategorije')
        prodavnica = request.form['prodavnica']


        try:
            stara_oznaka = request.form['stara_oznaka']
        except:
            stara_oznaka = None

        if oznaka is not None and oznaka =="":
            greska_oznaka="Morate uneti oznaku"
        if naziv is not None and naziv == "":
            greska_naziv="Morate uneti naziv"
        if opis is not None and opis == "":
            greska_opis="Morate uneti opis"
        if cena is not None and cena == "":
            greska_cena="Morate uneti cenu"

        if kategorije_lista is not None and kategorije_lista == "":
            greska_kategorije="Morate izabrati kategorije"
        if prodavnica is not None and prodavnica == "":
            greska_prodavnica="Morate izabrati prodavnicu"

        if not cena_converted:
            greska_cena="Morate uneti decimalnu vrednost za cenu"
        if greska_prodavnica is None:
            p=pronadji_prodavnicu(prodavnice,prodavnica)
            if p is not None:
                prodavnica=p
            else:
                greska_prodavnica="Izabrana prodavnica ne postoji"
        if greska_oznaka is None:
            a = pronadji_artikal(artikli, oznaka)
            if a is not None:
                if (stara_oznaka is not None and stara_oznaka != oznaka) or stara_oznaka is None:
                    greska_oznaka = "Artikal sa tom vrednoscu oznake vec postoji"

        kategorije=[]
        for k_oznaka in kategorije_lista:
            k=pronadji_kategoriju(lista_kategorija,k_oznaka)
            kategorije.append(k)
        if len(kategorije)==0:
            greska_kategorije="Morate izabrati kategoriju"

        if greska_oznaka is None and greska_naziv is None and greska_opis is None and greska_cena is None \
                and greska_na_akciji is None and greska_kategorije is None and greska_prodavnica is None:
            if stara_oznaka is None:
                    artikli.append(Artikal(oznaka,naziv,opis,cena,na_akciji,kategorije,prodavnica))
            else:
                a = pronadji_artikal(artikli,stara_oznaka)
                a.oznaka=oznaka
                a.naziv=naziv
                a.opis=opis
                a.cena=cena
                a.na_akciji=na_akciji
                a.kategorije=kategorije
                a.prodavnica=prodavnica
            return redirect(url_for('lista_artikala'))
        return render_template("unos_artikla.html",title=title,greska_oznaka=greska_oznaka,
                                   greska_naziv=greska_naziv,greska_opis=greska_opis,
                                   greska_cena=greska_cena, greska_na_akciji=greska_na_akciji,
                                   greska_kategorije=greska_kategorije,greska_prodavnica=greska_prodavnica,
                                   oznaka=oznaka,naziv=naziv,opis=opis,
                                   na_akciji=na_akciji,
                                   kategorije=kategorije,prodavnica=prodavnica,
                                   prodavnice=prodavnice, lista_kategorija=lista_kategorija
                                   )
