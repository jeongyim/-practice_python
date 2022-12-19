from random import*
person=list()
for i in range(1,21):
    person.append(i)
print("추첨대상번호:",person)
shuffle(person)#섞어준다.
print("섞인 번호:",person)
winner=sample(person,3)
print("TV 당첨자 : {0} ".format(winner[0]))
print("냉장고 당첨자 : {0} ".format(winner[1:]))
