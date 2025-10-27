from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import env_variables

engine=create_engine(env_variables.dburl)
SessionLocal=sessionmaker(autoflush=True,bind=engine)
Base=declarative_base()
def get_db():
  db=SessionLocal()
  try:
    yield db
  finally:
    db.close()
