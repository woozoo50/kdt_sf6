# with open(파일경로, 모드) as 파일객체 구문
# 자원 누수 방지를 위해서 f.close()를 사용하지 않음

try:
    team = ['서울', '인천', '부산', '광주', '대전', '대구']
    with open("./source/city.txt", "w") as f:
        for i in team:
            f.write(i + '\n')

    with open("./source/city.txt", "r") as f:
        data = f.read()
        print(data)

except FileNotFoundError:
    print("File not found")