from flask import Flask #패키지 불러오기
app = Flask(__name__)   #객체 인스턴스 생성하기

@app.route('/') #데코레이터 사용, url 경로
def hello_world():
    return 'Hello, DevOps!' #함수정의, 반환 문자열 지정

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=8080)