# pickle 모듈 - 객체(리스트, 딕셔너리)의 형태 그대로 저장하고 읽을 수 있는 모듈
# 읽을 수 있는 모듈
# dump - 쓰기, load - 읽기
import pickle

with open('./output/data.txt', 'wb') as f:
    li = ['강아지', '닭', '고양이', '소']
    dict = {1: '고구마', 2: '옥수수', 3: '감자'}

    pickle.dump(li, f)
    pickle.dump(dict, f)

with open('./output/data.txt', 'rb') as f1:
    a = pickle.load(f1)
    b = pickle.load(f1)

    print(a)
    print(b)