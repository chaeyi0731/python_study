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