#형 변환을 해보자
#? 형변환이란 어떤 값의 데이터 타입을 다른 데이터 타입으로 변환하는 작업이다. 
#문자열과 숫자를 형 변환 없이 더하면 타입 에러발생 
# ex


#int() 함수를 사용하여 실수형 또는 문자열을 정수형으로 변환하는 함수다

print(int("123")+456)
# 579

num = "123"
print(int(num[0])+int(num[1])+int(num[2]))
#6

#! 정수로 해석할 수 없는 문자열은 형 변환 불가 

#str()함수는 정수형,실수형,리스트 등을 문자열로 변환하는 함수

print("123"+str(456)) #123456

phone_number= 821012345678
print("전화번호:"+str(phone_number)) #전화번호:821012345678

# f-string은 변수를 포함 할 수 있는 문자열 문자열 앞에 f를 붙이고 문자열 내 변수를 중괄호로 감싸서 넣는다. 암시적으로 문자열로 변환된다

drink = "아메리카노"
count=2
sample_string=f"나는 오늘 {drink}를 {count} 잔 마셨다."
print(sample_string)
#나는 오늘 아메리카노를 2 잔 마셨다.
# 하나의 f-string 에 여러개 변수를 넣을수 있다.

sample_string=f"나는 오늘 '{drink}'를 {count} 잔 마셨다."
print(sample_string)