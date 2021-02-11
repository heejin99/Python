# absent = [2, 5] # 결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
#         break
#     print("{0}, 책을 읽어봐.".format(student))

absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
index = 0
while index < 11:
    index += 1
    if index in absent:
        continue 
        # absent 리스트에 학생이 있으면 아래 수행 부분은 무시하고 while문으로 올라감
    elif index in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(index))
        break # no_book 리스트에 학생이 있으면 반복문 종료
    print("{0}, 책을 읽어봐.".format(index))