from pydantic_settings import BaseSettings

class Env(BaseSettings):
  dbhost:str
  dbport:str
  dbname:str
  dbusername:str
  dbpassword:str
  secretkey:str
  access_token_expires_minutes:int
  algorithm:str
  class Config:
    env_file=".env"
  
env_variables=Env()
  
