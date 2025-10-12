from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import env_variables
DATABASE_URL=f"postgresql://{env_variables.dbusername}:{env_variables.dbpassword}@metro.proxy.rlwy.net:21465/{env_variables.dbname}"

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autoflush=True,bind=engine)
Base=declarative_base()
def get_db():
  db=SessionLocal()
  try:
    yield db
  finally:
    db.close()
