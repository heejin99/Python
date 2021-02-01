# Coca 서비스 이용 택시 기사님(50명)
# 조건 1 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수
# 조건 2 소요시간 5분~15분 사이의 승객만 매칭

from random import *
cnt = 0 # 총 탑승 승객 수

for person in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15: # 매칭 성공
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(person, time))
        cnt+=1
    else: # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(person, time))

print("총 탑승 승객 : {0} 분".format(cnt))