from flask import Blueprint, url_for
from werkzeug.utils import redirect

## 블루프린트 객체 생성 : 이름, 모듈명, URL 프리픽스
# URL 프리픽스 : 특정 파일(main_views.py)에 있는 함수의 애너테이션 URL 앞에 기본으로 붙일 접두어 URL
# 만약, / 대신 /main으로 변경하면 URL은 localhost:5000/이 아니라 localhost:5000/main/으로 변경
bp = Blueprint('main', __name__, url_prefix = '/')

@bp.route('/hello')
def hello_pybo() :
    return 'Hello, Pybo!'

# 특정 주소에 접속할 시 바로 다음 줄에 있는 함수 호출
@bp.route('/')
def index() :
    ## 이 주소로 리다이렉트 : bp 이름 question의 _list 함수
    return redirect(url_for('question._list'))