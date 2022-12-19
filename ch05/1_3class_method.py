#클래스 코드 1
class RunningMan:
    def __init__(self, name, tag):
        self.name=name
        self.tag=tag
        print("{0} : 런닝맨 맴버 입니다 ".format(name))
        print("이름표 접착력은{0}입니다. ".format(tag))  
    #클래스 내 메소드 만들기
    def move(self, location):
        print("{0}: {1}방향으로 이동 합니다. ".format(self.name,location) )

#객체 생성 코드및 메소드 사용 코드
runningMan1=RunningMan("유재석",50)
runningMan2=RunningMan("송지효",50)
runningMan3=RunningMan("김종국",50)
print("---------------")
runningMan1.move("3시")
runningMan2.move("5시")
runningMan3.move("9시")
