#<파일 이어쓰기>
test_file = open("test.txt","a",encoding="utf8")
test_file.writelines(["이름:김종국\n","나이:35\n","직업:예는인\n"])
test_file.close()