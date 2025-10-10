#파이썬에서 변수는 어떻게 칭할까? 자스와 같이 =로 대입한다.

i = "Hello World!"

#변수는 만드는 규칙이 있다 문자 숫자 언더스코어만 사용해야한다.
#변수는 숫자로 시작할 수 없다 why? = 에러 발생 한다.
#파이썬은 대문자와 소문자를 구별 하기에 유의하여야한다.

print(i)

#변수명은 정확히..! 변수의 용도르 담아 지으면 협업시 편하다.

print("파이썬 할 수 있선!")
print("파이썬 할 수 있선!")
print("파이썬 할 수 있선!")
print("파이썬 할 수 있선!")

#일일히 치지 않고 변수로 지정해보자

closing = "파이썬 할 수 있썬!"

print(closing)
print(closing)
print(closing)
print(closing)

#깔끔히 읽기 좋은 코드

favorite_food = "chocolate"
print("I love" + favorite_food)

#변수와 스트링 합침 가능 

preference = "mint "

print ("I love "+ preference + favorite_food)

#스트링 + 변수 + 변수 가능하다

preference = "dark"
print("I love "+preference + favorite_food)

#변수의 값을 변하게 할 수 있다 . 변수를 업데이트 하다.

# 변수 업데이트 방식 
#1
num = 4
num = 3

#변수의 새로운 값을 할당하는 것으로 변수를 업데이트 할 수 있다.
#2
#복합 대입 연산자 를 적용한다
#변수의 기존값에 새로운 값을 더하고 빼거나 나누고 곱해서 그 결과를 변수에 다시 할당하는 것이다.

num+= 1
print(num)

#결과는 4로 나온다 즉 num이었던 3에 1을 더하여 업데이트 된것 