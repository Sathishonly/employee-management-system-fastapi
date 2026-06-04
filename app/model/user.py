from sqlalchemy import Column,Integer,String,DateTime,Boolean
from app.core.database import Base
from datetime import datetime,timezone

class users(Base):
    
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False,index=True)
    email = Column(String,nullable=False,index=True,unique=True)
    password = Column(String, nullable=False)
    isactive = Column(Boolean,default=True)
    created_at = Column(DateTime,default= lambda : datetime.now(timezone.utc))
    updated_at = Column(DateTime,default= lambda : datetime.now(timezone.utc),onupdate=lambda : datetime.now(timezone.utc))