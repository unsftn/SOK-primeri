from flask.globals import request
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect

from prodavnica import app
from prodavnica.injector_modules import Title, ListaProdavnica
from prodavnica.model import Prodavnica
from prodavnica.util import pronadji_prodavnicu


@app.route("/prodavnice")
def lista_prodavnica(title:Title,prodavnice:ListaProdavnica):
    return render_template("lista_prodavnica.html",title=title,prodavnice=prodavnice)

@app.route("/brisanje/prodavnice/<pib>")
def brisanje_prodavnice(prodavnice:ListaProdavnica,pib):
    pronadjena=None
    for p in prodavnice:
        if p.pib == pib:
            pronadjena=p
    if pronadjena is not None:
        prodavnice.remove(p)
    return redirect(url_for('lista_prodavnica'))

@app.route("/unos/prodavnice",methods=['GET','POST'])
def unos_prodavnice(title:Title,prodavnice:ListaProdavnica):
    if request.method=='GET':
        stari_pib=request.args.get('pib')
        p=pronadji_prodavnicu(prodavnice,stari_pib)
        if p is None:
            return render_template("unos_prodavnice.html",title=title)
        else:
            return render_template("unos_prodavnice.html",title=title,stari_pib=stari_pib,pib=p.pib,
                               naziv=p.naziv,adresa=p.adresa,broj_telefona=p.broj_telefona)
    else:
        greska_pib=None
        greska_naziv=None
        greska_adresa=None
        greska_broj_telefona=None
        pib = request.form['pib']
        naziv = request.form['naziv']
        adresa = request.form['adresa']
        broj_telefona= request.form['broj_telefona']

        try:
            stari_pib = request.form['stari_pib']
        except:
            stari_pib = None

        if pib is not None and pib =="":
            greska_pib="Morate uneti pib"
        if naziv is not None and naziv == "":
            greska_naziv="Morate uneti naziv"
        if adresa is not None and adresa == "":
            greska_adresa="Morate uneti adresu"
        if broj_telefona is not None and broj_telefona == "":
            greska_broj_telefona = "Morate uneti broj telefona"

        if greska_pib is None:
            p = pronadji_prodavnicu(prodavnice, pib)
            if p is not None:
                if (stari_pib is not None and stari_pib != pib) or stari_pib is None:
                    greska_pib = "Prodavnica sa tom vrednoscu pib-a vec postoji"

        if greska_pib is None and greska_adresa is None and greska_naziv is None and greska_broj_telefona is None:
            if stari_pib is None:
                    prodavnice.append(Prodavnica(pib,naziv,adresa,broj_telefona))
            else:
                p = pronadji_prodavnicu(prodavnice,stari_pib)
                p.pib=pib
                p.naziv=naziv
                p.adresa=adresa
                p.broj_telefona=broj_telefona
            return redirect(url_for('lista_prodavnica'))
        return render_template("unos_prodavnice.html",title=title,greska_pib=greska_pib,
                                   greska_naziv=greska_naziv,greska_adresa=greska_adresa,
                                   greska_broj_telefona=greska_broj_telefona,
                                   pib=pib,naziv=naziv,adresa=adresa,
                                   broj_telefona=broj_telefona,stari_pib=stari_pib
                                   )
