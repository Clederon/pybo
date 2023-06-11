import os

BASE_DIR = os.path.dirname(__file__)

# 데이터베이스(SQLite) 접속 주소 : 데베 파일 pybo.db을 루트 디렉터리에 저장
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLAlchemy의 이벤트 처리 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False