# a1 = str(input("영어 문장을 입력 : "))
# print("입력된 문장의 길이는 : ", len(a1))
# print("각 단어의 첫 문자를 대문자로 변환 : ",a1.title() )
# print("모든 글자를 대문자로 변환 : ",a1.upper() )
# print("문자열에 a가 몇번 나타났는가 : ",a1.count("a") )
# print()
# print("입력된 문자열이 모두 숫자로만 구성되었는가? : ",a1.isdigit() )
# print("입력된 문자열이 모두 대문자로만 구성되었는가? : ",a1.isupper() )

st = input("영어문장 입력:")

print("입력된 문장의 길이 : ",len(st))
print("각 단어의 첫 문자를 대문자로 변환 : ",st.title() )
print("각 단어의 모든 글자를 대문자로 변환 :",st.upper())
print("문자열에 a가 몇 번 등장 : ",st.count("a"))
print("문자열이 모두 문자로만 구성? : ", st.isalpha())
print("문자열이 모두 숫자로만 구성? : ", st.isdigit())
print("문자열이 모두 대문자로만 구성?",st.isupper())
