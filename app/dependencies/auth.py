from fastapi.security import OAuth2PasswordBearer
from jose import jwt,JWTError
from app.core.config import SECRET_KEY,ALGORITHM
from app.model.user import users
from app.core.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status


oauthschema = OAuth2PasswordBearer(tokenUrl="/login")

def getcurrentuser(token : str= Depends(oauthschema),db : Session = Depends(get_db)):
    
    try:
        
      decodetoken = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
      
      userId = decodetoken.get("userId")
      
      if not userId:
          
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Token")
      
      User =  db.query(users).filter(users.id == userId).first()
      
      if not User:
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User Not Found")
       
      return User
       
    except JWTError:
        
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Token")
