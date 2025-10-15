#append메서드는 리스트의 끝에 요소 추가 

nickname = ["Amy","Oliver","Rei","Kali","Joy"]
print(nickname) #['Amy', 'Oliver', 'Rei', 'Kali', 'Joy']

nickname[3] = "Kelly"
print(nickname) #['Amy', 'Oliver', 'Rei', 'Kelly', 'Joy']

nickname[4] = "Jay"
print(nickname) #['Amy', 'Oliver', 'Rei', 'Kelly', 'Jay']

nickname[0:2] = ["John","Tom"]
print(nickname)#['John', 'Tom', 'Rei', 'Kelly', 'Jay']

# 지정한 인덱스에서 수정이 된다.

#append 사용 

nickname = ["Amy","Oliver","Rei","Kali","Joy"]
print(nickname)

nickname.append("Bella")
print(nickname) #['Amy', 'Oliver', 'Rei', 'Kali', 'Joy', 'Bella'] 마지막에 벨라가 추가 되었다.

#한 개 뿐만 아닌 여러 개의 요소가 추가가 된다. 인자로 리스트를 전달하면 개별 요소가 리스트의 끝에 추가된다.

fruits=["딸기","바나나","사과"]
fruits.append(["수박","포도"])
print (fruits) #['딸기', '바나나', '사과', ['수박', '포도']]