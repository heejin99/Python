# # for waiting_no in range(1,6): # 1 2 3 4 5
# #     print("대기번호: {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르","아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# while문
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
#     index -= 1
#     if (index == 0):
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# 한 줄 for문
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101 102 103 104
# students = [1,2,3,4,5]

# students = [i+100 for i in students]
# print(students)

# 학생 이름 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]

# students = [len(i) for i in students]
# print(students)

# 학생 이름 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)