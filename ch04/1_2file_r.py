#<파일 읽어오기>
#읽어올 파일을 open한다.
test_file=open("test.txt","r",encoding="utf8")
print(test_file.read()) # test_file의 모든 내용을 읽어 온다.
test_file.close()#파일을 닫아준다.
print('-------------------')
#한줄 한줄씩 읽어오기
test_file=open("test.txt","r",encoding="utf8")
while True:
    line=test_file.readline()#한줄 읽어오고 커서는 다은 줄로 이동
    if not line:# line에 저장되는 값이 없으면
        break  #중단하고 while문을 빠져나간다.
    print(line,end="")#아니면 라인내용을 출력한다.
test_file.close()
print('----------------------')
#<읽어온 파일을 list형태로 저장 후 출력>
test_file=open("test.txt","r",encoding="utf8")
lines = test_file.readlines() #모든 라인을 읽어 와서 리스트 형태로 저장해 준다.
for line in lines:  #리스트에서 한줄씩 읽어 와서 출력
    print(line,end="")
test_file.close()#파일을 닫아준다.

