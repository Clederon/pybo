from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
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
    migrate.init_app(app, db)
    # migrate 객체가 models.py 파일을 참조
    from . import models

    ## 블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app