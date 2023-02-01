# Web Programming 2018112801 Koh Dong-Jae

#1. 이번 주말에 저녁 식사에 초대할 사람을 5명 dinner_guests 리스트로 작성하고, 출력합니다.
dinner_guests=['e','d','c','b','a']
print(dinner_guests)
#2. 갑자기 2번째와 3번째 손님이 불참하기로 합니다. 불참하는 손님의 이름을 출력합니다.
print(dinner_guests[1] +", "+ dinner_guests[2])
#3. 불참하기로 한 2번째와 3번째 손님을 dinner_guests에서 제거한 뒤, 남은 손님의 명단을 확인하기 위해 dinner_guests 리스트를 출력합니다.
dinner_guests.pop(1)
dinner_guests.pop(1)
print(dinner_guests)
#4. 마침 새 손님이 1분 오시기로 했습니다. 새 손님의 이름을 dinner_guests 리스트 마지막에 추가하고, dinner_guests 리스트를 출력합니다.
dinner_guests.append('f')
print(dinner_guests)
#5. 손님목록인 dinner_guests 리스트를 알파벳(또는 가나다)순서로 정렬한 뒤, dinner_guests 리스트에 저장된 각 손님의 이름 앞으로 초대 메세지를 출력합니다.
dinner_guests.sort()
for guest in dinner_guests:
    print("Dear "+guest+", Invite you")