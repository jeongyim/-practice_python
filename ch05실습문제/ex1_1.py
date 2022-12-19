# class Robot:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def show(self, color):
#         print("이름 : {}, 나이 : {}, 색깔 : {}색인 로봇이 만들어졌습니다.".format(self.name, self.age, color))

# robot1 = Robot("청소",20)
# robot2 = Robot("음식",20)
# robot3 = Robot("주문",20)

# robot1.show("화이트")
# robot2.show("주황")
# robot3.show("검정")


class Robot:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
        
    def show(self):
        print("이름: {0},나이:{1}세,색깔 :{2}색인 로봇이 만들어 졌습니다."\
            .format(self.name,self.age,self.color))

#로봇객체 3개 생성
robot1=Robot("청소 로봇",20,"화이트")
robot2=Robot("음식 로봇",20,"주황")
robot3=Robot("주문 로봇",20,"검정")
#show메소드를 이용한 로봇 정보출력
robot1.show()
robot2.show()
robot3.show()

