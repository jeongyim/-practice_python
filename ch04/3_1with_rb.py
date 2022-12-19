#with를 이용해서 간편하게 피클파일 읽어오기
import pickle
with open("test.pickle","rb") as test_file:#피클파일을 읽어 와서 test_file에 저장한다
    print(pickle.load(test_file))#파일을 로드해서 출력한다.

#열었던 파일에 대해서 따로 close()해줄 필요 없이 with문을 나오면 자동 close()된다. 

