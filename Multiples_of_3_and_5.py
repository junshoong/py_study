#If we list all the natural numbers below 10 that 
#are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#
#Multiples_of_3_and_5.py

def mul(var):
	cnt = 1
	max = 1000
	var_mul = [var]
	while(1):
		cnt = cnt + 1
		tmp = var * cnt
		if tmp >= max: break
		var_mul.append(tmp)
	return var_mul

def sum(List):
	result = 0
	for i in List:
		result = result+i
	return result

a=3
b=5
c=a*b
aList = mul(a)
bList = mul(b)
cList = mul(c)
x = sum(bList) + sum(aList) - sum(cList)
print(x)


