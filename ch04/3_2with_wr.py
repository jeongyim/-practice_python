#<with를 이용해서 파일 쓰고 읽기>
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("김종국은 열심히 운동을 하고 있어요")
with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())
#파일을 쓰는 것도 두 문장, 읽는 것도 두문장으로 간단하게 할 수 있다.
