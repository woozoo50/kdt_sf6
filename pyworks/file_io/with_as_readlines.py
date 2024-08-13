# with open(파일경로, 모드) as 파일객체 구문
# 자원 누수 방지를 위해서 f.close()를 사용하지 않음

try:
    with open("./source/city.txt", "r") as f:
        # data = f.readlines()
        # data = f.readline().split()
        # print(data)

        a = []
        for i in range(6):
            city = f.readline().split()
            a.append(city)


        print(a[0])  # 서울
        print(a[-1])  # 대구
        print("=====")
        print(a[0][0])  # 서울
        print(a[-1][0])  # 대구

        for i in a:
            print(i)

except FileNotFoundError:
    print("File not found")