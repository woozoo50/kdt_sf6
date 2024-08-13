# 파일 쓰기 - 파일을 생성
# 파일 열기(open()) > 파일 쓰기(write()) > 종료(close())
# 절대 경로 : c:/디렉터리/파일.확장자
# 상대 경로 :
# 모드(mode) : 쓰기모드(w) , 읽기모드(r) , 추가 모드('a')

# 문자(글자)를 쓰기(저장)
# f = open("경로, "모드"")  / w는 기존 내용 다 사라지고 새로저장
f = open("c:/pyfile/file1.txt", "w")

f.write("Hello~ Python\n")
f.write("너무 더워\n")

# 숫자 저장
# f.write(100) #not int type error
num = 4 + 5
f.write(f'{num}\n')
f.write(str(num) + '\n')
f.write("100\n")
# f.write('音樂\n')
f.write('※★\n')
f.write('15.9\n')

f.close()
