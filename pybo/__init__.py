from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

db = SQLAlchemy()

naming_convention = {
    "ix" : "ix_%(column_0_label)s",
    "uq" : "uq_%(table_name)s_%(column_0_name)s",
    "ck" : "ck_%(table_name)s_%(column_0_name)s",
    "fk" : "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk" : "pk_%(table_name)s"
}

db = SQLAlchemy(metadata = MetaData(naming_convention = naming_convention))
migrate = Migrate()

def create_app() :

    ## Flask 어플리케이션 생성
    # __name__ : 모듈명(pybo.py의 pybo)
    app = Flask(__name__)
    # config.py 파일에 작성된 항목을 app.config 환경 변수로 불러줌.
    app.config.from_object(config)

    ## ORM
    # init_app : 초기화
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite") :
        migrate.init_app(app, db, render_as_batch = True)
    else :
        migrate.init_app(app, db)
    
    # migrate 객체가 models.py 파일을 참조
    from . import models

    ## 블루프린트
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    ## 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app