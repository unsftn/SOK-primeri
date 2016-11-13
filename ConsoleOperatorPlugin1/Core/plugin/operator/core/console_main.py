import pkg_resources


def racunanje(operatori):
    try:
        prvi = unesi_broj("Unesite prvi broj:")
        drugi = unesi_broj("Unesite drugi broj:")

        operator = odredi_operator(operatori)

        rezultat = operator.operation(prvi, drugi)
        print("Rezultat je: {}".format(rezultat))
    except Exception as e:
        print(e)



def unesi_broj(poruka):
    nije_konvertovan = False
    while not nije_konvertovan:
        broj, nije_konvertovan = convert_to_int(input(poruka))
    return broj


def odredi_operator(operatori):
    while True:
        print("Izaberite operator koji zelite:")
        for i, o in enumerate(operatori):
            print(" {} {}  {}".format(i, o.operator_identifier(),o.operator_name()))
        izbor=unesi_broj("Unesite redni broj opcije:")
        if izbor >=0 and izbor < len(operatori):
            return operatori[izbor]


def convert_to_int(number,default=0):
    try:
        value=int(number)
        return value,True
    except:
        value=default
        return value, False


def load_plugins():
    operators=[]
    for ep in pkg_resources.iter_entry_points(group='core.operator'):
        o = ep.load()
        print("{} {}".format(ep.name, o))
        operator = o()
        operators.append(operator)
    return operators

def main():
    try:
        operatori = load_plugins()
        if (len(operatori) == 0):
            print("Nije pronadjen ni jedan plugin")
            return
    except:
        pass

    while True:
        print("---------------------------------------------")
        racunanje(operatori)
        izbor = input("Unesite Enter za dalje ili q za izlaz:")
        if izbor == "q":
            break

if __name__ == "__main__":
    main()