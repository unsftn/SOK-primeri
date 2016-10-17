def get_singleton():
    get_singleton.instance=None
    if get_singleton.instance is None:
        class Singletone():
            def __init__(self):
                pass
        get_singleton.instance=Singletone()
    return get_singleton.instance

if __name__=="__main__":
    s1=get_singleton()
    print(s1)
    s2=get_singleton()
    print(s1)
    s3=get_singleton()
    print(s1)

