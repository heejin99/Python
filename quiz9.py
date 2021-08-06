# 자동주문 시스템
# 조건1 : 1보다 작거나 숫자가 아닌 입력값인 경우 ValueError로 처리
# 출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리 한장
# 치킨 소진 시 사용자 정의 에러[SoldoutError]를 발생시키고 프로그램 종료
# 출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

class SoldoutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg 

chicken = 10
waiting = 1 # 대기번호 1부터 시작
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? "))
        if order < 1:
            raise ValueError
        elif order > chicken: # 남은 치킨량보다 주문 수가 많을 때
            raise SoldoutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." \
                .format(waiting, order))
            waiting += 1
            chicken -= order
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldoutError as err:
        print(err)
        break
    