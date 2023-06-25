## __init__ : db = SQLAlchemy()
from pybo import db

class Question(db.Model) :
    # 질문 데이터의 고유 번호
    id = db.Column(db.Integer, primary_key=True)
    # 질문 제목
    subject = db.Column(db.String(200), nullable = False)
    # 질문 내용
    content = db.Column(db.Text(), nullable = False)
    # 질문 작성일시
    create_date = db.Column(db.DateTime(), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'), nullable = False)
    user = db.relationship('User', backref = db.backref('question_set'))

    modify_date = db.Column(db.DateTime(), nullable = True)

class Answer(db.Model) :
    # 답변 데이터의 고유 번호
    id = db.Column(db.Integer, primary_key=True)
    # 질문 데이터의 고유 번호
    question_id = db.Column(db.Integer,
                            db.ForeignKey('question.id', ondelete = 'CASCADE')) # question.id : 연결할 기존 모델의 속성 / CASCADE : 삭제 연동 설정
    question = db.relationship('Question', backref = db.backref('answer_set', cascade = 'all, delete-orphan')) # backref : 역참조 설정 / cascade : 질문에 달린 답글들 모두 삭제
    # 질문 내용
    content = db.Column(db.Text(), nullable = False)
    # 질문 작성일시
    create_date = db.Column(db.DateTime(), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'), nullable = False)
    user = db.relationship('User', backref = db.backref('answer_set'))

    modify_date = db.Column(db.DateTime(), nullable = True)

class User(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
