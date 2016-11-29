from flask.templating import render_template

from prodavnica import app
from prodavnica.injector_modules import Title, ListaKategorija


@app.route("/")
def index(title:Title):
    return render_template("index.html",title=title)

@app.route("/kategorije")
def lista_kategorija(title:Title,kategorije:ListaKategorija):
    return render_template("lista_kategorija.html",title=title,kategorije=kategorije)



