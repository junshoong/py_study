#나도 도전한다. 피보나치킨
# 2014.12.15 실패하였다..

limit =10000000
a=1
b=1
c = [a,b]
print("피보나치!")
while(1):
	if b >= limit:
		break
	a += b
	b += a
	c.append(a)
	c.append(b)

how = int(input("값:"))

for i in c:
	if how > i:
		pibo = i
		

print("바로 전의 값 : %d" % pibo)