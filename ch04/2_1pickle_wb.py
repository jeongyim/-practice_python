#<pickle 파일 쓰기>
import pickle #피클이라는 모듈을 임포트 해 온다
test_file = open("test.pickle","wb")
data={"이름":"김종국","취미":["축구","노래","헬스"]}
pickle.dump(data,test_file)#data에 있는 정보를 test_file에 저장
test_file.close()#파일을 닫아준다.
#<실행결과>#  text.pickle파일이 만들어짐
