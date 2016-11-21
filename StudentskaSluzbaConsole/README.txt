U ovom primeru koriste se pkg_resources modul za implementaciju i prepoznavanje plugina.
Za ovaj primer potrebno je imati instaliran pip i setuptools.
Intaliranje plugina se pokrece komandom

python setup.py install

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
Project:StudentskaSluzbaConsole->Project Interpreter
i otici na settings dugme i izabrati opciju
Add Local
i pronaci putanju gde je kreirano virtualno okruzenje i izabrati python interpreter

Za Linux

NAZIV_OKRUZENJA/bin/python

Za Windows

NAZIV_OKRUZENJA\Scrpits\python.exe

Ovi primeri se mogu pokrenuti iz PyCharm razvojnog okruzenja ali potrebno je za setup.py
module napraviti posebne konfiguracije tako sto se ode na:
Run -> Edit configurations
Napravi se nova Python konfiguracija i za polje
Script:
se izabere jedan od tri setup.py modula i za polje
Script parameters:
se upise:
install

Ovo treba ponoviti za sve setup skripte koje se nalaze u projektu.