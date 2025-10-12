import bcrypt

def hashpassword(password:str)->str:
  return bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
def validpassword(attemptedpass:str,hashedpass:str)->bool:
  return bcrypt.checkpw(attemptedpass.encode('utf-8'),hashedpass.encode('utf-8'))
