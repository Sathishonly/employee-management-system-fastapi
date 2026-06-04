from pydantic import BaseModel,EmailStr,Field
from typing import Optional,List
from datetime import date

class employee(BaseModel):
    
    id : int
    employee_code : str
    name : str
    email : EmailStr
    phone : str
    department : str
    salary : float
    designation : str
    joining_date : date
    
    class Config:
        from_attributes = True


class employeecreate(BaseModel):
    
    employee_code : str
    name : str
    email : EmailStr
    phone : str
    department : str
    salary : float
    designation : str
    joining_date : date
    
    
class employeresponse(BaseModel):
    
    status_code : int
    message : str
    data : employee
    
    
class pageable(BaseModel):
    page : int
    limit : int
    total : int
    
    
class employeelist(BaseModel):
    
    status_code : int
    message : str
    data : List[employee]
    pageable : pageable
    
    
class employeeupdate(BaseModel):
    
    employee_code : Optional[str] = None
    name : Optional[str] = None
    email :  Optional[EmailStr] = None
    phone : Optional[str] = None
    department : Optional[str] = None
    salary : Optional[float] = None
    designation : Optional[str] = None
    joining_date : Optional[date] = None