#구구단.py
#단을 입력받아서 출력.
#정수외의 값은 다시 입력


def GuGu(n):
	result =[]
	for i in range(1,10):	
		result.append(n*i)
	return result

while(1):
	try: how = int(input("몇 단을 출력할까? : "))
	except ValueError: 
		print("정수로 다시 입력해!")
		continue
	if type(how) == type(1): break
print(GuGu(how))
