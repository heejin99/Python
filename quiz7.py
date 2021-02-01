# 조건 파일명은 1주차.txt, 2주차.txt, ... 50주차.txt

for i in range(1, 51):
    with open(str(i)+"주차.txt","w",encoding="utf8") as company_file:
        # company_file.write("-"+str(i)+"주차 주간보고-\n")
        company_file.write("-{0}주차 주간보고-\n".format(i))
        company_file.write("부서:\n이름: \n업무요약:")
