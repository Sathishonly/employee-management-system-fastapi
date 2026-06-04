from sqlalchemy import Column,Integer,String,DateTime,Boolean,Float,Date
from app.core.database import Base
from datetime import datetime,timezone

class employees(Base):
    
    __tablename__ = "employees"
    
    id = Column(Integer,primary_key=True,index=True)
    employee_code = Column(String,nullable=False,unique=True)
    name = Column(String,nullable=False,index=True)
    email = Column(String,nullable=False,unique=True,index=True)
    phone = Column(String, nullable=False)
    department = Column(String, nullable=False)
    designation = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    isactive = Column(Boolean,default=True)
    joining_date  = Column(Date,nullable=False)
    created_at = Column(DateTime,default= lambda : datetime.now(timezone.utc))
    updated_at = Column(DateTime,default= lambda : datetime.now(timezone.utc),onupdate=lambda : datetime.now(timezone.utc))