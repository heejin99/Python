# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음

# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# demage = 5 # 유닛의 공격력

# print("{}유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, demage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있음. 일반 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_demage = 35

# print("{}유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_demage))

# def attack(name, location, demage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(\
#         name, location, demage))

# attack(name, "1시", demage)
# attack(tank_name, "1시", tank_demage)

class Unit:
    def __init__(self, name, hp, damage): # 생성자
        self.name = name # 멤버 변수(클래스 내 생성된 변수)
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # unit 클래스의 인스턴스
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력 {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = wraith1 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True
if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


