from passlib.context import CryptContext
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES,REFRESH_TOKEN_EXPIRE_DAYS,ALGORITHM,SECRET_KEY
from jose import JWTError,jwt
from datetime import datetime,timedelta,timezone


passcrypt = CryptContext(schemes=['argon2'],deprecated="auto")

def hashpassword(password:str):
    
    return passcrypt.hash(password)


def verifypassword(plainpassord:str,hashedpassword:str):
    
    return passcrypt.verify(plainpassord,hashedpassword)


def createaccesstoken(data: dict):
    
    orgdata = data.copy()
    
    exptime = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    orgdata.update({
        "exp" : exptime
    })
    
    token = jwt.encode(orgdata,SECRET_KEY,algorithm=ALGORITHM)
    
    return token


def createrefreshtoken(data: dict):
    
    orgdata = data.copy()
    
    exptime = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    
    orgdata.update({
        "exp" : exptime
    })
    
    token = jwt.encode(orgdata,SECRET_KEY,algorithm=ALGORITHM)
    
    return token