#<파일 생성>
# 파일을 open하여 test.txt파일을 쓴다.
test_file = open("test.txt","w",encoding="utf8")
#문자열 하나 쓰기
test_file.write('신상정보\n') # write()는 줄바꿈기능이 없어 \n으로 줄바꿈을 해준다.
#3개의 문자열 행을 일괄적으로 파일에 쓰기
test_file.writelines(["이름 : 박찬성\n","나이 : 35\n","직업 : 엔지니어\n"])
#파일을 열고, 작업을 다하고 나면 반드시 닫아 줘야 한다.
test_file.close()