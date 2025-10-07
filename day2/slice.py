#문자열 슬라이싱
#문자열 뒤 대괄호 안에 콜론(:) 기호를 사용해 인덱스 범위를 지정한다.

# 문자열 [a:b] 인덱스가 a인 문자부터 인덱스가 (b-1)인 문자까지 선택
# 문자열 [:b] 쳐음부터 인텍스가 (b-1)인 문자까지 선택
#문자열[a:] 인덱스가 a인 문자부터 끝까지 선택
#문자열[:] 문자열 전체를 선택

print("Mint Chocolate")
print("Mint Chocolate"[0:4])
#인덱스 4인 Mint 까지만 출력이 된다.
print("Mint Chocolate"[:4])
#또한 굳이 0을 넣지 않아도 Mint가 출력이 된다.

print("Mint Chocolate"[5:14])
#인덱스 5부터 14까지인 Chocolate 만 출력이 된다.
print("Mint Chocolate"[5:])
#위와 같이 마지막 인덱스를 적지 않아도 자동으로 Chocolate 만 출력이 된다.

print("Mint Chocolate"[:])
print("Mint Chocolate"[5:])
# 콜론만 넣을 경우 처음부터 끝까지 슬라이싱 하라는 의미이므로 Mint Chocolate 전체가 출력 된다.

#슬라이싱 간격 설정
#슬라이스 구문에 step을 추가해 특정 간격으로 문자를 선택 할 수 있다.
# Step을 2로 지정하면 문자를 2개마다 하나씩 선택한다.

#0부터 13까지의 2의 간격으로 선택
print("Mint Chocolate"[0:14:2])
#결과 Mn hclt

#처음부터 끝까지 5의 간격으로 선택
print("Mint Chocolate"[::5])
#결과 MCl