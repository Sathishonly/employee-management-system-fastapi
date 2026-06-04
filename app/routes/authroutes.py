from fastapi import APIRouter,Depends,status,HTTPException
from app.model.user import users
from app.core.database import get_db
from app.schema.authschema import userregister,login,userresponse,requestschema
from sqlalchemy.orm import Session
from app.core.security import hashpassword,verifypassword,createaccesstoken,createrefreshtoken
from jose import jwt,JWTError
from app.core.config import SECRET_KEY,ALGORITHM


router = APIRouter()

@router.post("/registeruser",response_model=userresponse)
def register(request : userregister, db: Session = Depends(get_db)):
    
    existinguser = db.query(users).filter(users.email == request.email).first()
    
    if existinguser:
        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail="Email already exists"
        )
        
    newuser = users(
       name = request.name,
       email = request.email,
       password = hashpassword(request.password),
       isactive = True
    )
    
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    
    accesstoken =createaccesstoken({"userId":newuser.id})
    refreshtoken = createrefreshtoken({"userId" : newuser.id})
    
    return {
        "status_code" : status.HTTP_201_CREATED,
        "message" : "User Resigter Successfully",
        "data" : newuser,
        "access_token" : accesstoken,
        "refresh_token" : refreshtoken
    }
    
    

@router.post("/login",response_model=userresponse)
def loginuser(request : login, db: Session = Depends(get_db)):
    
    user = db.query(users).filter(users.email == request.email).first()
    
    if not user:
         raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail="Email not exists"
        )
        
    password = verifypassword(request.password,user.password)
    
    if not password:
        
         raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail="Invalid Password"
        )
         
    accesstoken = createaccesstoken({"userId" : user.id})
    refreshtoken = createrefreshtoken({"userId" : user.id})
    
    return {
        "status_code" : status.HTTP_200_OK,
        "message" : "LogIn Successfully",
        "data" : user,
        "access_token" : accesstoken,
        "refresh_token" : refreshtoken
    }
    
    
@router.post("/refreshtoken")
def refreshtoken(refreshtoken: requestschema, db : Session = Depends(get_db)):
    
    try:
        
       decodetoken = jwt.decode(refreshtoken.token,SECRET_KEY,algorithms=[ALGORITHM])
       
       userId = decodetoken.get("userId")
       
       if not userId:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Token")
      
       user = db.query(users).filter(users.id == userId).first()
       
       if not user:
           raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User Not Found")
       
       accesstoken = createaccesstoken({"userId": userId})
       
       return {
           "status_code" : status.HTTP_200_OK,
           "data" : accesstoken
       }
       
    except JWTError as e:
        
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Invalid Refresh Token :{e}")