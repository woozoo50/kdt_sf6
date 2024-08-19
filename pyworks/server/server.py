from flask import Flask # 클래스

app = Flask(__name__) # 생성자 , Flask 클래스의 app 객체를 생성

# 웹 페이지의 경로 설정 - 라우팅
@app.route('/') # 루트 경로 127.0.0.1:5000 , 5000은 포트 번호
def index(): # 모든 사이트의 첫페이지를 인덱스라고 함
    return '<h1>Hello Flask!</h1>'  # 문자를 루트 페이지에 보냄 .. HTML Tag <h1>

@app.route('/signup')  # 루트 경로 127.0.0.1:5000/signup
def signup():
    return "회원가입 페이지입니다."

@app.route('/shopping')  # 루트 경로 127.0.0.1:5000/signup
def shop():
    return "쇼핑 페이지입니다."

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()

# 문자를 반환하는 것 보다는
# 서버에서 웹 문서를 밯놘 - a.html
# 인터넷 언어 - html , css