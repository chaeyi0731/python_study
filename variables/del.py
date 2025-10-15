#del은 변수 또는 요소를 삭제한다. 리스트에서 요소를 삭제하면 뒤에 요소들이 한칸씩 앞으로 당겨진다.

beverage_list = ["아메리카노","키푸치노","라떼","녹차","유자차"]

del beverage_list[2]
print(beverage_list) #['아메리카노', '키푸치노', '녹차', '유자차']

#del과 슬라이싱을 사용하여 여러 요소를 삭제 할 수 있다.

nickname = ["Amy","Oliver","Rei","Kali","Joy"]

del nickname[3:]
print (nickname) #['Amy', 'Oliver', 'Rei']

del nickname[:]
print (nickname) # [] -> 빈리스트 만들기도 가능하다.

#del 문으로 리스트 변수 자체를 삭제 할 수있다.

del beverage_list
print(beverage_list) #NameError: name 'beverage_list' is not defined