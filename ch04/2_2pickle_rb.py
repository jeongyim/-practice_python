#<pickle 파일 읽어오기>
import pickle 
test_file=open("test.pickle","rb")
data=pickle.load(test_file)#파일에 있는 정보를 data에 불러오기
print(data)
test_file.close()