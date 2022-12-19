from random import *
#클래스 코드 1
class RunningMan:
    def __init__(self, name, tag):
        self.name = name
        self.tag = tag
        print("{}:런닝맨 멤버입니다.".format(name))
        print("이름표 접착력은 {}입니다.".format(tag))

    def move(self, location):
        print("{}:{}시 방향으로 이동합니다.".format(self.name, location))
    
# a= RunningMan("유재석", 50)
# a.move(5)

#클래스 코드 2  : 상속

class AttackMan(RunningMan):
    def __init__(self, name, tag, power): #가진힘 만큼 공격합니다.

        RunningMan.__init__(self,name,tag)
        self.power = power
    
    def attack(self, location):
        print("{}:{}시 방향으로 공격합니다.[공격력:{}]"\
            .format(self.name, location, self.power))

    def damaged(self, damage):
        print("{}:{}데미지를 입었습니다.".format(self.name, damage))
        self.tag -= damage
        if self.tag <= 0:
            print("{}:파괴되었습니다.".format(self.name))
        else:
            print("{}:현재 이름표 접착력은 {}입니다.".format(self.name, self.tag))

#test
# a=AttackMan("유재석",50,10)
# a.attack(5)
# a.damaged(50)

#test#클래스 코드 3 :다중상속, 메소드 오버라이딩
class Powerable:
    def __init__(self, super_power):
        self.super_power = super_power

#파워맨은 두개의 클래스를 상속받아 맴버변수를 초기화 해준다.
class PowerMan(AttackMan, Powerable):
    def __init__(self, name, tag, super_power):
        AttackMan.__init__(self, name, tag, 0) #일반 power은 사용하지 않을 것임으로 0으로 한다
        Powerable.__init__(self, super_power)
    
    def move(self, location): #메소드를 오버라이딩 

        print("{}은 {}시 방향으로 돌진합니다.".format(self.name, location))
    
    def attack(self, location): #메소드를 오버라이딩 

        print("{}:{}시 방향으로 슈퍼 공격합니다.[공격력:{}]"\
            .format(self.name, location, self.super_power))

# a= PowerMan("김종국", 50, 50)
# a.move(7)
# a.attack(9)

#class code 4:
#스피드맨  생성 :PowerMan클래스를 복붙하여 수정하여 만든다.
#super이용 생성
class SpeedMan(AttackMan):
    def __init__(self, name, tag, power):
        super().__init__(name,tag,power)

    def move(self, location): #메소드 오버라이딩
        print("{}:{}시 방향으로 빠르게 이동합니다.".format(self.name, location))

    def attack(self, location): #메소드 오버라이딩
        print("{}:{}시 방향으로 빠르게 공격합니다.[공격력:{}]"\
            .format(self.name, location, self.power))

# #SpeedMan test
# speedMan=SpeedMan("송지효",50,10)
# speedMan.move("5시")
# speedMan.attack("5시")
# speedMan.damaged(30)

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_stop():
    print("[알림] 게임을 종료합니다.")

#게임시작
game_start()
print("***<객체생성>***")

#객체생성
am1=AttackMan("유재석",50,20)
am2=AttackMan("전소민",50,15)
am3=AttackMan("이광수",50,10)
am4=AttackMan("지석진",50,10)
sm1=SpeedMan("송지효",50,15)
sm2=SpeedMan("송중기",50,20)
sm3=SpeedMan("하하",50,20)
sm4=SpeedMan("양세찬",50,20)
pm1=PowerMan("김종국",50,50)

#생성된 런닝맨을 일괄 관리하기 위하여 리스트에 넣어 준다.
runningMan = [am1,am2,am3,am4,sm1,sm2,sm3,sm4,pm1]
print("***<활동시작>***")
for run in runningMan:
    run.move(randint(1,12))#1~12사이의 방향으로 이동한다. 
print("***<공격 시작>***")
for run in runningMan:
    run.attack(randint(1,12))#1에서 12사이의 방향으로 공격 한다. 
print("***<손상을 입음>***")
for run in runningMan:
    run.damaged(randint(10,100))

game_stop()
