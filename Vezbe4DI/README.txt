U ovom primeru koriste se python anotacije koje su podrzane od python 3 verzije.
Za dependency injection se koristi injector modul koji podrzava python verzije 2.7/3.2+.
Za ovaj primer potrebno je instalirati injector sa PyPi sajta komandom

pip install injector

Da bi mogli da koristite pip komandu mozete instalirati po uputstvu sa sajta

https://pip.pypa.io/en/stable/installing/

Zatim treba instalirati virtualenv alat komandom

pip install virtualenv

Preporucljivo je injector instalirati u novom virtualnom okruzenju koristeci komandu

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
Project:Vezbe4DI->Project Interpreter
i otici na settings dugme i izabrati opciju
Add Local
i pronaci putanju gde je kreirano virtualno okruzenje i izabrati python interpreter

Za Linux

NAZIV_OKRUZENJA/bin/python

Za Windows

NAZIV_OKRUZENJA\Scrpits\python.exe