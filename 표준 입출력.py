# print("Python", "Java", sep=",", end="?") # end 문장의 끝 부분을 ?로 바꿔달라

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기 순번표
for num in range(1, 21):
    print("대기번호: "+str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ") # 항상 문자열 형태로 입력 받음
print(type(answer))
print("입력하신 값은 "+answer+"입니다.")