class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        print("{}은 런닝맨 멤버 입니다.".format(self.name))
        print("나이는 {}이고, 직업은 {}입니다.".format(self.age, self.job))


person1 = Person("유재석", 40, "코미디언")
person2 = Person("송지효", 30, "배우")
person3 = Person("김종국", 35, "가수")