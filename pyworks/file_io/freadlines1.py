# readlines() - 데이터를 리스트로 변환

try:
    f = open("./source/season.txt", 'r')

    seasons = f.readlines()  # 데이터가 seasons 리스트에 저장됨

    print(seasons)
    print(seasons[-1])

    for season in seasons:
        print(season.strip())

    f.close()

    # 내부의 에러 메시지 보고 싶을 때
except FileNotFoundError as msg:
    print(msg)