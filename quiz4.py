# 조건 1 편의상 댓글은 20명이 작성 아이디는 1~20
# 조건 2 댓글 내용과 상관없이 무작위 추첨, 중복 불가
# 조건 3 random 모듈의 shuffle과 sample을 활용

from random import *
users = list(range(1, 21)) # 1부터 20까지 숫자 생성(리스트로)
shuffle(users)
winners = sample(users, 4) # 1명은 치킨 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("-- 축하합니다 --")