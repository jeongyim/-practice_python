from random import*
lotto = set()
for j in range(1,6):
    while(len(lotto)<6):
        a=randint(1,45)
        lotto.add(a)
    print(lotto)
    lotto.clear()