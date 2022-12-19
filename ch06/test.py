#package와 test.py는 ch6이라는 같은 폴더 안에 있다.
#import 구문에서는 항상 모둘이나 패키지 명만 사용할 수 있고 클래스나 함수명은 사용할 수 없다.
#from ~import구문에서는 클래스 명을 사용할 수 있다.


import package.rose
flower = package.rose.RoseClass()
flower.info()

#아래에서는 클래스 명이 사용가능하다.
from package.rose import RoseClass
flower=RoseClass()
flower.info()

#아래 같은 형태의 모듈명으로 임포트 할수도있다.
from package import tulip
flower=tulip.TulipClass()
flower.info()

