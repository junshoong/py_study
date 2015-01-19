#tab_to_4_space.py
#vim을 활용한 python프로그램 
#코딩도장 lv.1 탭을 공백문자 4개로 바꾸기

def conv_tab(text):
	result = text.replace("\t","    ")
	return result

text = input("변환할 문자열")

print(conv_tab(text))
