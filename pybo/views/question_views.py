from datetime import datetime
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from ..import db # from pybo import db 
from pybo.models import Question
from ..forms import QuestionForm, AnswerForm

## 블루프린트 객체 생성 : 이름, 모듈명, URL 프리픽스
# URL 프리픽스 : 특정 파일(main_views.py)에 있는 함수의 애너테이션 URL 앞에 기본으로 붙일 접두어 URL
# 만약, / 대신 /main으로 변경하면 URL은 localhost:5000/이 아니라 localhost:5000/main/으로 변경
bp = Blueprint('question', __name__, url_prefix = '/question')

# 특정 주소에 접속할 시 바로 다음 줄에 있는 함수 호출
@bp.route('/list/')
def _list() :
    # 작성 일시를 기준으로 역순으로 정렬
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', 
                            question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id) :
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',
                            question=question, form = form)

@bp.route('/create/', methods=('GET', 'POST'))
def create() :
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit() :
        question = Question(subject = form.subject.data, content = form.content.data, create_date = datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form)