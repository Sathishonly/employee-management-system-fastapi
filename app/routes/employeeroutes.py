from fastapi import APIRouter,Depends,status,HTTPException
from app.model.employees import employees
from app.schema.employeeschema import employeecreate,employeresponse,employeelist,employeeupdate
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dependencies.auth import getcurrentuser
from datetime import date


router = APIRouter()

@router.post("/createemployee",response_model=employeresponse)
def createemployee(request:employeecreate,currentuser= Depends(getcurrentuser),db: Session = Depends(get_db)):
    
    existingemployee = db.query(employees).filter(employees.employee_code == request.employee_code).first()
    
    if existingemployee:

        raise HTTPException(
            status_code=400,
            detail="Employee Code Already Exists"
        )
        
        
    existingemail= db.query(employees).filter(employees.email == request.email).first()
    
    if existingemail:

        raise HTTPException(
            status_code=400,
            detail="Employee Email Already Exists"
        )
    
        
    newemployee = employees(
        employee_code = request.employee_code,
        name = request.name,
        email = request.email,
        phone = request.phone,
        department = request.department,
        salary = request.salary,
        designation = request.designation,
        joining_date = request.joining_date
    )
    
    db.add(newemployee)
    db.commit()
    db.refresh(newemployee)
    
    return {
        "status_code" : status.HTTP_201_CREATED,
        "message" : "Employee Resigter Successfully",
        "data" : newemployee
    }
    
    
@router.get("/getemployeelist",response_model=employeelist)
def employeelist(page : int = 1,limit : int = 8,search : str = "",fromdate : date = None,todate : date = None,db : Session = Depends(get_db),currentuser= Depends(getcurrentuser)):
   
   skip = (page-1) * limit
    
   query = db.query(employees)
   
   if search:
       
      query = query.filter(employees.name.ilike(f"%{search}%") | employees.email.ilike(f"%{search}%"))
       
   if fromdate and todate:

        query = query.filter(

            employees.joining_date >= fromdate,

            employees.joining_date <= todate
        )

       
   total = query.count()
   
   employeeslist = query.offset(skip).limit(limit).all()
   
   return {
       "status_code" : 200,
       "message": "Employee fetched successfully",
       "data" : employeeslist,
       "pageable" : {
           "total" : total,
           "limit" : limit,
           "page" : page
       }
   }
   
   
@router.get("/getemployee/{employeeId}",response_model=employeresponse)
def getemployee(employeeId:int,db : Session = Depends(get_db),currentuser= Depends(getcurrentuser)):
    
   employee = db.query(employees).filter(employees.id == employeeId).first()
   
   if not employee:
       raise HTTPException(status_code=400,detail="employee not found")
   
   return {
       "status_code" : 200,
       "message": "Employee fetched successfully",
       "data" : employee
   }
   
   
@router.put("/editemployee/{employeeId}",response_model=employeresponse)
def editemployee(request : employeeupdate,employeeId:int,db: Session = Depends(get_db),currentuser= Depends(getcurrentuser)):
    
   employee = db.query(employees).filter(employees.id == employeeId).first()
   
   if not employee:
       raise HTTPException(status_code=400,detail="employee not found")
   
   updateddata = request.model_dump(exclude_unset = True)
   
   for key,value in updateddata.items():
       setattr(employee,key,value)
       
   db.commit()
   db.refresh(employee)
   
   return {
       "status_code" : 200,
       "message" : "Employee details updated successfull",
       "data" : employee
   }
    

@router.delete("/deleteemployee/{employeeId}")
def deleteemployee(employeeId:int,db: Session = Depends(get_db),currentuser= Depends(getcurrentuser)):
    
   employee = db.query(employees).filter(employees.id == employeeId).first()
   
   if not employee:
       raise HTTPException(status_code=400,detail="employee not found")
       
   db.delete(employee)
   db.commit()
   
   return {
       "status_code" : 200,
       "message" : "employee deleted successfull"
   }