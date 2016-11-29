def pronadji_prodavnicu(prodavnice,pib):
    for p in prodavnice:
        if p.pib == pib:
            return p
    return None


def pronadji_artikal(artikli,oznaka):
    for a in artikli:
        if a.oznaka == oznaka:
            return a
    return None


def pronadji_kategoriju(kategorije,oznaka):
    for k in kategorije:
        if k.oznaka == oznaka:
            return k
    return None


def convert_to_float(number,default=0.0):
    try:
        value=float(number)
        return value,True
    except:
        value=default
        return value, False

def convert_to_boolean(number,default=False):
    try:
        value=bool(number)
        return value,True
    except:
        value=default
        return value, False