import sys


class SingletonA():

    __instance=None

    @classmethod
    def getInstance(cls):
        if SingletonA.__instance is None:
            SingletonA.__instance=SingletonA()
        return SingletonA.__instance


class SingletoneB(object):
    __instance = None

    def __new__(cls, val):
        if SingletoneB.__instance is None:
            SingletoneB.__instance = object.__new__(cls)
            SingletoneB.__instance.val = val
        return SingletoneB.__instance


if __name__=="__main__":
    s1=SingletonA.getInstance()
    print(s1)
    s2=SingletonA.getInstance()
    print(s2)
    try:
        SingletonA.__instance
    except:
        print(sys.exc_info())

    SingletoneB