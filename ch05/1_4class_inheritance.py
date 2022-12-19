#클래스 코드 1
class RunningMan:
    def __init__(self, name, tag):
        self.name=name
        self.tag=tag
        print("{} : 런닝맨 맴버 입니다 ".format(name))
        print("이름표 접착력은{}입니다. ".format(tag))  
    #클래스 내 메소드 만들기
    def move(self, location):
        print("{}: {}방향으로 이동 합니다. ".format(self.name,location) )

#클래스 코드 2  : 상속
#부모클래스:RunningMan, 자식클래스 공격맨 :AttackMan
class AttackMan(RunningMan):
    def __init__(self, name, tag, power):#가진힘 만큼 공격합니다.
        RunningMan.__init__(self, name, tag) #부모클래스 생성자 호출
        self.power = power #자식클래스 생성자에서 데이터 초기화
    
    def attack(self, location):
        print("{0}:{1}방향으로 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.power))
    def damaged(self, damage):
        print("{0}:{1} 데미지를 입었습니다.".format(self.name, damage))
        self.tag -= damage
        if self.tag <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        else:
            print("{0} : 현재 이름표 접착력은 {1}입니다.".format(self.name, self.tag))

#객체 코드 1  :상속
# attMan3 = AttackMan("송지효",50,20)
# attMan3.move("3시")#부모클래스 메소드사용
# attMan3.attack("5시")
# attMan1 =AttackMan("유재석",50,20)
# attMan1.damaged(20)

#클래스 코드 3 :다중상속
class Powerable:
    def __init__(self, super_power):
        self.super_power=super_power
    
    def power_move(self, name, location):
        print("{0}은 {1}방향으로 돌진 합니다. ".format(name,location) )
    
#파워맨은 두개의 클래스를 상속받아 맴버변수를 초기화 해준다.
class PowerMan(AttackMan,Powerable):
    def __init__(self, name, tag, super_power):
        AttackMan.__init__(self, name, tag, 0)#일반 power은 사용하지 않을 것임으로 0으로 한다.
        Powerable.__init__(self, super_power)
    
    
    def power_attack(self, location):
        print("{0}:{1}방향으로 슈퍼 공격을 합니다. [공격력 {2}]"\
            .format(self.name, location, self.super_power))


#객체코드 2  : 다중상속
powerMan1=PowerMan("김종국",50,50)
#부모클래스 Powerable메소드사용
powerMan1.power_move(powerMan1.name,"3시")
#자식클래스 PowerMan 메소드 사용
powerMan1.power_attack("6시")
#부모클래스 AttackMan 메소드 사용
powerMan1.damaged(10)
#Runningman의 메소드 사용
powerMan1.move("2시")
