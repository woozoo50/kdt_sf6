# 파일 읽기 - 기존의 파일의 내용 읽기
# 파일 열기(open()) > 파일 읽기(read()) > 종료(close())
# 절대 경로 : c:/디렉터리/파일.확장자
# 상대 경로 :
# 모드(mode) : 쓰기모드(w) , 읽기모드(r)

# f = open("경로, "모드"")
f = open("c:/pyfile/file1.txt", "r")

data = f.read()
print(data)

f.close()
