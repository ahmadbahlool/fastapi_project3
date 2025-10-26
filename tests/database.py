# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).parent.parent))
# from alembic.config import command,Config
# from fastapi_app.database import get_db
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from fastapi.testclient import TestClient
# import pytest
# from fastapi_app.hello import app

# sqlalchemyurl="postgresql://postgres:new_password@localhost:5432/fastapitest"
# engine=create_engine(url=sqlalchemyurl)
# session=sessionmaker(bind=engine,autoflush=True)
# @pytest.fixture
# def database():
#   print("database fixture started ")

#   command.downgrade(config=Config("alembic.ini"),revision="base")
#   command.upgrade(config=Config("alembic.ini"),revision="heads")
#   db=session()
#   try:
#     yield db
#   finally:
#     db.close()
#     print("database fixture finished")

    
  
# @pytest.fixture
# def client(database):
#   def override_origdb():
#     try:
#       yield database
#     finally:
#       database.close()
#   app.dependency_overrides[get_db]=override_origdb



#   yield TestClient(app)

