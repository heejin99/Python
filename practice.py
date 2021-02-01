# print('풍선')
# print("나비")
# print("ㅋ"*9)

# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))

# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3
# '''
# 장지정 바보
# '''

# print("우리집 "+animal+"의 이름은 "+name+"예요")
# print(name, "는 ",age, "살이며, ",hobby,"을 아주 좋아해요")
# print(name+"는 어른일까요? "+str(is_adult))

# print(5//3) # 1
# print(5%3) #2

# print(abs(-5)) # 절댓값
# print(pow(4,2)) # 4의 2승
# print(max(5,12)) # 최댓값
# print(min(5,2)) # 최솟값
# print(round(3.14)) # 3.14에 가까운 값 = 3
# print(round(4.99)) # 4.99에 가까운 값 = 5

# from math import *
# print(floor(4.99)) # 내림. 4
# print(ceil(3.14)) # 올림. 4
# print(sqrt(16)) # 제곱근. 4

# from random import *
# print(random()) # 0.0이상 1.0 미만의 임의의 값 생성
# print(random()*10) # 0.0이상 10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0~10 미만의 임의의 값 생성
# print(int(random()*10)+1) #1~10 이하의 임의의 값

# print(int(random()*45)+1) #1~45이하의 임의의 값

# print(randrange(1, 46)) #1~46미만의 임의의 값
# print(randint(1,45)) #1~45이하의 임의의 값

# sentence = """
# 나는 소녀이고
# 파이썬은 쉬움
# """
# print(sentence)

# jumin = "991029-2345678"

# print("성별: "+jumin[7])
# print("연: "+jumin[0:2]) #0~2직전까지(0,1)
# print("월: "+jumin[2:4])
# print("일: "+jumin[4:6])
# print("생년월일: "+jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리: "+jumin[7:])
# print("뒤 7자리(뒤에서부터): "+jumin[-7:])

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index+1) # 두번째 n
# print(index)
# print(python.find("n"))
# print(python.find("Java")) # 값이 없으면 -1 출력
# #print(python.index("Java")) # 값이 없으면 에러 메시지 출력하며 프로그램 종료
# print(python.count("n"))

# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple은 %c로 시작해요." % "A")

# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요.." % ("파란", "빨간"))

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# # 3.6이상
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

print("백문이 불여일견 \n백견이 불여일타")
print("저는 '나도코딩'입니다")
print('저는 "나도코딩"입니다')
print("저는 \"나도코딩\"입니다")

# \\ : 문장 내에서 \
print("C:\\Users\\wkdgm\\OneDrive\\Documents\\Python")

# \r: 커서를 맨앞으로 이동
print("Red Apple\rPine")

#\b: 백스페이스(한글자 삭제)
print("Redd\bApple")

# \t: 탭
print("Red\tApple")