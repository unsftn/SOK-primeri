U ovom primeru koristi se flask modul za implementaciju web aplikacije koja cuva evidenciju o prodavnicama.
Za ovaj primer potrebno je imati instaliran pip, setuptools, injector, flask i flask-injector.
Instaliranje plugina se pokrece komandom

python setup.py install

Instaliran primer se moze pokrenuti pokretanjem skripte prodavnica_main ili iz
PyCharm razvojonog okruzenja pokretanjem modula run_server.py
Preporucljivo je da se instaliranje vrsi u posebnom virtualnom okruzenju
Da bi mogli da koristite pip komandu mozete instalirati po uputstvu sa sajta

https://pip.pypa.io/en/stable/installing/

Zatim treba instalirati virtualenv alat komandom

pip install virtualenv

Kreirati novo virtualno okruzenje koristeci komandu

virtualenv NAZIV_OKRUZENJA

Kreirano virtualno okruzenje mozete aktivirati komandom

Za Linux

source NAZIV_OKRUZENJA/bin/activate

Za Windows

NAZIV_OKRUZENJA\Scripts\activate

Da bi se ovaj primer mogao pokrenuti potrebno je postaviti putanju do python interpretera
virtualnog okruzenja u PyCharm razvojnom okruzenju tako sto se ode na
File -> Settings
pronaci prikaz
Project:ProdavnicaFlask->Project Interpreter
i otici na settings dugme i izabrati opciju
Add Local
i pronaci putanju gde je kreirano virtualno okruzenje i izabrati python interpreter

Za Linux

NAZIV_OKRUZENJA/bin/python

Za Windows

NAZIV_OKRUZENJA\Scrpits\python.exe

Ovaj primer se moze pokrenuti iz PyCharm razvojnog okruzenja ali potrebno je za setup.py
modul napraviti posebnu konfiguraciju tako sto se ode na:
Run -> Edit configurations
Napravi se nova Python konfiguracija i za polje
Script:
se izabere setup.py modul i za polje
Script parameters:
se upise:
install

