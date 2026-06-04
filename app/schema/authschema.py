from pydantic import BaseModel,EmailStr,Field

class userdata(BaseModel):
    
    id: int
    name: str
    email: EmailStr
    isactive: bool

    class Config:
        from_attributes = True
    
class userregister(BaseModel):
    
    name  : str = Field(...,example="test")
    email  : EmailStr = Field(...,example="testing@gmail.com")
    password : str = Field(...,min_length=6,example="password")
    
    
class userresponse(BaseModel):
    
    status_code  : int
    message : str
    data : userdata
    access_token : str
    refresh_token : str
    
    class Config():
        from_attributes = True
    
class login(BaseModel):
    
    email  : EmailStr = Field(...,example="testing@gmail.com")
    password : str = Field(...,min_length=6,example="password")
    
    
class requestschema(BaseModel):
    
    token : str
    