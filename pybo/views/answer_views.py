from datetime import datetime

from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

from pybo import db
from ..forms import AnswerForm
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

## method는 답변 저장 템플릿에 있는 form의 method 값과 일치해야함!
@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id) :
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit() :
        # name 속성이 'content'인 값
        content = request.form['content']
        answer = Answer(content = content, create_date = datetime.now())
        # 질문에 대한 답변들
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', question = question, form = form)