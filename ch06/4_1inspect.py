#random모듈의 위치 알아보기
import inspect
import random
print(inspect.getfile(random))
#출력결과 : C:\Python310\Lib\random.py
from package import rose
print(inspect.getfile(rose))
#출력결과
# rose.py모듈을 외부에서 호출하였습니다.
# c:\Users\박해옥\Desktop\test\basic\ch6\package\rose.py
