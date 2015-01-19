#how_many_page.py
#입력: 총건수(m), 한 페이지에 보여줄 게시물수(n)(단, n>=1)
#출력: 총페이지수

def calc_page(post,view):
	if post%view == 0: page=post/view
	else: page=int(post/view)+1
	return page

m=int(input("게시물의 총 건수는 몇개 인가요? : "))
n=int(input("한 페이지에 보여줄 게시물의 수는 몇개인가요? : "))
print("총 페이지 수는 %s페이지 입니다." % int(calc_page(m,n)))

