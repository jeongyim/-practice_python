class Aclass:
    def __init__(self, name):
        self.name = name
        print(name,"클래스가 생성되었습니다.")

class Bclass(Aclass):
    def __init__(self, name):
        #Aclass.__init__(self, name)
        super().__init__(name)
        print("Bclass 입니다.")

test = Bclass("좋은")

class Cclass:
    def __init__(self, name):
        self.name=name
        print("C 클래스입니다.")

class Dclass(Bclass, Cclass):
    def __init__(self, name):
        super().__init__(name)
        print("D클래스 입니다.")

print()
dclass = Dclass("좋은")

class Eclass(Cclass, Bclass):
    def __init__(self, name):
        super().__init__(name)
        print("Eclass입니다.")
print()
eclass = Eclass("좋은")