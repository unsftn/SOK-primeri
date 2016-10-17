import copy


class ConcreatePrototype():
    def __init__(self):
        self.a=1
        self.list=[4,5,6]

    def clone(self):
        return copy.deepcopy(self)
    def __str__(self):
        return str(self.a)+" "+str(self.list)

def test(prototype):
    return prototype.clone()

if __name__=="__main__":
    c1=ConcreatePrototype()
    c2=test(c1)
    c3=test(c2)
    c2.a=4
    c2.list[0]=7
    c3.a = 8
    c3.list[1]=10
    print(c1)
    print(c2)
    print(c3)