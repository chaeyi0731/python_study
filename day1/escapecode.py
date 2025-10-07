##문자열을 여러줄로 출력하기
print("""Welcome!
Hello World!""")

#출력 내용
#Welcome!
#Hello World!
#같은 종류의 따옴표 3개로 문자열로 감싸면 줄바꿈이 가능하다.

#또한 escape code를 사용 하면 되는데 종류가 여러가지이다.
# \n 줄바꿈 
# \t 수평 탭(tap)
# \\ 백슬래시(\) 문자를 표현
# \' 작은 따옴표 표사
# \" 큰 따옴표 표시#

print("Welcome!\nHello World!")
#escape code를 사용한 예시 
# 출력내용 Welcome!
# Hello World!#

print("Welcome!\\nHello World!")

#\를 두번 쓸 경우 문자의 특수성이 사라지며 \n 도 출력 되는 것을 볼 수 있다.
#출력 결과 : Welcome!\nHello World!

print("""\"당신이 할 수 있다고 믿든,
할수 없다고 믿든,
믿는대로 될 것이다.\"
\t- 헨리 포드 -""")

#여기서 """는 줄바꿈 \"는 따옴표 표시 \t의경우는 문장 오른쪽 배치이다.
# 결과 
# "당신이 할 수 있다고 믿든,
#할수 없다고 믿든,
#믿는대로 될 것이다."
#	- 헨리 포드 -

#len() 홤수 length 길이라는 뜻으로 문자열의 길이를 나타낸다  

print(len("Hello World!"))

#결과 12
#빈칸도 숫자로 계산하기 때문이다.

#예시문제 
print('Apple은"사과를" 말합니다.')
print("\'Hello World\'")
print("\"안녕 나는 철수라고 해.\"")
print(len("맛집 투어!"))
print(len("12345"))
print("""A
B""")

#실행결과
# Apple은"사과를" 말합니다.
#'Hello World'
#"안녕 나는 철수라고 해."
#6
#5
#A
#B