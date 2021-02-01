# 규칙1 http:// 제외
# 규칙 2 처음 만나는 점 . 이후 부분 제외
# 규칙 3 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

url = "http://naver.com"
url = "http://daum.net"
first = url.replace("http://","") # 규칙 1
first = first[:first.index(".")] # 규칙 2

pw = first[:3] + str(len(first)) + str(first.count("e")) + "!"

print("{0}의 비밀번호: {1}".format(url, pw))
print(f"{url}의 비밀번호: {pw}")