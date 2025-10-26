import sys
from copy import deepcopy
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from alembic.config import command,Config
from fastapi_app.database import get_db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fastapi.testclient import TestClient
import pytest
from fastapi_app.hello import app

sqlalchemyurl="postgresql://postgres:new_password@localhost:5432/fastapitest"
engine=create_engine(url=sqlalchemyurl)
session=sessionmaker(bind=engine,autoflush=True)
@pytest.fixture
def database():
  print("database fixture started ")

  command.downgrade(config=Config("alembic.ini"),revision="base")
  command.upgrade(config=Config("alembic.ini"),revision="heads")
  db=session()
  try:
    yield db
  finally:
    db.close()
    print("database fixture finished")


    
@pytest.fixture
def client2(database):
  def override_origdb():
    try:
      yield database
    finally:
      database.close()
  app.dependency_overrides[get_db]=override_origdb
  yield TestClient(app)


@pytest.fixture
def client(database):
  def override_origdb():
    try:
      yield database
    finally:
      database.close()
  app.dependency_overrides[get_db]=override_origdb
  yield TestClient(app)


@pytest.fixture
def create_user2(client2):
    response=client2.post("/users/",json={"username":"ahmad","userpassword":"ahmad","useremail":"ahmad@gmail.com"})
    response=response.json()
    response["password"]="ahmad"
    return response

@pytest.fixture
def test_authorized2(client2,create_user2):
      
      response=client2.post("/user/login",data={"username":"ahmad","password":"ahmad"})


      try:
        del client2.headers["Authorization"]
      except KeyError:
          pass
      client2.headers["Authorization"]=f"Bearer {response.json()["access_token"]}"
  

     
      return client2
@pytest.fixture
def create_user(client):
  
  response=client.post("/users/",json={"username":"rashid","userpassword":"rashi","useremail":"rashi@gmail.com"})
  assert response.status_code==201
  resp=response.json()
  # resp.pop("useremail")
  resp["password"]="rashi"
  
  return resp
@pytest.fixture
def test_authorized(client,create_user):
  resp=client.post("/user/login",data={"username":create_user["username"],"password":create_user["password"]})
  try:
    del client.headers["Authorization"]
  except KeyError:
     pass
  client.headers["Authorization"]=f"Bearer {resp.json()["access_token"]}"

  return client



